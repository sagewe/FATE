import argparse
from fate_client.pipeline.components.fate import HeteroSecureBoost, PSI, Evaluation
from fate_client.pipeline import FateFlowPipeline
from fate_client.pipeline.interface import DataWarehouseChannel
from fate_client.pipeline.utils import test_utils


def main(config="../config.yaml", namespace=""):
    if isinstance(config, str):
        config = test_utils.load_job_config(config)
    parties = config.parties
    guest = parties.guest[0]
    host = parties.host[0]
    arbiter = parties.arbiter[0]

    pipeline = FateFlowPipeline().set_roles(guest=guest, host=host, arbiter=arbiter)

    psi_0 = PSI("psi_0")
    psi_0.guest.component_setting(input_data=DataWarehouseChannel(name="student_hetero_guest",
                                                                    namespace="experiment"))
    psi_0.hosts[0].component_setting(input_data=DataWarehouseChannel(name="student_hetero_host",
                                                                        namespace="experiment"))

    hetero_sbt_0 = HeteroSecureBoost('sbt_0', num_trees=3, max_bin=32, max_depth=3, objective='regression:l2', 
                                    he_param={'kind': 'paillier', 'key_length': 1024}, train_data=psi_0.outputs['output_data'],)
    evaluation_0 = Evaluation(
        'eval_0',
        runtime_roles=['guest'],
        metrics=['rmse'],
        input_data=[hetero_sbt_0.outputs['train_data_output']]
    )

    pipeline.add_task(psi_0)
    pipeline.add_task(hetero_sbt_0)
    pipeline.add_task(evaluation_0)
    pipeline.compile()
    pipeline.fit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("PIPELINE DEMO")
    parser.add_argument("--config", type=str, default="../config.yaml",
                        help="config file")
    parser.add_argument("--namespace", type=str, default="",
                        help="namespace for data stored in FATE")
    args = parser.parse_args()
    main(config=args.config, namespace=args.namespace)