/*
 * Copyright 2019 The FATE Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.fedai.osx.broker.ptp;

import org.apache.commons.lang3.StringUtils;
import org.fedai.osx.broker.ServiceContainer;
import org.fedai.osx.core.constant.ActionType;
import org.fedai.osx.core.context.FateContext;
import org.fedai.osx.core.exceptions.ParameterException;
import org.fedai.osx.core.service.InboundPackage;
import org.ppc.ptp.Osx;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class PtpClusterTopicApplyService extends AbstractPtpServiceAdaptor {
    Logger logger = LoggerFactory.getLogger(PtpClusterTopicApplyService.class);
    @Override
    protected Osx.Outbound doService(FateContext context, InboundPackage<Osx.Inbound> data) {
        try {
            context.setActionType(ActionType.TOPIC_APPLY.getAlias());
            Osx.Inbound inbound = data.getBody();
            String topic = inbound.getMetadataMap().get(Osx.Metadata.MessageTopic.name());
            String instanceId = inbound.getMetadataMap().get(Osx.Metadata.InstanceId.name());
            String sessionId = inbound.getMetadataMap().get(Osx.Header.SessionID.name());
            if (StringUtils.isEmpty(topic)) {
                throw new ParameterException("topic is null");
            }
            if (StringUtils.isEmpty(instanceId)) {
                throw new ParameterException("instanceId is null");
            }
            if (StringUtils.isEmpty(sessionId)) {
                throw new ParameterException("sessionId is null");
            }
            context.setTopic(topic);
            context.setSessionId(sessionId);
            Osx.Outbound outbound = ServiceContainer.transferQueueManager.applyFromMaster(topic, sessionId, instanceId);
            logger.info("====================PtpClusterTopicApplyService================{}=====", outbound);
            return outbound;
        }catch(Exception e){
            e.printStackTrace();
            throw  e;
        }
    }

}
