import os
import sys
import requests

from datetime import datetime

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger('MyLogger')

class Client:
    def __init__(self, host, port, serverId, simId):
        self.host = host
        self.port = port
        self.serverId = serverId
        self.simId = simId
        self.url = f"http://{host}:{port}/v1.0/invoke/{serverId}"
    
    def Init(self):
        self.Create()

    def Create(self):
        msg = { "envId": self.simId }
        res = requests.post(f"{self.url}/method/create", json=msg)
        res = res.json()
        self.instanceId = res["instanceId"]

    def Reset(self):
        res = requests.post(f"{self.url}/method/reset/{self.instanceId}")
        return res

    def ActionSpaceSample(self):
        res = requests.post(f"{self.url}/method/action-space-sample/{self.instanceId}")
        res = res.json()
        return res["action"]

    def ActionSpaceInfo(self):
        res = requests.post(f"{self.url}/method/action-space-info/{self.instanceId}")
        res = res.json()
        return res

    def ObservationSpaceInfo(self):
        res = requests.post(f"{self.url}/method/observation-space-info/{self.instanceId}")
        res = res.json()
        return res

    def Step(self, action):
        msg = { "action": action }
        res = requests.post(f"{self.url}/method/step/{self.instanceId}", json=msg)
        res = res.json()
        return res

    def MonitorStart(self):
        res = requests.post(f"{self.url}/method/monitor-start/{self.instanceId}")
        return res

    def MonitorStop(self):
        res = requests.post(f"{self.url}/method/monitor-stop/{self.instanceId}")
        return res

    # def DebugSlow(self):
    #     req = roadwork_messages.BaseRequest(instanceId=self.instanceId)
    #     res = self.DaprInvoke("debug", req, roadwork_messages.BaseResponse)
    #     return res

    # def DebugFast(self):
    #     data = Any(value='ACTION 1'.encode('utf-8'))
    #     print(f"[Client][DaprInvoke][debug] Creating Envelope {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
    #     envelope = dapr_messages.InvokeServiceEnvelope(id=self.simId, method="debug", data=data)
    #     print(f"[Client][DaprInvoke][debug] Creating Envelope 2 {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
    #     res = self.client.InvokeService(envelope)
    #     print(f"[Client][DaprInvoke][debug] Creating Envelope 3 {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
    #     return res