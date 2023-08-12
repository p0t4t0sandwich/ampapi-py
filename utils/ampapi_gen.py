#!/bin/python3
from __future__ import annotations

import requests
import json

type_dict = {
    "InstanceDatastore": "",
    "ActionResult": "",
    "Int32": "int",
    "IEnumerable<InstanceDatastore>": "list",
    "RunningTask": "",
    "IEnumerable<JObject>": "list[dict]",
    "Guid": "str",
    "Task<RunningTask>": "",
    "IEnumerable<DeploymentTemplate>": "list",
    "String": "str",
    "DeploymentTemplate": "",
    "Boolean": "bool",
    "List<String>": "list[str]",
    "PostCreateActions": "",
    "Dictionary<String, String>": "dict[str, str]",
    "RemoteTargetInfo": "",
    "IEnumerable<ApplicationSpec>": "list",
    "Void": "None",
    "IEnumerable<EndpointInfo>": "list",
    "IEnumerable<IADSInstance>": "list",
    "JObject": "dict",
    "PortProtocol": "str",
    "Task<ActionResult>": "",
    "ActionResult<String>": "",
    "IADSInstance": "bool",
    "Uri": "str",
    "IEnumerable<PortUsage>": "list",
    "Dictionary<String, Int32>": "dict[str, int]",
    "LocalAMPInstance": "",
    "ContainerMemoryPolicy": "",
    "Single": "",
    "Task<JObject>": "",
    "Int64": "int",
    "FileChunkData": "",
    "IEnumerable<BackupManifest>": "list[dict]",
    "Nullable<DateTime>": "",
    "IEnumerable<IAuditLogEntry>": "dict",
    "Dictionary<String, IEnumerable<JObject>>": "dict[str, list[dict]]",
    "IDictionary<String, String>": "dict[str, str]",
    "List<JObject>": "list[dict]",
    "String[]": "list[str]",
    "Task<IEnumerable<AuthRoleSummary>>": "",
    "Task<IDictionary<Guid, String>>": "",
    "Task<AuthRoleSummary>": "",
    "Task<ActionResult<Guid>>": "",
    "Nullable<Boolean>": "bool | None",
    "Task<IEnumerable<String>>": "",
    "ScheduleInfo": "",
    "Int32[]": "list[int]",
    "TimeIntervalTrigger": "",
    "IEnumerable<WebSessionSummary>": "list",
    "Task<IEnumerable<UserInfoSummary>>": "",
    "Task<UserInfo>": "",
    "Task<IEnumerable<UserInfo>>": "",
    "IList<IPermissionsTreeNode>": "list",
    "WebauthnLoginInfo": "",
    "IEnumerable<WebauthnCredentialSummary>": "list",
    "Task<ActionResult<TwoFactorSetupInfo>>": "",
    "IEnumerable<RunningTask>": "", "ModuleInfo": "",
    "Dictionary<String, Dictionary<String, MethodInfoSummary>>": "dict[str, dict]",
    "Object": "",
    "Task<String>": "",
    "UpdateInfo": "",
    "IEnumerable<ListeningPortSummary>": "list",
}

def generate_ampapi(spec: dict) -> None:
    f = open("../ampapi/ampapi.py", "w+")

    with open("./ampapi_core.py", "r") as ac:
        ampapi_core = ac.read()
        f.write(ampapi_core)

    for module in spec.keys():
        methods = spec[module]
        for method in methods.keys():
            methodParams = spec[module][method]["Parameters"]

            ##################### Add docs
            description = ""
            if "Description" in spec[module][method].keys():
                description = spec[module][method]["Description"] + "\n            "

            restdocs = f"\"\"\"{description}"

            ########## Parameters
            for i in range(len(methodParams)):
                name = methodParams[i]["Name"]
                type_name = methodParams[i]["TypeName"]

                # Print out the type if it hasn't been added to the type_dict
                if not type_name in type_dict.keys(): print(type_name)
                description = methodParams[i]["Description"]
                optional = methodParams[i]["Optional"]
                if optional == "true": type_name + ", optional"
                restdocs += f"\n        :param {name}: {description}"

                if not type_dict[type_name] == "":
                    restdocs += f"\n        :type {name}: {type_dict[type_name]} {optional}"
                restdocs += f"\n            AMP Type: {type_name}"
            ##########

            ########## Return type
            return_type = spec[module][method]["ReturnTypeName"]

            # Print out the type if it hasn't been added to the type_dict
            if not return_type in type_dict.keys(): print(return_type)
            restdocs += f"\n        :returns: AMP Type: {return_type}"
            if not type_dict[return_type] == "":
                restdocs += f"\n        :rtype: {type_dict[return_type]}"
            ##########

            restdocs += "\n        \"\"\""
            #####################

            ##################### Set up data and params and type hints
            data = {}
            for i in range(len(methodParams)):
                data[methodParams[i]["Name"]] = methodParams[i]["Name"]

            data_string = ""
            params = ""
            if len(data.keys()) != 0:
                data_string = ", data={"
                for i in range(len(methodParams)):
                    data_string += '\n            "' + methodParams[i]["Name"] + '": ' + methodParams[i]["Name"] + ", "
                if data_string[-1]==",": data_string = data_string[:-2]
                data_string += "\n        }"

                if len(data.keys()) != 0:
                    for i in range(len(methodParams)):
                        param_typehint = ""
                        if not type_dict[methodParams[i]["TypeName"]] == "":
                            param_typehint = f": {type_dict[methodParams[i]['TypeName']]}"
                        params += ", " + methodParams[i]["Name"] + param_typehint

            return_typehint = ""
            # if return_type == "WebauthnLoginInfo":
            #     pass
            # elif not type_dict[return_type] == "":
            #     return_typehint = f" -> {type_dict[return_type]}"

            #####################

            ##################### Add sync method
            sync_method = f"\n    def {module}_{method}(self{params}){return_typehint}:"
            sync_method += f"\n        {restdocs}"
            sync_method += f"\n        return self.APICall(endpoint=\"{module}/{method}\"{data_string})\n"
            #####################

            ##################### Add async method
            async_method = f"\n    async def {module}_{method}Async(self{params}){return_typehint}:"
            async_method += f"\n        {restdocs}"
            async_method += f"\n        return await self.APICallAsync(endpoint=\"{module}/{method}\"{data_string})\n"
            #####################

            template = sync_method + async_method

            f.write(template)

    with open("./ampapi_handler.py", "r") as ah:
        ampapi_handler = ah.read()
        ampapi_handler = ampapi_handler.replace("from typing import TypeVar\nfrom ampapi import AMPAPI\nimport requests\nimport json\nfrom aiohttp import ClientSession\n", "")
        f.write(ampapi_handler)

    f.close()

if __name__ == "__main__":
    res = requests.get("https://raw.githubusercontent.com/p0t4t0sandwich/ampapi-spec/main/APISpec.json")
    res_json = json.loads(res.content)

    generate_ampapi(res_json)
