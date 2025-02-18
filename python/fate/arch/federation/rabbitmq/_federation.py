#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import json
from logging import getLogger
from typing import List, Optional

from fate.arch.abc import PartyMeta

from .._federation import FederationBase
from .._parties import Party
from ._mq_channel import MQChannel
from ._rabbit_manager import RabbitManager

LOGGER = getLogger(__name__)

# default message max size in bytes = 1MB
DEFAULT_MESSAGE_MAX_SIZE = 1048576


class MQ(object):
    def __init__(self, host, port, union_name, policy_id, route_table):
        self.host = host
        self.port = port
        self.union_name = union_name
        self.policy_id = policy_id
        self.route_table = route_table

    def __str__(self):
        return (
            f"MQ(host={self.host}, port={self.port}, union_name={self.union_name}, "
            f"policy_id={self.policy_id}, route_table={self.route_table})"
        )

    def __repr__(self):
        return self.__str__()


class _TopicPair(object):
    def __init__(self, tenant=None, namespace=None, vhost=None, send=None, receive=None):
        self.tenant = tenant
        self.namespace = namespace
        self.vhost = vhost
        self.send = send
        self.receive = receive


class RabbitmqFederation(FederationBase):
    @staticmethod
    def from_conf(
        federation_session_id: str,
        computing_session,
        party: PartyMeta,
        parties: List[PartyMeta],
        route_table: dict,
        host: str,
        port: int,
        mng_port: int,
        base_user: str,
        base_password: str,
        mode: str,
        max_message_size: Optional[int],
        rabbitmq_run: dict = {},
        connection: dict = {},
    ):
        LOGGER.debug(
            f"federation_session_id={federation_session_id}, party={party}, parties={parties},  route_table={route_table}, rabbitmq_run={rabbitmq_run}",
        )
        if max_message_size is None:
            max_message_size = DEFAULT_MESSAGE_MAX_SIZE
        union_name = federation_session_id
        policy_id = federation_session_id
        rabbit_manager = RabbitManager(base_user, base_password, f"{host}:{mng_port}", rabbitmq_run)
        rabbit_manager.create_user(union_name, policy_id)
        mq = MQ(host, port, union_name, policy_id, route_table)

        return RabbitmqFederation(
            federation_session_id,
            computing_session,
            party,
            parties,
            mq,
            rabbit_manager,
            max_message_size,
            connection,
            mode,
        )

    def __init__(
        self,
        session_id,
        computing_session,
        party: PartyMeta,
        parties: List[PartyMeta],
        mq: MQ,
        rabbit_manager: RabbitManager,
        max_message_size,
        connection,
        mode,
    ):
        super().__init__(
            session_id=session_id,
            computing_session=computing_session,
            party=party,
            parties=parties,
            mq=mq,
            max_message_size=max_message_size,
            conf=connection,
        )
        self._rabbit_manager = rabbit_manager
        self._vhost_set = set()
        self._mode = mode

    def __getstate__(self):
        pass

    def destroy(self):
        LOGGER.debug("[rabbitmq.cleanup]start to cleanup...")
        for party in self.parties:
            if self.local_party == party:
                continue
            vhost = self._get_vhost(Party(role=party[0], party_id=party[1]))
            LOGGER.debug(f"[rabbitmq.cleanup]start to cleanup vhost {vhost}...")
            self._rabbit_manager.clean(vhost)
            LOGGER.debug(f"[rabbitmq.cleanup]cleanup vhost {vhost} done")
        if self._mq.union_name:
            LOGGER.debug(f"[rabbitmq.cleanup]clean user {self._mq.union_name}.")
            self._rabbit_manager.delete_user(user=self._mq.union_name)

    def _get_vhost(self, party):
        low, high = (self._party, party) if self._party < party else (party, self._party)
        vhost = f"{self._session_id}-{low.role}-{low.party_id}-{high.role}-{high.party_id}"
        return vhost

    def _maybe_create_topic_and_replication(self, party, topic_suffix):
        if self._mode == "replication":
            return self._create_topic_by_replication_mode(party, topic_suffix)

        if self._mode == "client":
            return self._create_topic_by_client_mode(party, topic_suffix)

        raise ValueError("mode={self._mode} is not support!")

    def _create_topic_by_client_mode(self, party, topic_suffix):
        # gen names
        vhost_name = self._get_vhost(party)
        send_queue_name = f"{self._session_id}-{self._party.role}-{self._party.party_id}-{party.role}-{party.party_id}-{topic_suffix}"
        receive_queue_name = f"{self._session_id}-{party.role}-{party.party_id}-{self._party.role}-{self._party.party_id}-{topic_suffix}"

        topic_pair = _TopicPair(
            namespace=self._session_id,
            vhost=vhost_name,
            send=send_queue_name,
            receive=receive_queue_name,
        )

        # initial vhost
        if topic_pair.vhost not in self._vhost_set:
            self._rabbit_manager.create_vhost(topic_pair.vhost)
            self._rabbit_manager.add_user_to_vhost(self._mq.union_name, topic_pair.vhost)
            self._vhost_set.add(topic_pair.vhost)

        # initial send queue, the name is send-${vhost}
        self._rabbit_manager.create_queue(topic_pair.vhost, topic_pair.send)
        # initial receive queue, the name is receive-${vhost}
        self._rabbit_manager.create_queue(topic_pair.vhost, topic_pair.receive)

        return topic_pair

    def _create_topic_by_replication_mode(self, party, topic_suffix):
        # gen names
        vhost_name = self._get_vhost(party)
        send_queue_name = f"send-{self._session_id}-{self._party.role}-{self._party.party_id}-{party.role}-{party.party_id}-{topic_suffix}"
        receive_queue_name = f"receive-{self._session_id}-{party.role}-{party.party_id}-{self._party.role}-{self._party.party_id}-{topic_suffix}"

        topic_pair = _TopicPair(
            namespace=self._session_id,
            vhost=vhost_name,
            send=send_queue_name,
            receive=receive_queue_name,
        )

        # initial vhost
        if topic_pair.vhost not in self._vhost_set:
            self._rabbit_manager.create_vhost(topic_pair.vhost)
            self._rabbit_manager.add_user_to_vhost(self._mq.union_name, topic_pair.vhost)
            self._vhost_set.add(topic_pair.vhost)

        # initial send queue, the name is send-${vhost}
        self._rabbit_manager.create_queue(topic_pair.vhost, topic_pair.send)

        # initial receive queue, the name is receive-${vhost}
        self._rabbit_manager.create_queue(topic_pair.vhost, topic_pair.receive)

        upstream_uri = self._upstream_uri(party_id=party.party_id)
        self._rabbit_manager.federate_queue(
            upstream_host=upstream_uri,
            vhost=topic_pair.vhost,
            send_queue_name=topic_pair.send,
            receive_queue_name=topic_pair.receive,
        )

        return topic_pair

    def _upstream_uri(self, party_id):
        host = self._mq.route_table.get(party_id).get("host")
        port = self._mq.route_table.get(party_id).get("port")
        upstream_uri = f"amqp://{self._mq.union_name}:{self._mq.policy_id}@{host}:{port}"
        return upstream_uri

    def _get_channel(
        self,
        topic_pair,
        src_party_id,
        src_role,
        dst_party_id,
        dst_role,
        mq,
        conf: dict = None,
    ):
        LOGGER.debug(
            f"rabbitmq federation _get_channel, src_party_id={src_party_id}, src_role={src_role},"
            f"dst_party_id={dst_party_id}, dst_role={dst_role}"
        )
        return MQChannel(
            host=mq.host,
            port=mq.port,
            user=mq.union_name,
            password=mq.policy_id,
            namespace=topic_pair.namespace,
            vhost=topic_pair.vhost,
            send_queue_name=topic_pair.send,
            receive_queue_name=topic_pair.receive,
            src_party_id=src_party_id,
            src_role=src_role,
            dst_party_id=dst_party_id,
            dst_role=dst_role,
            extra_args=conf,
        )

    def _get_consume_message(self, channel_info):
        for method, properties, body in channel_info.consume():
            LOGGER.debug(f"[rabbitmq._get_consume_message] method: {method}, properties: {properties}")

            properties = {
                "message_id": properties.message_id,
                "correlation_id": properties.correlation_id,
                "content_type": properties.content_type,
                "headers": json.dumps(properties.headers),
            }

            yield method.delivery_tag, properties, body

    def _consume_ack(self, channel_info, id):
        channel_info.ack(delivery_tag=id)
