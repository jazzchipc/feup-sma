import logging
import typing
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import grpc

from multi_agent_gym import utils

from multi_agent_gym.protos import proto_env_message_pb2
from multi_agent_gym.protos import proto_env_message_pb2_grpc

logger = utils.logger.create_standard_logger(__name__, logging.DEBUG)


class MultiAgentEnv:
    """
    Responsible for all logic in an environment.
    """

    def __init__(self, agent_envs_ids: typing.List[str]) -> None:
        self.agent_envs_ids = agent_envs_ids
        super().__init__()

    def reset(self, agent_id) -> np.ndarray:
        assert agent_id in self.agent_envs_ids
        return self._reset(agent_id)

    def step(self, agent_id, action):
        assert agent_id in self.agent_envs_ids
        return self._step(agent_id, action)

    def _reset(self, agent_id) -> np.ndarray:
        raise NotImplementedError

    def _step(self, agent_id, action) -> [np.ndarray, float, bool, dict]:
        raise NotImplementedError


class MultiAgentServicer(proto_env_message_pb2_grpc.TurnBasedServerServicer):
    """
    Deals with requests and redirecting to the proper MultiAgentEnv functions.
    """

    def __init__(self, multi_agent_env: MultiAgentEnv) -> None:
        super().__init__()
        self.multi_agent_env = multi_agent_env

    def GetInitialObservation(self,
                              request: proto_env_message_pb2.SubEnvInfo,
                              context) -> proto_env_message_pb2.InitialObservation:
        logger.debug("Received request: {}".format(request))

        initial_observation = self.multi_agent_env.reset(request.sub_env_id)

        initial_observation_proto = proto_env_message_pb2.InitialObservation(
            observation=utils.numproto.ndarray_to_proto(initial_observation))

        return initial_observation_proto

    def GetObservation(self,
                       request: proto_env_message_pb2.ActionInfo,
                       context) -> proto_env_message_pb2.Observation:
        return super().GetObservation(request, context)


class MultiAgentServer:
    """
    Responsible for setting up the servicer to run in a thread.
    """

    def __init__(self, multi_agent_env: MultiAgentEnv, port: int) -> None:
        super().__init__()

        self.multi_agent_env = multi_agent_env
        self.multi_agent_servicer = MultiAgentServicer(multi_agent_env)
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))

        proto_env_message_pb2_grpc.add_TurnBasedServerServicer_to_server(self.multi_agent_servicer, self.server)

        self.port = port
        self.server.add_insecure_port("[::]:{}".format(port))

    def serve(self):
        self.server.start()
        self.server.wait_for_termination()
