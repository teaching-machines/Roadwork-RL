import os
import grpc
import sys

# Roadwork
import proto_compiled.roadwork_pb2 as roadwork_messages
import proto_compiled.roadwork_pb2_grpc as roadwork_services

from google.protobuf.any_pb2 import Any
import protobuf_helpers
from datetime import datetime

class Client:
    def __init__(self, simId, envId):
        self.simId = simId
        self.envId = envId

    def Init(self, host, port):
        self.host = host
        self.port = port
        print(f"Trying to connect on {self.host}:{self.port}")
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.client = roadwork_services.RoadworkStub(self.channel)
        print(f"Started gRPC client on GRPC_PORT: {self.port}")
        req = roadwork_messages.CreateRequest(envId=self.envId)
        res = self.client.Create(req)

        self.instanceId = res.instanceId

    def Reset(self):
        req = roadwork_messages.ResetRequest(instanceId=self.instanceId)
        res = self.client.Reset(req)
        return res.observation

    def ActionSpaceSample(self):
        req = roadwork_messages.ActionSpaceSampleRequest(instanceId=self.instanceId)
        res = self.client.ActionSpaceSample(req)
        return res.action

    def ActionSpaceInfo(self):
        req = roadwork_messages.ActionSpaceInfoRequest(instanceId=self.instanceId)
        res = self.client.ActionSpaceInfo(req)
        return res.result

    def ObservationSpaceInfo(self):
        req = roadwork_messages.ObservationSpaceInfoRequest(instanceId=self.instanceId)
        res = self.client.ObservationSpaceInfo(req)
        return res.result

    def Step(self, action):
        req = roadwork_messages.StepRequest(instanceId=self.instanceId, action=action)
        res = self.client.Step(req)
        return res

    def MonitorStart(self):
        req = roadwork_messages.BaseRequest(instanceId=self.instanceId)
        res = self.client.MonitorStart(req)
        return res

    def MonitorStop(self):
        req = roadwork_messages.BaseRequest(instanceId=self.instanceId)
        res = self.client.MonitorStop()
        return res