#!/bin/python3

from dataclasses import dataclass

import requests
import json

import asyncstdlib as a

@dataclass
class Module:
    def __setattr__(self, name, value) -> None:
        if value is not None:
            self.__dict__[name] = value

    def __getattr__(self, name):
        return self.__dict__[name]

    def __setitem__(self, name, value) -> None:
        if value is not None:
            self.__dict__[name] = value

    def __getitem__(self, name):
        return self.__dict__[name]

@dataclass
class AMPAPI():
    def __init__(self, baseUri: str) -> None:
        self.baseUri = baseUri
        self.sessionId = ""
        self.dataSource = ""
        self.API = {"Core": {"GetAPISpec": {}}}

        if not self.baseUri[-1] == "/":
            self.dataSource = self.baseUri + "/API"
        else:
            self.dataSource = self.baseUri + "API"

    def __setattr__(self, name, value) -> None:
        if value is not None:
            self.__dict__[name] = value

    def __getattr__(self, name):
        return self.__dict__[name]

    def __setitem__(self, name, value) -> None:
        if value is not None:
            self.__dict__[name] = value

    def __getitem__(self, name):
        return self.__dict__[name]

    def APICall(self, module, methodName, args):
        headers = {'accept': 'text/javascript',}

        method = self.API[module][methodName]

        if "Parameters" in method.keys():
            methodParams = self.API[module][methodName]["Parameters"]
            data = {methodParams[i]["Name"]:args[i] for i in range(len(methodParams))}
        else: data = {}

        data["SESSIONID"] = self.sessionId

        data_json = json.dumps(data)

        res = requests.post(
            url=f'{self.dataSource}/{module}/{methodName}',
            headers=headers,
            data=data_json
        )
        res_json = json.loads(res.content)

        return res_json

    def init(self, stage2: bool = False) -> bool:
        for module in self.API.keys():
            methods = self.API[module]
            self[module] = Module()

            for method in methods.keys():
                self[module][method] = lambda *args, module=module, method=method: self.APICall(module, method, args)

        if stage2:
            return True

        else:
            result = self["Core"]["GetAPISpec"]()
            if result != None:
                self.API = result["result"]
                return self.init(True)
            else:
                return False