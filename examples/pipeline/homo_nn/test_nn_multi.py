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

import argparse
from fate_test.utils import parse_summary_result
from fate_client.pipeline import FateFlowPipeline
from fate_client.pipeline.interface import DataWarehouseChannel
from fate_client.pipeline.utils import test_utils
from fate_client.pipeline.components.fate.evaluation import Evaluation
from fate_client.pipeline import FateFlowPipeline
from fate_client.pipeline.interface import DataWarehouseChannel
from fate_client.pipeline.components.fate.nn.torch import nn, optim
from fate_client.pipeline.components.fate.nn.torch.base import Sequential
from fate_client.pipeline.components.fate.nn.loader import ModelLoader
from fate_client.pipeline.components.fate.homo_nn import HomoNN, get_config_of_default_runner
from fate_client.pipeline.components.fate.nn.algo_params import TrainingArguments, FedAVGArguments


def main(config="../../config.yaml", namespace=""):
    # obtain config
    if isinstance(config, str):
        config = test_utils.load_job_config(config)
    parties = config.parties
    guest = parties.guest[0]
    host = parties.host[0]
    arbiter = parties.arbiter[0]

    epochs = 10
    batch_size = 64
    in_feat = 18
    lr = 0.01
    class_num=4

    guest_train_data = {"name": "vehicle_scale_homo_guest", "namespace": f"experiment{namespace}"}
    host_train_data = {"name": "vehicle_scale_homo_host", "namespace": f"experiment{namespace}"}
    pipeline = FateFlowPipeline().set_roles(guest=guest, host=host, arbiter=arbiter)

    conf = get_config_of_default_runner(
        algo='fedavg',
        model=ModelLoader('multi_model', 'Multi', feat=in_feat, class_num=class_num), 
        loss=nn.CrossEntropyLoss(),
        optimizer=optim.Adam(lr=lr),
        training_args=TrainingArguments(num_train_epochs=epochs, per_device_train_batch_size=batch_size, seed=114514),
        fed_args=FedAVGArguments(),
        task_type='multi'
        )


    homo_nn_0 = HomoNN(
        'nn_0',
        runner_conf=conf
    )

    homo_nn_0.guest.component_setting(train_data=DataWarehouseChannel(name=guest_train_data["name"], namespace=guest_train_data["namespace"]))
    homo_nn_0.hosts[0].component_setting(train_data=DataWarehouseChannel(name=host_train_data["name"], namespace=host_train_data["namespace"]))

    evaluation_0 = Evaluation(
        'eval_0',
        runtime_roles=['guest'],
        default_eval_setting='multi',
        input_data=[homo_nn_0.outputs['train_data_output']]
    )


    pipeline.add_task(homo_nn_0)
    pipeline.add_task(evaluation_0)
    pipeline.compile()
    pipeline.fit()

    result_summary = parse_summary_result(pipeline.get_task_info("eval_0").get_output_metric()[0]["data"])
    print(f"result_summary: {result_summary}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("PIPELINE DEMO")
    parser.add_argument("--config", type=str, default="../config.yaml",
                        help="config file")
    parser.add_argument("--namespace", type=str, default="",
                        help="namespace for data stored in FATE")
    args = parser.parse_args()
    main(config=args.config, namespace=args.namespace)