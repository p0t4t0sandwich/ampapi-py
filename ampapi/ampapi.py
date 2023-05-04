#!/bin/python3
from __future__ import annotations
from typing import TypeVar

import requests
import json

from aiohttp import ClientSession

class AMPAPI():
    """Class for interacting with the AMP API"""
    def __init__(self, baseUri: str) -> None:
        """Initializes the AMP API class
        :param baseUri: The base URI of the AMP instance
        :type baseUri: str
        :returns: None
        """
        self.baseUri = baseUri
        self.sessionId = ""
        self.dataSource = ""

        if not self.baseUri[-1] == "/":
            self.dataSource = self.baseUri + "/API"
        else:
            self.dataSource = self.baseUri + "API"

    def APICall(self, endpoint: str, data: dict = {}) -> dict:
        """Method to make AMP API calls
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :returns: dict with the result of the API call
        :rtype: dict
        """
        headers = {'Accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)

        data_json = json.dumps(data_added)

        res = requests.post(
            url=f"{self.dataSource}/{endpoint}",
            headers=headers,
            data=data_json
        )
        res_json = json.loads(res.content)

        return res_json

    async def APICallAsync(self, endpoint: str, data: dict = {}) -> dict:
        """Method to make AMP API calls
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :returns: dict with the result of the API call
        :rtype: dict
        """
        headers = {'accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)

        data_json = json.dumps(data_added)

        async with ClientSession() as session:
            async with session.post(url=f'{self.dataSource}/{endpoint}', headers=headers, data=data_json) as post:
                response = await post.json()
                post.close()

        return response

    def ADSModule_AddDatastore(self, newDatastore):
        """
        :param newDatastore: 
            AMP Type: InstanceDatastore
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/AddDatastore", data={
            "newDatastore": newDatastore, 
        })

    async def ADSModule_AddDatastoreAsync(self, newDatastore):
        """
        :param newDatastore: 
            AMP Type: InstanceDatastore
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/AddDatastore", data={
            "newDatastore": newDatastore, 
        })

    def ADSModule_DeleteDatastore(self, id: int):
        """
        :param id: 
        :type id: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/DeleteDatastore", data={
            "id": id, 
        })

    async def ADSModule_DeleteDatastoreAsync(self, id: int):
        """
        :param id: 
        :type id: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/DeleteDatastore", data={
            "id": id, 
        })

    def ADSModule_UpdateDatastore(self, updatedDatastore):
        """
        :param updatedDatastore: 
            AMP Type: InstanceDatastore
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/UpdateDatastore", data={
            "updatedDatastore": updatedDatastore, 
        })

    async def ADSModule_UpdateDatastoreAsync(self, updatedDatastore):
        """
        :param updatedDatastore: 
            AMP Type: InstanceDatastore
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/UpdateDatastore", data={
            "updatedDatastore": updatedDatastore, 
        })

    def ADSModule_GetDatastores(self):
        """
        :returns: AMP Type: IEnumerable<InstanceDatastore>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetDatastores")

    async def ADSModule_GetDatastoresAsync(self):
        """
        :returns: AMP Type: IEnumerable<InstanceDatastore>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="ADSModule/GetDatastores")

    def ADSModule_RequestDatastoreSizeCalculation(self, datastoreId: int):
        """
        :param datastoreId: 
        :type datastoreId: intFalse
            AMP Type: Int32
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="ADSModule/RequestDatastoreSizeCalculation", data={
            "datastoreId": datastoreId, 
        })

    async def ADSModule_RequestDatastoreSizeCalculationAsync(self, datastoreId: int):
        """
        :param datastoreId: 
        :type datastoreId: intFalse
            AMP Type: Int32
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="ADSModule/RequestDatastoreSizeCalculation", data={
            "datastoreId": datastoreId, 
        })

    def ADSModule_GetDatastore(self, id: int):
        """
        :param id: 
        :type id: intFalse
            AMP Type: Int32
        :returns: AMP Type: InstanceDatastore
        """
        return self.APICall(endpoint="ADSModule/GetDatastore", data={
            "id": id, 
        })

    async def ADSModule_GetDatastoreAsync(self, id: int):
        """
        :param id: 
        :type id: intFalse
            AMP Type: Int32
        :returns: AMP Type: InstanceDatastore
        """
        return await self.APICallAsync(endpoint="ADSModule/GetDatastore", data={
            "id": id, 
        })

    def ADSModule_RepairDatastore(self, id: int):
        """
        :param id: 
        :type id: intFalse
            AMP Type: Int32
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="ADSModule/RepairDatastore", data={
            "id": id, 
        })

    async def ADSModule_RepairDatastoreAsync(self, id: int):
        """
        :param id: 
        :type id: intFalse
            AMP Type: Int32
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="ADSModule/RepairDatastore", data={
            "id": id, 
        })

    def ADSModule_GetDatastoreInstances(self, datastoreId: int):
        """
        :param datastoreId: 
        :type datastoreId: intFalse
            AMP Type: Int32
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="ADSModule/GetDatastoreInstances", data={
            "datastoreId": datastoreId, 
        })

    async def ADSModule_GetDatastoreInstancesAsync(self, datastoreId: int):
        """
        :param datastoreId: 
        :type datastoreId: intFalse
            AMP Type: Int32
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="ADSModule/GetDatastoreInstances", data={
            "datastoreId": datastoreId, 
        })

    def ADSModule_MoveInstanceDatastore(self, instanceId: str, datastoreId: int):
        """
        :param instanceId: 
        :type instanceId: strFalse
            AMP Type: Guid
        :param datastoreId: 
        :type datastoreId: intFalse
            AMP Type: Int32
        :returns: AMP Type: Task<RunningTask>
        """
        return self.APICall(endpoint="ADSModule/MoveInstanceDatastore", data={
            "instanceId": instanceId, 
            "datastoreId": datastoreId, 
        })

    async def ADSModule_MoveInstanceDatastoreAsync(self, instanceId: str, datastoreId: int):
        """
        :param instanceId: 
        :type instanceId: strFalse
            AMP Type: Guid
        :param datastoreId: 
        :type datastoreId: intFalse
            AMP Type: Int32
        :returns: AMP Type: Task<RunningTask>
        """
        return await self.APICallAsync(endpoint="ADSModule/MoveInstanceDatastore", data={
            "instanceId": instanceId, 
            "datastoreId": datastoreId, 
        })

    def ADSModule_GetDeploymentTemplates(self):
        """
        :returns: AMP Type: IEnumerable<DeploymentTemplate>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetDeploymentTemplates")

    async def ADSModule_GetDeploymentTemplatesAsync(self):
        """
        :returns: AMP Type: IEnumerable<DeploymentTemplate>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="ADSModule/GetDeploymentTemplates")

    def ADSModule_CreateDeploymentTemplate(self, Name: str):
        """
        :param Name: 
        :type Name: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/CreateDeploymentTemplate", data={
            "Name": Name, 
        })

    async def ADSModule_CreateDeploymentTemplateAsync(self, Name: str):
        """
        :param Name: 
        :type Name: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/CreateDeploymentTemplate", data={
            "Name": Name, 
        })

    def ADSModule_UpdateDeploymentTemplate(self, templateToUpdate):
        """
        :param templateToUpdate: 
            AMP Type: DeploymentTemplate
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/UpdateDeploymentTemplate", data={
            "templateToUpdate": templateToUpdate, 
        })

    async def ADSModule_UpdateDeploymentTemplateAsync(self, templateToUpdate):
        """
        :param templateToUpdate: 
            AMP Type: DeploymentTemplate
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/UpdateDeploymentTemplate", data={
            "templateToUpdate": templateToUpdate, 
        })

    def ADSModule_DeleteDeploymentTemplate(self, Id: int):
        """
        :param Id: 
        :type Id: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/DeleteDeploymentTemplate", data={
            "Id": Id, 
        })

    async def ADSModule_DeleteDeploymentTemplateAsync(self, Id: int):
        """
        :param Id: 
        :type Id: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/DeleteDeploymentTemplate", data={
            "Id": Id, 
        })

    def ADSModule_CloneTemplate(self, Id: int, NewName: str):
        """
        :param Id: 
        :type Id: intFalse
            AMP Type: Int32
        :param NewName: 
        :type NewName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/CloneTemplate", data={
            "Id": Id, 
            "NewName": NewName, 
        })

    async def ADSModule_CloneTemplateAsync(self, Id: int, NewName: str):
        """
        :param Id: 
        :type Id: intFalse
            AMP Type: Int32
        :param NewName: 
        :type NewName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/CloneTemplate", data={
            "Id": Id, 
            "NewName": NewName, 
        })

    def ADSModule_ApplyTemplate(self, InstanceID: str, TemplateID: int, NewFriendlyName: str, Secret: str, RestartIfPreviouslyRunning: bool):
        """Overlays an existing template on an existing instance. Used to perform package reconfigurations. Do not use this to 'transform' an existing application into another. The instance should be deleted and re-created in that situation.
            
        :param InstanceID: 
        :type InstanceID: strFalse
            AMP Type: Guid
        :param TemplateID: 
        :type TemplateID: intFalse
            AMP Type: Int32
        :param NewFriendlyName: 
        :type NewFriendlyName: strTrue
            AMP Type: String
        :param Secret: 
        :type Secret: strTrue
            AMP Type: String
        :param RestartIfPreviouslyRunning: 
        :type RestartIfPreviouslyRunning: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/ApplyTemplate", data={
            "InstanceID": InstanceID, 
            "TemplateID": TemplateID, 
            "NewFriendlyName": NewFriendlyName, 
            "Secret": Secret, 
            "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning, 
        })

    async def ADSModule_ApplyTemplateAsync(self, InstanceID: str, TemplateID: int, NewFriendlyName: str, Secret: str, RestartIfPreviouslyRunning: bool):
        """Overlays an existing template on an existing instance. Used to perform package reconfigurations. Do not use this to 'transform' an existing application into another. The instance should be deleted and re-created in that situation.
            
        :param InstanceID: 
        :type InstanceID: strFalse
            AMP Type: Guid
        :param TemplateID: 
        :type TemplateID: intFalse
            AMP Type: Int32
        :param NewFriendlyName: 
        :type NewFriendlyName: strTrue
            AMP Type: String
        :param Secret: 
        :type Secret: strTrue
            AMP Type: String
        :param RestartIfPreviouslyRunning: 
        :type RestartIfPreviouslyRunning: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/ApplyTemplate", data={
            "InstanceID": InstanceID, 
            "TemplateID": TemplateID, 
            "NewFriendlyName": NewFriendlyName, 
            "Secret": Secret, 
            "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning, 
        })

    def ADSModule_DeployTemplate(self, TemplateID: int, NewUsername: str, NewPassword: str, NewEmail: str, RequiredTags: list[str], Tag: str, FriendlyName: str, Secret: str, PostCreate, ExtraProvisionSettings: dict[str, str]):
        """
        :param TemplateID: The ID of the template to be deployed, as per the Template Management UI in AMP itself.
        :type TemplateID: intFalse
            AMP Type: Int32
        :param NewUsername: If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user.
        :type NewUsername: strTrue
            AMP Type: String
        :param NewPassword: If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user.
        :type NewPassword: strTrue
            AMP Type: String
        :param NewEmail: If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user.
        :type NewEmail: strTrue
            AMP Type: String
        :param RequiredTags: If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings.
        :type RequiredTags: list[str]True
            AMP Type: List<String>
        :param Tag: Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique.
        :type Tag: strTrue
            AMP Type: String
        :param FriendlyName: A friendly name for this instance. If left blank, AMP will generate one for you.
        :type FriendlyName: strTrue
            AMP Type: String
        :param Secret: Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request.
        :type Secret: strTrue
            AMP Type: String
        :param PostCreate: 0: Do nothing, 10: Start instance only, 20: Start instance and update application, 30: Full application startup.
            AMP Type: PostCreateActions
        :param ExtraProvisionSettings: A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself.
        :type ExtraProvisionSettings: dict[str, str]True
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="ADSModule/DeployTemplate", data={
            "TemplateID": TemplateID, 
            "NewUsername": NewUsername, 
            "NewPassword": NewPassword, 
            "NewEmail": NewEmail, 
            "RequiredTags": RequiredTags, 
            "Tag": Tag, 
            "FriendlyName": FriendlyName, 
            "Secret": Secret, 
            "PostCreate": PostCreate, 
            "ExtraProvisionSettings": ExtraProvisionSettings, 
        })

    async def ADSModule_DeployTemplateAsync(self, TemplateID: int, NewUsername: str, NewPassword: str, NewEmail: str, RequiredTags: list[str], Tag: str, FriendlyName: str, Secret: str, PostCreate, ExtraProvisionSettings: dict[str, str]):
        """
        :param TemplateID: The ID of the template to be deployed, as per the Template Management UI in AMP itself.
        :type TemplateID: intFalse
            AMP Type: Int32
        :param NewUsername: If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user.
        :type NewUsername: strTrue
            AMP Type: String
        :param NewPassword: If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user.
        :type NewPassword: strTrue
            AMP Type: String
        :param NewEmail: If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user.
        :type NewEmail: strTrue
            AMP Type: String
        :param RequiredTags: If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings.
        :type RequiredTags: list[str]True
            AMP Type: List<String>
        :param Tag: Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique.
        :type Tag: strTrue
            AMP Type: String
        :param FriendlyName: A friendly name for this instance. If left blank, AMP will generate one for you.
        :type FriendlyName: strTrue
            AMP Type: String
        :param Secret: Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request.
        :type Secret: strTrue
            AMP Type: String
        :param PostCreate: 0: Do nothing, 10: Start instance only, 20: Start instance and update application, 30: Full application startup.
            AMP Type: PostCreateActions
        :param ExtraProvisionSettings: A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself.
        :type ExtraProvisionSettings: dict[str, str]True
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="ADSModule/DeployTemplate", data={
            "TemplateID": TemplateID, 
            "NewUsername": NewUsername, 
            "NewPassword": NewPassword, 
            "NewEmail": NewEmail, 
            "RequiredTags": RequiredTags, 
            "Tag": Tag, 
            "FriendlyName": FriendlyName, 
            "Secret": Secret, 
            "PostCreate": PostCreate, 
            "ExtraProvisionSettings": ExtraProvisionSettings, 
        })

    def ADSModule_GetTargetInfo(self):
        """
        :returns: AMP Type: RemoteTargetInfo
        """
        return self.APICall(endpoint="ADSModule/GetTargetInfo")

    async def ADSModule_GetTargetInfoAsync(self):
        """
        :returns: AMP Type: RemoteTargetInfo
        """
        return await self.APICallAsync(endpoint="ADSModule/GetTargetInfo")

    def ADSModule_GetSupportedApplications(self):
        """
        :returns: AMP Type: IEnumerable<ApplicationSpec>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetSupportedApplications")

    async def ADSModule_GetSupportedApplicationsAsync(self):
        """
        :returns: AMP Type: IEnumerable<ApplicationSpec>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="ADSModule/GetSupportedApplications")

    def ADSModule_RefreshAppCache(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="ADSModule/RefreshAppCache")

    async def ADSModule_RefreshAppCacheAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="ADSModule/RefreshAppCache")

    def ADSModule_RefreshRemoteConfigStores(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="ADSModule/RefreshRemoteConfigStores")

    async def ADSModule_RefreshRemoteConfigStoresAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="ADSModule/RefreshRemoteConfigStores")

    def ADSModule_GetApplicationEndpoints(self, instanceId: str):
        """
        :param instanceId: 
        :type instanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: IEnumerable<EndpointInfo>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetApplicationEndpoints", data={
            "instanceId": instanceId, 
        })

    async def ADSModule_GetApplicationEndpointsAsync(self, instanceId: str):
        """
        :param instanceId: 
        :type instanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: IEnumerable<EndpointInfo>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="ADSModule/GetApplicationEndpoints", data={
            "instanceId": instanceId, 
        })

    def ADSModule_ReactivateLocalInstances(self):
        """
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="ADSModule/ReactivateLocalInstances")

    async def ADSModule_ReactivateLocalInstancesAsync(self):
        """
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="ADSModule/ReactivateLocalInstances")

    def ADSModule_GetInstances(self):
        """
        :returns: AMP Type: IEnumerable<IADSInstance>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetInstances")

    async def ADSModule_GetInstancesAsync(self):
        """
        :returns: AMP Type: IEnumerable<IADSInstance>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="ADSModule/GetInstances")

    def ADSModule_GetInstance(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return self.APICall(endpoint="ADSModule/GetInstance", data={
            "InstanceId": InstanceId, 
        })

    async def ADSModule_GetInstanceAsync(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="ADSModule/GetInstance", data={
            "InstanceId": InstanceId, 
        })

    def ADSModule_ModifyCustomFirewallRule(self, instanceId: str, PortNumber: int, Range: int, Protocol: str, Description: str, Open: bool):
        """
        :param instanceId: 
        :type instanceId: strFalse
            AMP Type: Guid
        :param PortNumber: 
        :type PortNumber: intFalse
            AMP Type: Int32
        :param Range: 
        :type Range: intFalse
            AMP Type: Int32
        :param Protocol: 
        :type Protocol: strFalse
            AMP Type: PortProtocol
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param Open: 
        :type Open: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/ModifyCustomFirewallRule", data={
            "instanceId": instanceId, 
            "PortNumber": PortNumber, 
            "Range": Range, 
            "Protocol": Protocol, 
            "Description": Description, 
            "Open": Open, 
        })

    async def ADSModule_ModifyCustomFirewallRuleAsync(self, instanceId: str, PortNumber: int, Range: int, Protocol: str, Description: str, Open: bool):
        """
        :param instanceId: 
        :type instanceId: strFalse
            AMP Type: Guid
        :param PortNumber: 
        :type PortNumber: intFalse
            AMP Type: Int32
        :param Range: 
        :type Range: intFalse
            AMP Type: Int32
        :param Protocol: 
        :type Protocol: strFalse
            AMP Type: PortProtocol
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param Open: 
        :type Open: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/ModifyCustomFirewallRule", data={
            "instanceId": instanceId, 
            "PortNumber": PortNumber, 
            "Range": Range, 
            "Protocol": Protocol, 
            "Description": Description, 
            "Open": Open, 
        })

    def ADSModule_ManageInstance(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult<String>
        """
        return self.APICall(endpoint="ADSModule/ManageInstance", data={
            "InstanceId": InstanceId, 
        })

    async def ADSModule_ManageInstanceAsync(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult<String>
        """
        return await self.APICallAsync(endpoint="ADSModule/ManageInstance", data={
            "InstanceId": InstanceId, 
        })

    def ADSModule_GetGroup(self, GroupId: str):
        """
        :param GroupId: 
        :type GroupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: IADSInstance
        :rtype: bool
        """
        return self.APICall(endpoint="ADSModule/GetGroup", data={
            "GroupId": GroupId, 
        })

    async def ADSModule_GetGroupAsync(self, GroupId: str):
        """
        :param GroupId: 
        :type GroupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: IADSInstance
        :rtype: bool
        """
        return await self.APICallAsync(endpoint="ADSModule/GetGroup", data={
            "GroupId": GroupId, 
        })

    def ADSModule_RefreshGroup(self, GroupId: str):
        """
        :param GroupId: 
        :type GroupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/RefreshGroup", data={
            "GroupId": GroupId, 
        })

    async def ADSModule_RefreshGroupAsync(self, GroupId: str):
        """
        :param GroupId: 
        :type GroupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/RefreshGroup", data={
            "GroupId": GroupId, 
        })

    def ADSModule_GetLocalInstances(self):
        """
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="ADSModule/GetLocalInstances")

    async def ADSModule_GetLocalInstancesAsync(self):
        """
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="ADSModule/GetLocalInstances")

    def ADSModule_GetInstanceStatuses(self):
        """
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="ADSModule/GetInstanceStatuses")

    async def ADSModule_GetInstanceStatusesAsync(self):
        """
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="ADSModule/GetInstanceStatuses")

    def ADSModule_GetProvisionFitness(self):
        """
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return self.APICall(endpoint="ADSModule/GetProvisionFitness")

    async def ADSModule_GetProvisionFitnessAsync(self):
        """
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="ADSModule/GetProvisionFitness")

    def ADSModule_AttachADS(self, Friendly: str, IsHTTPS: bool, Host: str, Port: int, InstanceID: str):
        """
        :param Friendly: 
        :type Friendly: strFalse
            AMP Type: String
        :param IsHTTPS: 
        :type IsHTTPS: boolFalse
            AMP Type: Boolean
        :param Host: 
        :type Host: strFalse
            AMP Type: String
        :param Port: 
        :type Port: intFalse
            AMP Type: Int32
        :param InstanceID: 
        :type InstanceID: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/AttachADS", data={
            "Friendly": Friendly, 
            "IsHTTPS": IsHTTPS, 
            "Host": Host, 
            "Port": Port, 
            "InstanceID": InstanceID, 
        })

    async def ADSModule_AttachADSAsync(self, Friendly: str, IsHTTPS: bool, Host: str, Port: int, InstanceID: str):
        """
        :param Friendly: 
        :type Friendly: strFalse
            AMP Type: String
        :param IsHTTPS: 
        :type IsHTTPS: boolFalse
            AMP Type: Boolean
        :param Host: 
        :type Host: strFalse
            AMP Type: String
        :param Port: 
        :type Port: intFalse
            AMP Type: Int32
        :param InstanceID: 
        :type InstanceID: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/AttachADS", data={
            "Friendly": Friendly, 
            "IsHTTPS": IsHTTPS, 
            "Host": Host, 
            "Port": Port, 
            "InstanceID": InstanceID, 
        })

    def ADSModule_DetatchTarget(self, Id: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/DetatchTarget", data={
            "Id": Id, 
        })

    async def ADSModule_DetatchTargetAsync(self, Id: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/DetatchTarget", data={
            "Id": Id, 
        })

    def ADSModule_UpdateTargetInfo(self, Id: str, FriendlyName: str, Url: str, Description: str, Tags: list[str]):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :param FriendlyName: 
        :type FriendlyName: strFalse
            AMP Type: String
        :param Url: 
        :type Url: strFalse
            AMP Type: Uri
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param Tags: 
        :type Tags: list[str]False
            AMP Type: List<String>
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/UpdateTargetInfo", data={
            "Id": Id, 
            "FriendlyName": FriendlyName, 
            "Url": Url, 
            "Description": Description, 
            "Tags": Tags, 
        })

    async def ADSModule_UpdateTargetInfoAsync(self, Id: str, FriendlyName: str, Url: str, Description: str, Tags: list[str]):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :param FriendlyName: 
        :type FriendlyName: strFalse
            AMP Type: String
        :param Url: 
        :type Url: strFalse
            AMP Type: Uri
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param Tags: 
        :type Tags: list[str]False
            AMP Type: List<String>
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/UpdateTargetInfo", data={
            "Id": Id, 
            "FriendlyName": FriendlyName, 
            "Url": Url, 
            "Description": Description, 
            "Tags": Tags, 
        })

    def ADSModule_ConvertToManaged(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/ConvertToManaged", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_ConvertToManagedAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/ConvertToManaged", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_GetInstanceNetworkInfo(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: IEnumerable<PortUsage>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetInstanceNetworkInfo", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_GetInstanceNetworkInfoAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: IEnumerable<PortUsage>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="ADSModule/GetInstanceNetworkInfo", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_SetInstanceNetworkInfo(self, InstanceId: str, PortMappings: dict[str, int]):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :param PortMappings: 
        :type PortMappings: dict[str, int]False
            AMP Type: Dictionary<String, Int32>
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/SetInstanceNetworkInfo", data={
            "InstanceId": InstanceId, 
            "PortMappings": PortMappings, 
        })

    async def ADSModule_SetInstanceNetworkInfoAsync(self, InstanceId: str, PortMappings: dict[str, int]):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :param PortMappings: 
        :type PortMappings: dict[str, int]False
            AMP Type: Dictionary<String, Int32>
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/SetInstanceNetworkInfo", data={
            "InstanceId": InstanceId, 
            "PortMappings": PortMappings, 
        })

    def ADSModule_ApplyInstanceConfiguration(self, InstanceID: str, Args: dict[str, str], RebuildConfiguration: bool):
        """
        :param InstanceID: 
        :type InstanceID: strFalse
            AMP Type: Guid
        :param Args: 
        :type Args: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :param RebuildConfiguration: 
        :type RebuildConfiguration: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/ApplyInstanceConfiguration", data={
            "InstanceID": InstanceID, 
            "Args": Args, 
            "RebuildConfiguration": RebuildConfiguration, 
        })

    async def ADSModule_ApplyInstanceConfigurationAsync(self, InstanceID: str, Args: dict[str, str], RebuildConfiguration: bool):
        """
        :param InstanceID: 
        :type InstanceID: strFalse
            AMP Type: Guid
        :param Args: 
        :type Args: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :param RebuildConfiguration: 
        :type RebuildConfiguration: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/ApplyInstanceConfiguration", data={
            "InstanceID": InstanceID, 
            "Args": Args, 
            "RebuildConfiguration": RebuildConfiguration, 
        })

    def ADSModule_CreateLocalInstance(self, Instance, PostCreate):
        """
        :param Instance: 
            AMP Type: LocalAMPInstance
        :param PostCreate: 
            AMP Type: PostCreateActions
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/CreateLocalInstance", data={
            "Instance": Instance, 
            "PostCreate": PostCreate, 
        })

    async def ADSModule_CreateLocalInstanceAsync(self, Instance, PostCreate):
        """
        :param Instance: 
            AMP Type: LocalAMPInstance
        :param PostCreate: 
            AMP Type: PostCreateActions
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/CreateLocalInstance", data={
            "Instance": Instance, 
            "PostCreate": PostCreate, 
        })

    def ADSModule_CreateInstance(self, TargetADSInstance: str, NewInstanceId: str, Module: str, InstanceName: str, FriendlyName: str, IPBinding: str, PortNumber: int, AdminUsername: str, AdminPassword: str, ProvisionSettings: dict[str, str], AutoConfigure: bool, PostCreate, StartOnBoot: bool, DisplayImageSource: str, TargetDatastore: int):
        """
        :param TargetADSInstance: 
        :type TargetADSInstance: strFalse
            AMP Type: Guid
        :param NewInstanceId: 
        :type NewInstanceId: strFalse
            AMP Type: Guid
        :param Module: 
        :type Module: strFalse
            AMP Type: String
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :param FriendlyName: 
        :type FriendlyName: strFalse
            AMP Type: String
        :param IPBinding: 
        :type IPBinding: strFalse
            AMP Type: String
        :param PortNumber: 
        :type PortNumber: intFalse
            AMP Type: Int32
        :param AdminUsername: 
        :type AdminUsername: strFalse
            AMP Type: String
        :param AdminPassword: 
        :type AdminPassword: strFalse
            AMP Type: String
        :param ProvisionSettings: 
        :type ProvisionSettings: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :param AutoConfigure: When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values.
        :type AutoConfigure: boolTrue
            AMP Type: Boolean
        :param PostCreate: 
            AMP Type: PostCreateActions
        :param StartOnBoot: 
        :type StartOnBoot: boolTrue
            AMP Type: Boolean
        :param DisplayImageSource: 
        :type DisplayImageSource: strTrue
            AMP Type: String
        :param TargetDatastore: 
        :type TargetDatastore: intTrue
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/CreateInstance", data={
            "TargetADSInstance": TargetADSInstance, 
            "NewInstanceId": NewInstanceId, 
            "Module": Module, 
            "InstanceName": InstanceName, 
            "FriendlyName": FriendlyName, 
            "IPBinding": IPBinding, 
            "PortNumber": PortNumber, 
            "AdminUsername": AdminUsername, 
            "AdminPassword": AdminPassword, 
            "ProvisionSettings": ProvisionSettings, 
            "AutoConfigure": AutoConfigure, 
            "PostCreate": PostCreate, 
            "StartOnBoot": StartOnBoot, 
            "DisplayImageSource": DisplayImageSource, 
            "TargetDatastore": TargetDatastore, 
        })

    async def ADSModule_CreateInstanceAsync(self, TargetADSInstance: str, NewInstanceId: str, Module: str, InstanceName: str, FriendlyName: str, IPBinding: str, PortNumber: int, AdminUsername: str, AdminPassword: str, ProvisionSettings: dict[str, str], AutoConfigure: bool, PostCreate, StartOnBoot: bool, DisplayImageSource: str, TargetDatastore: int):
        """
        :param TargetADSInstance: 
        :type TargetADSInstance: strFalse
            AMP Type: Guid
        :param NewInstanceId: 
        :type NewInstanceId: strFalse
            AMP Type: Guid
        :param Module: 
        :type Module: strFalse
            AMP Type: String
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :param FriendlyName: 
        :type FriendlyName: strFalse
            AMP Type: String
        :param IPBinding: 
        :type IPBinding: strFalse
            AMP Type: String
        :param PortNumber: 
        :type PortNumber: intFalse
            AMP Type: Int32
        :param AdminUsername: 
        :type AdminUsername: strFalse
            AMP Type: String
        :param AdminPassword: 
        :type AdminPassword: strFalse
            AMP Type: String
        :param ProvisionSettings: 
        :type ProvisionSettings: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :param AutoConfigure: When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values.
        :type AutoConfigure: boolTrue
            AMP Type: Boolean
        :param PostCreate: 
            AMP Type: PostCreateActions
        :param StartOnBoot: 
        :type StartOnBoot: boolTrue
            AMP Type: Boolean
        :param DisplayImageSource: 
        :type DisplayImageSource: strTrue
            AMP Type: String
        :param TargetDatastore: 
        :type TargetDatastore: intTrue
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/CreateInstance", data={
            "TargetADSInstance": TargetADSInstance, 
            "NewInstanceId": NewInstanceId, 
            "Module": Module, 
            "InstanceName": InstanceName, 
            "FriendlyName": FriendlyName, 
            "IPBinding": IPBinding, 
            "PortNumber": PortNumber, 
            "AdminUsername": AdminUsername, 
            "AdminPassword": AdminPassword, 
            "ProvisionSettings": ProvisionSettings, 
            "AutoConfigure": AutoConfigure, 
            "PostCreate": PostCreate, 
            "StartOnBoot": StartOnBoot, 
            "DisplayImageSource": DisplayImageSource, 
            "TargetDatastore": TargetDatastore, 
        })

    def ADSModule_SetInstanceConfig(self, InstanceName: str, SettingNode: str, Value: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :param SettingNode: 
        :type SettingNode: strFalse
            AMP Type: String
        :param Value: 
        :type Value: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/SetInstanceConfig", data={
            "InstanceName": InstanceName, 
            "SettingNode": SettingNode, 
            "Value": Value, 
        })

    async def ADSModule_SetInstanceConfigAsync(self, InstanceName: str, SettingNode: str, Value: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :param SettingNode: 
        :type SettingNode: strFalse
            AMP Type: String
        :param Value: 
        :type Value: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/SetInstanceConfig", data={
            "InstanceName": InstanceName, 
            "SettingNode": SettingNode, 
            "Value": Value, 
        })

    def ADSModule_RefreshInstanceConfig(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/RefreshInstanceConfig", data={
            "InstanceId": InstanceId, 
        })

    async def ADSModule_RefreshInstanceConfigAsync(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/RefreshInstanceConfig", data={
            "InstanceId": InstanceId, 
        })

    def ADSModule_HandoutInstanceConfigs(self, ForModule: str, SettingNode: str, Values: list[str]):
        """
        :param ForModule: 
        :type ForModule: strFalse
            AMP Type: String
        :param SettingNode: 
        :type SettingNode: strFalse
            AMP Type: String
        :param Values: 
        :type Values: list[str]False
            AMP Type: List<String>
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/HandoutInstanceConfigs", data={
            "ForModule": ForModule, 
            "SettingNode": SettingNode, 
            "Values": Values, 
        })

    async def ADSModule_HandoutInstanceConfigsAsync(self, ForModule: str, SettingNode: str, Values: list[str]):
        """
        :param ForModule: 
        :type ForModule: strFalse
            AMP Type: String
        :param SettingNode: 
        :type SettingNode: strFalse
            AMP Type: String
        :param Values: 
        :type Values: list[str]False
            AMP Type: List<String>
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/HandoutInstanceConfigs", data={
            "ForModule": ForModule, 
            "SettingNode": SettingNode, 
            "Values": Values, 
        })

    def ADSModule_GetProvisionArguments(self, ModuleName: str):
        """
        :param ModuleName: 
        :type ModuleName: strFalse
            AMP Type: String
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="ADSModule/GetProvisionArguments", data={
            "ModuleName": ModuleName, 
        })

    async def ADSModule_GetProvisionArgumentsAsync(self, ModuleName: str):
        """
        :param ModuleName: 
        :type ModuleName: strFalse
            AMP Type: String
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="ADSModule/GetProvisionArguments", data={
            "ModuleName": ModuleName, 
        })

    def ADSModule_TestADSLoginDetails(self, url: str, username: str, password: str):
        """
        :param url: 
        :type url: strFalse
            AMP Type: String
        :param username: 
        :type username: strFalse
            AMP Type: String
        :param password: 
        :type password: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/TestADSLoginDetails", data={
            "url": url, 
            "username": username, 
            "password": password, 
        })

    async def ADSModule_TestADSLoginDetailsAsync(self, url: str, username: str, password: str):
        """
        :param url: 
        :type url: strFalse
            AMP Type: String
        :param username: 
        :type username: strFalse
            AMP Type: String
        :param password: 
        :type password: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/TestADSLoginDetails", data={
            "url": url, 
            "username": username, 
            "password": password, 
        })

    def ADSModule_RegisterTarget(self, controllerUrl: str, myUrl: str, username: str, password: str, twoFactorToken: str, friendlyName: str):
        """
        :param controllerUrl: 
        :type controllerUrl: strFalse
            AMP Type: String
        :param myUrl: 
        :type myUrl: strFalse
            AMP Type: String
        :param username: 
        :type username: strFalse
            AMP Type: String
        :param password: 
        :type password: strFalse
            AMP Type: String
        :param twoFactorToken: 
        :type twoFactorToken: strFalse
            AMP Type: String
        :param friendlyName: 
        :type friendlyName: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/RegisterTarget", data={
            "controllerUrl": controllerUrl, 
            "myUrl": myUrl, 
            "username": username, 
            "password": password, 
            "twoFactorToken": twoFactorToken, 
            "friendlyName": friendlyName, 
        })

    async def ADSModule_RegisterTargetAsync(self, controllerUrl: str, myUrl: str, username: str, password: str, twoFactorToken: str, friendlyName: str):
        """
        :param controllerUrl: 
        :type controllerUrl: strFalse
            AMP Type: String
        :param myUrl: 
        :type myUrl: strFalse
            AMP Type: String
        :param username: 
        :type username: strFalse
            AMP Type: String
        :param password: 
        :type password: strFalse
            AMP Type: String
        :param twoFactorToken: 
        :type twoFactorToken: strFalse
            AMP Type: String
        :param friendlyName: 
        :type friendlyName: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/RegisterTarget", data={
            "controllerUrl": controllerUrl, 
            "myUrl": myUrl, 
            "username": username, 
            "password": password, 
            "twoFactorToken": twoFactorToken, 
            "friendlyName": friendlyName, 
        })

    def ADSModule_UpdateTarget(self, TargetID: str):
        """
        :param TargetID: 
        :type TargetID: strFalse
            AMP Type: Guid
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="ADSModule/UpdateTarget", data={
            "TargetID": TargetID, 
        })

    async def ADSModule_UpdateTargetAsync(self, TargetID: str):
        """
        :param TargetID: 
        :type TargetID: strFalse
            AMP Type: Guid
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="ADSModule/UpdateTarget", data={
            "TargetID": TargetID, 
        })

    def ADSModule_UpdateInstanceInfo(self, InstanceId: str, FriendlyName: str, Description: str, StartOnBoot: bool, Suspended: bool, ExcludeFromFirewall: bool, RunInContainer: bool, ContainerMemory: int, MemoryPolicy, ContainerMaxCPU):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: String
        :param FriendlyName: 
        :type FriendlyName: strFalse
            AMP Type: String
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param StartOnBoot: 
        :type StartOnBoot: boolFalse
            AMP Type: Boolean
        :param Suspended: 
        :type Suspended: boolFalse
            AMP Type: Boolean
        :param ExcludeFromFirewall: 
        :type ExcludeFromFirewall: boolFalse
            AMP Type: Boolean
        :param RunInContainer: 
        :type RunInContainer: boolFalse
            AMP Type: Boolean
        :param ContainerMemory: 
        :type ContainerMemory: intFalse
            AMP Type: Int32
        :param MemoryPolicy: 
            AMP Type: ContainerMemoryPolicy
        :param ContainerMaxCPU: 
            AMP Type: Single
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/UpdateInstanceInfo", data={
            "InstanceId": InstanceId, 
            "FriendlyName": FriendlyName, 
            "Description": Description, 
            "StartOnBoot": StartOnBoot, 
            "Suspended": Suspended, 
            "ExcludeFromFirewall": ExcludeFromFirewall, 
            "RunInContainer": RunInContainer, 
            "ContainerMemory": ContainerMemory, 
            "MemoryPolicy": MemoryPolicy, 
            "ContainerMaxCPU": ContainerMaxCPU, 
        })

    async def ADSModule_UpdateInstanceInfoAsync(self, InstanceId: str, FriendlyName: str, Description: str, StartOnBoot: bool, Suspended: bool, ExcludeFromFirewall: bool, RunInContainer: bool, ContainerMemory: int, MemoryPolicy, ContainerMaxCPU):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: String
        :param FriendlyName: 
        :type FriendlyName: strFalse
            AMP Type: String
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param StartOnBoot: 
        :type StartOnBoot: boolFalse
            AMP Type: Boolean
        :param Suspended: 
        :type Suspended: boolFalse
            AMP Type: Boolean
        :param ExcludeFromFirewall: 
        :type ExcludeFromFirewall: boolFalse
            AMP Type: Boolean
        :param RunInContainer: 
        :type RunInContainer: boolFalse
            AMP Type: Boolean
        :param ContainerMemory: 
        :type ContainerMemory: intFalse
            AMP Type: Int32
        :param MemoryPolicy: 
            AMP Type: ContainerMemoryPolicy
        :param ContainerMaxCPU: 
            AMP Type: Single
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/UpdateInstanceInfo", data={
            "InstanceId": InstanceId, 
            "FriendlyName": FriendlyName, 
            "Description": Description, 
            "StartOnBoot": StartOnBoot, 
            "Suspended": Suspended, 
            "ExcludeFromFirewall": ExcludeFromFirewall, 
            "RunInContainer": RunInContainer, 
            "ContainerMemory": ContainerMemory, 
            "MemoryPolicy": MemoryPolicy, 
            "ContainerMaxCPU": ContainerMaxCPU, 
        })

    def ADSModule_SetInstanceSuspended(self, InstanceName: str, Suspended: bool):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :param Suspended: 
        :type Suspended: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/SetInstanceSuspended", data={
            "InstanceName": InstanceName, 
            "Suspended": Suspended, 
        })

    async def ADSModule_SetInstanceSuspendedAsync(self, InstanceName: str, Suspended: bool):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :param Suspended: 
        :type Suspended: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/SetInstanceSuspended", data={
            "InstanceName": InstanceName, 
            "Suspended": Suspended, 
        })

    def ADSModule_UpgradeInstance(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/UpgradeInstance", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_UpgradeInstanceAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/UpgradeInstance", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_StartAllInstances(self):
        """
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/StartAllInstances")

    async def ADSModule_StartAllInstancesAsync(self):
        """
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/StartAllInstances")

    def ADSModule_StopAllInstances(self):
        """
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/StopAllInstances")

    async def ADSModule_StopAllInstancesAsync(self):
        """
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/StopAllInstances")

    def ADSModule_UpgradeAllInstances(self, RestartRunning: bool):
        """
        :param RestartRunning: 
        :type RestartRunning: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/UpgradeAllInstances", data={
            "RestartRunning": RestartRunning, 
        })

    async def ADSModule_UpgradeAllInstancesAsync(self, RestartRunning: bool):
        """
        :param RestartRunning: 
        :type RestartRunning: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/UpgradeAllInstances", data={
            "RestartRunning": RestartRunning, 
        })

    def ADSModule_StartInstance(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/StartInstance", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_StartInstanceAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/StartInstance", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_RestartInstance(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/RestartInstance", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_RestartInstanceAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/RestartInstance", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_StopInstance(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="ADSModule/StopInstance", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_StopInstanceAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="ADSModule/StopInstance", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_DeleteInstanceUsers(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/DeleteInstanceUsers", data={
            "InstanceId": InstanceId, 
        })

    async def ADSModule_DeleteInstanceUsersAsync(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/DeleteInstanceUsers", data={
            "InstanceId": InstanceId, 
        })

    def ADSModule_DeleteInstance(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="ADSModule/DeleteInstance", data={
            "InstanceName": InstanceName, 
        })

    async def ADSModule_DeleteInstanceAsync(self, InstanceName: str):
        """
        :param InstanceName: 
        :type InstanceName: strFalse
            AMP Type: String
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="ADSModule/DeleteInstance", data={
            "InstanceName": InstanceName, 
        })

    def ADSModule_ExtractEverywhere(self, SourceArchive: str):
        """
        :param SourceArchive: 
        :type SourceArchive: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="ADSModule/ExtractEverywhere", data={
            "SourceArchive": SourceArchive, 
        })

    async def ADSModule_ExtractEverywhereAsync(self, SourceArchive: str):
        """
        :param SourceArchive: 
        :type SourceArchive: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="ADSModule/ExtractEverywhere", data={
            "SourceArchive": SourceArchive, 
        })

    def ADSModule_Servers(self, id: str, REQ_RAWJSON: str):
        """
        :param id: 
        :type id: strFalse
            AMP Type: String
        :param REQ_RAWJSON: 
        :type REQ_RAWJSON: strFalse
            AMP Type: String
        :returns: AMP Type: Task<JObject>
        """
        return self.APICall(endpoint="ADSModule/Servers", data={
            "id": id, 
            "REQ_RAWJSON": REQ_RAWJSON, 
        })

    async def ADSModule_ServersAsync(self, id: str, REQ_RAWJSON: str):
        """
        :param id: 
        :type id: strFalse
            AMP Type: String
        :param REQ_RAWJSON: 
        :type REQ_RAWJSON: strFalse
            AMP Type: String
        :returns: AMP Type: Task<JObject>
        """
        return await self.APICallAsync(endpoint="ADSModule/Servers", data={
            "id": id, 
            "REQ_RAWJSON": REQ_RAWJSON, 
        })

    def FileManagerPlugin_Dummy(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="FileManagerPlugin/Dummy")

    async def FileManagerPlugin_DummyAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/Dummy")

    def FileManagerPlugin_CalculateFileMD5Sum(self, FilePath: str):
        """
        :param FilePath: 
        :type FilePath: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult<String>
        """
        return self.APICall(endpoint="FileManagerPlugin/CalculateFileMD5Sum", data={
            "FilePath": FilePath, 
        })

    async def FileManagerPlugin_CalculateFileMD5SumAsync(self, FilePath: str):
        """
        :param FilePath: 
        :type FilePath: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult<String>
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/CalculateFileMD5Sum", data={
            "FilePath": FilePath, 
        })

    def FileManagerPlugin_ChangeExclusion(self, ModifyPath: str, AsDirectory: bool, Exclude: bool):
        """
        :param ModifyPath: 
        :type ModifyPath: strFalse
            AMP Type: String
        :param AsDirectory: 
        :type AsDirectory: boolFalse
            AMP Type: Boolean
        :param Exclude: 
        :type Exclude: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/ChangeExclusion", data={
            "ModifyPath": ModifyPath, 
            "AsDirectory": AsDirectory, 
            "Exclude": Exclude, 
        })

    async def FileManagerPlugin_ChangeExclusionAsync(self, ModifyPath: str, AsDirectory: bool, Exclude: bool):
        """
        :param ModifyPath: 
        :type ModifyPath: strFalse
            AMP Type: String
        :param AsDirectory: 
        :type AsDirectory: boolFalse
            AMP Type: Boolean
        :param Exclude: 
        :type Exclude: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/ChangeExclusion", data={
            "ModifyPath": ModifyPath, 
            "AsDirectory": AsDirectory, 
            "Exclude": Exclude, 
        })

    def FileManagerPlugin_CreateArchive(self, PathToArchive: str):
        """
        :param PathToArchive: 
        :type PathToArchive: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/CreateArchive", data={
            "PathToArchive": PathToArchive, 
        })

    async def FileManagerPlugin_CreateArchiveAsync(self, PathToArchive: str):
        """
        :param PathToArchive: 
        :type PathToArchive: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/CreateArchive", data={
            "PathToArchive": PathToArchive, 
        })

    def FileManagerPlugin_ExtractArchive(self, ArchivePath: str, DestinationPath: str):
        """
        :param ArchivePath: 
        :type ArchivePath: strFalse
            AMP Type: String
        :param DestinationPath: 
        :type DestinationPath: strTrue
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/ExtractArchive", data={
            "ArchivePath": ArchivePath, 
            "DestinationPath": DestinationPath, 
        })

    async def FileManagerPlugin_ExtractArchiveAsync(self, ArchivePath: str, DestinationPath: str):
        """
        :param ArchivePath: 
        :type ArchivePath: strFalse
            AMP Type: String
        :param DestinationPath: 
        :type DestinationPath: strTrue
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/ExtractArchive", data={
            "ArchivePath": ArchivePath, 
            "DestinationPath": DestinationPath, 
        })

    def FileManagerPlugin_GetDirectoryListing(self, Dir: str):
        """
        :param Dir: 
        :type Dir: strFalse
            AMP Type: String
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="FileManagerPlugin/GetDirectoryListing", data={
            "Dir": Dir, 
        })

    async def FileManagerPlugin_GetDirectoryListingAsync(self, Dir: str):
        """
        :param Dir: 
        :type Dir: strFalse
            AMP Type: String
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/GetDirectoryListing", data={
            "Dir": Dir, 
        })

    def FileManagerPlugin_GetFileChunk(self, Filename: str, Position: int, Length: int):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Position: 
        :type Position: intFalse
            AMP Type: Int64
        :param Length: 
        :type Length: intFalse
            AMP Type: Int32
        :returns: AMP Type: FileChunkData
        """
        return self.APICall(endpoint="FileManagerPlugin/GetFileChunk", data={
            "Filename": Filename, 
            "Position": Position, 
            "Length": Length, 
        })

    async def FileManagerPlugin_GetFileChunkAsync(self, Filename: str, Position: int, Length: int):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Position: 
        :type Position: intFalse
            AMP Type: Int64
        :param Length: 
        :type Length: intFalse
            AMP Type: Int32
        :returns: AMP Type: FileChunkData
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/GetFileChunk", data={
            "Filename": Filename, 
            "Position": Position, 
            "Length": Length, 
        })

    def FileManagerPlugin_AppendFileChunk(self, Filename: str, Data: str, Delete: bool):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Data: 
        :type Data: strFalse
            AMP Type: String
        :param Delete: 
        :type Delete: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="FileManagerPlugin/AppendFileChunk", data={
            "Filename": Filename, 
            "Data": Data, 
            "Delete": Delete, 
        })

    async def FileManagerPlugin_AppendFileChunkAsync(self, Filename: str, Data: str, Delete: bool):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Data: 
        :type Data: strFalse
            AMP Type: String
        :param Delete: 
        :type Delete: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/AppendFileChunk", data={
            "Filename": Filename, 
            "Data": Data, 
            "Delete": Delete, 
        })

    def FileManagerPlugin_ReadFileChunk(self, Filename: str, Offset: int):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Offset: 
        :type Offset: intFalse
            AMP Type: Int64
        :returns: AMP Type: ActionResult<String>
        """
        return self.APICall(endpoint="FileManagerPlugin/ReadFileChunk", data={
            "Filename": Filename, 
            "Offset": Offset, 
        })

    async def FileManagerPlugin_ReadFileChunkAsync(self, Filename: str, Offset: int):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Offset: 
        :type Offset: intFalse
            AMP Type: Int64
        :returns: AMP Type: ActionResult<String>
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/ReadFileChunk", data={
            "Filename": Filename, 
            "Offset": Offset, 
        })

    def FileManagerPlugin_WriteFileChunk(self, Filename: str, Data: str, Offset: int, FinalChunk: bool):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Data: 
        :type Data: strFalse
            AMP Type: String
        :param Offset: 
        :type Offset: intFalse
            AMP Type: Int64
        :param FinalChunk: 
        :type FinalChunk: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/WriteFileChunk", data={
            "Filename": Filename, 
            "Data": Data, 
            "Offset": Offset, 
            "FinalChunk": FinalChunk, 
        })

    async def FileManagerPlugin_WriteFileChunkAsync(self, Filename: str, Data: str, Offset: int, FinalChunk: bool):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param Data: 
        :type Data: strFalse
            AMP Type: String
        :param Offset: 
        :type Offset: intFalse
            AMP Type: Int64
        :param FinalChunk: 
        :type FinalChunk: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/WriteFileChunk", data={
            "Filename": Filename, 
            "Data": Data, 
            "Offset": Offset, 
            "FinalChunk": FinalChunk, 
        })

    def FileManagerPlugin_DownloadFileFromURL(self, Source: str, TargetDirectory: str):
        """
        :param Source: 
        :type Source: strFalse
            AMP Type: Uri
        :param TargetDirectory: 
        :type TargetDirectory: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/DownloadFileFromURL", data={
            "Source": Source, 
            "TargetDirectory": TargetDirectory, 
        })

    async def FileManagerPlugin_DownloadFileFromURLAsync(self, Source: str, TargetDirectory: str):
        """
        :param Source: 
        :type Source: strFalse
            AMP Type: Uri
        :param TargetDirectory: 
        :type TargetDirectory: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/DownloadFileFromURL", data={
            "Source": Source, 
            "TargetDirectory": TargetDirectory, 
        })

    def FileManagerPlugin_RenameFile(self, Filename: str, NewFilename: str):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param NewFilename: 
        :type NewFilename: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/RenameFile", data={
            "Filename": Filename, 
            "NewFilename": NewFilename, 
        })

    async def FileManagerPlugin_RenameFileAsync(self, Filename: str, NewFilename: str):
        """
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :param NewFilename: 
        :type NewFilename: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/RenameFile", data={
            "Filename": Filename, 
            "NewFilename": NewFilename, 
        })

    def FileManagerPlugin_CopyFile(self, Origin: str, TargetDirectory: str):
        """
        :param Origin: 
        :type Origin: strFalse
            AMP Type: String
        :param TargetDirectory: 
        :type TargetDirectory: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/CopyFile", data={
            "Origin": Origin, 
            "TargetDirectory": TargetDirectory, 
        })

    async def FileManagerPlugin_CopyFileAsync(self, Origin: str, TargetDirectory: str):
        """
        :param Origin: 
        :type Origin: strFalse
            AMP Type: String
        :param TargetDirectory: 
        :type TargetDirectory: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/CopyFile", data={
            "Origin": Origin, 
            "TargetDirectory": TargetDirectory, 
        })

    def FileManagerPlugin_TrashFile(self, Filename: str):
        """Moves a file to trash, files must be trashed before they can be deleted.
            
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/TrashFile", data={
            "Filename": Filename, 
        })

    async def FileManagerPlugin_TrashFileAsync(self, Filename: str):
        """Moves a file to trash, files must be trashed before they can be deleted.
            
        :param Filename: 
        :type Filename: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/TrashFile", data={
            "Filename": Filename, 
        })

    def FileManagerPlugin_TrashDirectory(self, DirectoryName: str):
        """Moves a directory to trash, files must be trashed before they can be deleted.
            
        :param DirectoryName: 
        :type DirectoryName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/TrashDirectory", data={
            "DirectoryName": DirectoryName, 
        })

    async def FileManagerPlugin_TrashDirectoryAsync(self, DirectoryName: str):
        """Moves a directory to trash, files must be trashed before they can be deleted.
            
        :param DirectoryName: 
        :type DirectoryName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/TrashDirectory", data={
            "DirectoryName": DirectoryName, 
        })

    def FileManagerPlugin_EmptyTrash(self, TrashDirectoryName: str):
        """Empties a trash bin
            
        :param TrashDirectoryName: 
        :type TrashDirectoryName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/EmptyTrash", data={
            "TrashDirectoryName": TrashDirectoryName, 
        })

    async def FileManagerPlugin_EmptyTrashAsync(self, TrashDirectoryName: str):
        """Empties a trash bin
            
        :param TrashDirectoryName: 
        :type TrashDirectoryName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/EmptyTrash", data={
            "TrashDirectoryName": TrashDirectoryName, 
        })

    def FileManagerPlugin_CreateDirectory(self, NewPath: str):
        """Creates a new directory. The parent directory must already exist.
            
        :param NewPath: 
        :type NewPath: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/CreateDirectory", data={
            "NewPath": NewPath, 
        })

    async def FileManagerPlugin_CreateDirectoryAsync(self, NewPath: str):
        """Creates a new directory. The parent directory must already exist.
            
        :param NewPath: 
        :type NewPath: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/CreateDirectory", data={
            "NewPath": NewPath, 
        })

    def FileManagerPlugin_RenameDirectory(self, oldDirectory: str, NewDirectoryName: str):
        """Renames a directory
            
        :param oldDirectory: The full path to the old directory
        :type oldDirectory: strFalse
            AMP Type: String
        :param NewDirectoryName: The name component of the new directory (not the full path)
        :type NewDirectoryName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="FileManagerPlugin/RenameDirectory", data={
            "oldDirectory": oldDirectory, 
            "NewDirectoryName": NewDirectoryName, 
        })

    async def FileManagerPlugin_RenameDirectoryAsync(self, oldDirectory: str, NewDirectoryName: str):
        """Renames a directory
            
        :param oldDirectory: The full path to the old directory
        :type oldDirectory: strFalse
            AMP Type: String
        :param NewDirectoryName: The name component of the new directory (not the full path)
        :type NewDirectoryName: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="FileManagerPlugin/RenameDirectory", data={
            "oldDirectory": oldDirectory, 
            "NewDirectoryName": NewDirectoryName, 
        })

    def EmailSenderPlugin_TestSMTPSettings(self):
        """
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="EmailSenderPlugin/TestSMTPSettings")

    async def EmailSenderPlugin_TestSMTPSettingsAsync(self):
        """
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="EmailSenderPlugin/TestSMTPSettings")

    def LocalFileBackupPlugin_UploadToS3(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/UploadToS3", data={
            "BackupId": BackupId, 
        })

    async def LocalFileBackupPlugin_UploadToS3Async(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/UploadToS3", data={
            "BackupId": BackupId, 
        })

    def LocalFileBackupPlugin_DownloadFromS3(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: RunningTask
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/DownloadFromS3", data={
            "BackupId": BackupId, 
        })

    async def LocalFileBackupPlugin_DownloadFromS3Async(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: RunningTask
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/DownloadFromS3", data={
            "BackupId": BackupId, 
        })

    def LocalFileBackupPlugin_DeleteFromS3(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/DeleteFromS3", data={
            "BackupId": BackupId, 
        })

    async def LocalFileBackupPlugin_DeleteFromS3Async(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/DeleteFromS3", data={
            "BackupId": BackupId, 
        })

    def LocalFileBackupPlugin_GetBackups(self):
        """
        :returns: AMP Type: IEnumerable<BackupManifest>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/GetBackups")

    async def LocalFileBackupPlugin_GetBackupsAsync(self):
        """
        :returns: AMP Type: IEnumerable<BackupManifest>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/GetBackups")

    def LocalFileBackupPlugin_RestoreBackup(self, BackupId: str, DeleteExistingData: bool):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :param DeleteExistingData: 
        :type DeleteExistingData: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/RestoreBackup", data={
            "BackupId": BackupId, 
            "DeleteExistingData": DeleteExistingData, 
        })

    async def LocalFileBackupPlugin_RestoreBackupAsync(self, BackupId: str, DeleteExistingData: bool):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :param DeleteExistingData: 
        :type DeleteExistingData: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/RestoreBackup", data={
            "BackupId": BackupId, 
            "DeleteExistingData": DeleteExistingData, 
        })

    def LocalFileBackupPlugin_DeleteLocalBackup(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/DeleteLocalBackup", data={
            "BackupId": BackupId, 
        })

    async def LocalFileBackupPlugin_DeleteLocalBackupAsync(self, BackupId: str):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/DeleteLocalBackup", data={
            "BackupId": BackupId, 
        })

    def LocalFileBackupPlugin_SetBackupSticky(self, BackupId: str, Sticky: bool):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :param Sticky: 
        :type Sticky: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/SetBackupSticky", data={
            "BackupId": BackupId, 
            "Sticky": Sticky, 
        })

    async def LocalFileBackupPlugin_SetBackupStickyAsync(self, BackupId: str, Sticky: bool):
        """
        :param BackupId: 
        :type BackupId: strFalse
            AMP Type: Guid
        :param Sticky: 
        :type Sticky: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/SetBackupSticky", data={
            "BackupId": BackupId, 
            "Sticky": Sticky, 
        })

    def LocalFileBackupPlugin_TakeBackup(self, Title: str, Description: str, Sticky: bool):
        """
        :param Title: 
        :type Title: strFalse
            AMP Type: String
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param Sticky: 
        :type Sticky: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="LocalFileBackupPlugin/TakeBackup", data={
            "Title": Title, 
            "Description": Description, 
            "Sticky": Sticky, 
        })

    async def LocalFileBackupPlugin_TakeBackupAsync(self, Title: str, Description: str, Sticky: bool):
        """
        :param Title: 
        :type Title: strFalse
            AMP Type: String
        :param Description: 
        :type Description: strFalse
            AMP Type: String
        :param Sticky: 
        :type Sticky: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="LocalFileBackupPlugin/TakeBackup", data={
            "Title": Title, 
            "Description": Description, 
            "Sticky": Sticky, 
        })

    def Core_GetAuditLogEntries(self, Before, Count: int):
        """
        :param Before: 
            AMP Type: Nullable<DateTime>
        :param Count: 
        :type Count: intFalse
            AMP Type: Int32
        :returns: AMP Type: IEnumerable<IAuditLogEntry>
        :rtype: dict
        """
        return self.APICall(endpoint="Core/GetAuditLogEntries", data={
            "Before": Before, 
            "Count": Count, 
        })

    async def Core_GetAuditLogEntriesAsync(self, Before, Count: int):
        """
        :param Before: 
            AMP Type: Nullable<DateTime>
        :param Count: 
        :type Count: intFalse
            AMP Type: Int32
        :returns: AMP Type: IEnumerable<IAuditLogEntry>
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="Core/GetAuditLogEntries", data={
            "Before": Before, 
            "Count": Count, 
        })

    def Core_GetSettingsSpec(self):
        """
        :returns: AMP Type: Dictionary<String, IEnumerable<JObject>>
        :rtype: dict[str, list[dict]]
        """
        return self.APICall(endpoint="Core/GetSettingsSpec")

    async def Core_GetSettingsSpecAsync(self):
        """
        :returns: AMP Type: Dictionary<String, IEnumerable<JObject>>
        :rtype: dict[str, list[dict]]
        """
        return await self.APICallAsync(endpoint="Core/GetSettingsSpec")

    def Core_RefreshSettingValueList(self, Node: str):
        """
        :param Node: 
        :type Node: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/RefreshSettingValueList", data={
            "Node": Node, 
        })

    async def Core_RefreshSettingValueListAsync(self, Node: str):
        """
        :param Node: 
        :type Node: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/RefreshSettingValueList", data={
            "Node": Node, 
        })

    def Core_RefreshSettingsSourceCache(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/RefreshSettingsSourceCache")

    async def Core_RefreshSettingsSourceCacheAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/RefreshSettingsSourceCache")

    def Core_GetSettingValues(self, SettingNode: str, WithRefresh: bool):
        """
        :param SettingNode: 
        :type SettingNode: strFalse
            AMP Type: String
        :param WithRefresh: 
        :type WithRefresh: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: IDictionary<String, String>
        :rtype: dict[str, str]
        """
        return self.APICall(endpoint="Core/GetSettingValues", data={
            "SettingNode": SettingNode, 
            "WithRefresh": WithRefresh, 
        })

    async def Core_GetSettingValuesAsync(self, SettingNode: str, WithRefresh: bool):
        """
        :param SettingNode: 
        :type SettingNode: strFalse
            AMP Type: String
        :param WithRefresh: 
        :type WithRefresh: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: IDictionary<String, String>
        :rtype: dict[str, str]
        """
        return await self.APICallAsync(endpoint="Core/GetSettingValues", data={
            "SettingNode": SettingNode, 
            "WithRefresh": WithRefresh, 
        })

    def Core_GetProvisionSpec(self):
        """
        :returns: AMP Type: List<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="Core/GetProvisionSpec")

    async def Core_GetProvisionSpecAsync(self):
        """
        :returns: AMP Type: List<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="Core/GetProvisionSpec")

    def Core_GetConfig(self, node: str):
        """
        :param node: 
        :type node: strFalse
            AMP Type: String
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return self.APICall(endpoint="Core/GetConfig", data={
            "node": node, 
        })

    async def Core_GetConfigAsync(self, node: str):
        """
        :param node: 
        :type node: strFalse
            AMP Type: String
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="Core/GetConfig", data={
            "node": node, 
        })

    def Core_GetConfigs(self, nodes: list[str]):
        """
        :param nodes: 
        :type nodes: list[str]False
            AMP Type: String[]
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return self.APICall(endpoint="Core/GetConfigs", data={
            "nodes": nodes, 
        })

    async def Core_GetConfigsAsync(self, nodes: list[str]):
        """
        :param nodes: 
        :type nodes: list[str]False
            AMP Type: String[]
        :returns: AMP Type: IEnumerable<JObject>
        :rtype: list[dict]
        """
        return await self.APICallAsync(endpoint="Core/GetConfigs", data={
            "nodes": nodes, 
        })

    def Core_SetConfigs(self, data: dict[str, str]):
        """
        :param data: 
        :type data: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: Boolean
        :rtype: bool
        """
        return self.APICall(endpoint="Core/SetConfigs", data={
            "data": data, 
        })

    async def Core_SetConfigsAsync(self, data: dict[str, str]):
        """
        :param data: 
        :type data: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: Boolean
        :rtype: bool
        """
        return await self.APICallAsync(endpoint="Core/SetConfigs", data={
            "data": data, 
        })

    def Core_SetConfig(self, node: str, value: str):
        """
        :param node: 
        :type node: strFalse
            AMP Type: String
        :param value: 
        :type value: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/SetConfig", data={
            "node": node, 
            "value": value, 
        })

    async def Core_SetConfigAsync(self, node: str, value: str):
        """
        :param node: 
        :type node: strFalse
            AMP Type: String
        :param value: 
        :type value: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/SetConfig", data={
            "node": node, 
            "value": value, 
        })

    def Core_GetRoleData(self):
        """
        :returns: AMP Type: Task<IEnumerable<AuthRoleSummary>>
        """
        return self.APICall(endpoint="Core/GetRoleData")

    async def Core_GetRoleDataAsync(self):
        """
        :returns: AMP Type: Task<IEnumerable<AuthRoleSummary>>
        """
        return await self.APICallAsync(endpoint="Core/GetRoleData")

    def Core_GetRoleIds(self):
        """
        :returns: AMP Type: Task<IDictionary<Guid, String>>
        """
        return self.APICall(endpoint="Core/GetRoleIds")

    async def Core_GetRoleIdsAsync(self):
        """
        :returns: AMP Type: Task<IDictionary<Guid, String>>
        """
        return await self.APICallAsync(endpoint="Core/GetRoleIds")

    def Core_GetRole(self, RoleId: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<AuthRoleSummary>
        """
        return self.APICall(endpoint="Core/GetRole", data={
            "RoleId": RoleId, 
        })

    async def Core_GetRoleAsync(self, RoleId: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<AuthRoleSummary>
        """
        return await self.APICallAsync(endpoint="Core/GetRole", data={
            "RoleId": RoleId, 
        })

    def Core_CreateRole(self, Name: str, AsCommonRole: bool):
        """
        :param Name: 
        :type Name: strFalse
            AMP Type: String
        :param AsCommonRole: 
        :type AsCommonRole: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult<Guid>>
        """
        return self.APICall(endpoint="Core/CreateRole", data={
            "Name": Name, 
            "AsCommonRole": AsCommonRole, 
        })

    async def Core_CreateRoleAsync(self, Name: str, AsCommonRole: bool):
        """
        :param Name: 
        :type Name: strFalse
            AMP Type: String
        :param AsCommonRole: 
        :type AsCommonRole: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult<Guid>>
        """
        return await self.APICallAsync(endpoint="Core/CreateRole", data={
            "Name": Name, 
            "AsCommonRole": AsCommonRole, 
        })

    def Core_DeleteRole(self, RoleId: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/DeleteRole", data={
            "RoleId": RoleId, 
        })

    async def Core_DeleteRoleAsync(self, RoleId: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/DeleteRole", data={
            "RoleId": RoleId, 
        })

    def Core_RenameRole(self, RoleId: str, NewName: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :param NewName: 
        :type NewName: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/RenameRole", data={
            "RoleId": RoleId, 
            "NewName": NewName, 
        })

    async def Core_RenameRoleAsync(self, RoleId: str, NewName: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :param NewName: 
        :type NewName: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/RenameRole", data={
            "RoleId": RoleId, 
            "NewName": NewName, 
        })

    def Core_SetAMPRolePermission(self, RoleId: str, PermissionNode: str, Enabled: bool | None):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :param PermissionNode: 
        :type PermissionNode: strFalse
            AMP Type: String
        :param Enabled: 
        :type Enabled: bool | NoneFalse
            AMP Type: Nullable<Boolean>
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/SetAMPRolePermission", data={
            "RoleId": RoleId, 
            "PermissionNode": PermissionNode, 
            "Enabled": Enabled, 
        })

    async def Core_SetAMPRolePermissionAsync(self, RoleId: str, PermissionNode: str, Enabled: bool | None):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :param PermissionNode: 
        :type PermissionNode: strFalse
            AMP Type: String
        :param Enabled: 
        :type Enabled: bool | NoneFalse
            AMP Type: Nullable<Boolean>
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/SetAMPRolePermission", data={
            "RoleId": RoleId, 
            "PermissionNode": PermissionNode, 
            "Enabled": Enabled, 
        })

    def Core_GetAMPRolePermissions(self, RoleId: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<IEnumerable<String>>
        """
        return self.APICall(endpoint="Core/GetAMPRolePermissions", data={
            "RoleId": RoleId, 
        })

    async def Core_GetAMPRolePermissionsAsync(self, RoleId: str):
        """
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<IEnumerable<String>>
        """
        return await self.APICallAsync(endpoint="Core/GetAMPRolePermissions", data={
            "RoleId": RoleId, 
        })

    def Core_GetScheduleData(self):
        """
        :returns: AMP Type: ScheduleInfo
        """
        return self.APICall(endpoint="Core/GetScheduleData")

    async def Core_GetScheduleDataAsync(self):
        """
        :returns: AMP Type: ScheduleInfo
        """
        return await self.APICallAsync(endpoint="Core/GetScheduleData")

    def Core_AddEventTrigger(self, triggerId: str):
        """
        :param triggerId: 
        :type triggerId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/AddEventTrigger", data={
            "triggerId": triggerId, 
        })

    async def Core_AddEventTriggerAsync(self, triggerId: str):
        """
        :param triggerId: 
        :type triggerId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/AddEventTrigger", data={
            "triggerId": triggerId, 
        })

    def Core_RunEventTriggerImmediately(self, triggerId: str):
        """
        :param triggerId: 
        :type triggerId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/RunEventTriggerImmediately", data={
            "triggerId": triggerId, 
        })

    async def Core_RunEventTriggerImmediatelyAsync(self, triggerId: str):
        """
        :param triggerId: 
        :type triggerId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/RunEventTriggerImmediately", data={
            "triggerId": triggerId, 
        })

    def Core_AddIntervalTrigger(self, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str):
        """
        :param months: 
        :type months: list[int]False
            AMP Type: Int32[]
        :param days: 
        :type days: list[int]False
            AMP Type: Int32[]
        :param hours: 
        :type hours: list[int]False
            AMP Type: Int32[]
        :param minutes: 
        :type minutes: list[int]False
            AMP Type: Int32[]
        :param daysOfMonth: 
        :type daysOfMonth: list[int]False
            AMP Type: Int32[]
        :param description: 
        :type description: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/AddIntervalTrigger", data={
            "months": months, 
            "days": days, 
            "hours": hours, 
            "minutes": minutes, 
            "daysOfMonth": daysOfMonth, 
            "description": description, 
        })

    async def Core_AddIntervalTriggerAsync(self, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str):
        """
        :param months: 
        :type months: list[int]False
            AMP Type: Int32[]
        :param days: 
        :type days: list[int]False
            AMP Type: Int32[]
        :param hours: 
        :type hours: list[int]False
            AMP Type: Int32[]
        :param minutes: 
        :type minutes: list[int]False
            AMP Type: Int32[]
        :param daysOfMonth: 
        :type daysOfMonth: list[int]False
            AMP Type: Int32[]
        :param description: 
        :type description: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/AddIntervalTrigger", data={
            "months": months, 
            "days": days, 
            "hours": hours, 
            "minutes": minutes, 
            "daysOfMonth": daysOfMonth, 
            "description": description, 
        })

    def Core_GetTimeIntervalTrigger(self, Id: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :returns: AMP Type: TimeIntervalTrigger
        """
        return self.APICall(endpoint="Core/GetTimeIntervalTrigger", data={
            "Id": Id, 
        })

    async def Core_GetTimeIntervalTriggerAsync(self, Id: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :returns: AMP Type: TimeIntervalTrigger
        """
        return await self.APICallAsync(endpoint="Core/GetTimeIntervalTrigger", data={
            "Id": Id, 
        })

    def Core_EditIntervalTrigger(self, Id: str, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :param months: 
        :type months: list[int]False
            AMP Type: Int32[]
        :param days: 
        :type days: list[int]False
            AMP Type: Int32[]
        :param hours: 
        :type hours: list[int]False
            AMP Type: Int32[]
        :param minutes: 
        :type minutes: list[int]False
            AMP Type: Int32[]
        :param daysOfMonth: 
        :type daysOfMonth: list[int]False
            AMP Type: Int32[]
        :param description: 
        :type description: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/EditIntervalTrigger", data={
            "Id": Id, 
            "months": months, 
            "days": days, 
            "hours": hours, 
            "minutes": minutes, 
            "daysOfMonth": daysOfMonth, 
            "description": description, 
        })

    async def Core_EditIntervalTriggerAsync(self, Id: str, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :param months: 
        :type months: list[int]False
            AMP Type: Int32[]
        :param days: 
        :type days: list[int]False
            AMP Type: Int32[]
        :param hours: 
        :type hours: list[int]False
            AMP Type: Int32[]
        :param minutes: 
        :type minutes: list[int]False
            AMP Type: Int32[]
        :param daysOfMonth: 
        :type daysOfMonth: list[int]False
            AMP Type: Int32[]
        :param description: 
        :type description: strFalse
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/EditIntervalTrigger", data={
            "Id": Id, 
            "months": months, 
            "days": days, 
            "hours": hours, 
            "minutes": minutes, 
            "daysOfMonth": daysOfMonth, 
            "description": description, 
        })

    def Core_SetTriggerEnabled(self, Id: str, Enabled: bool):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :param Enabled: 
        :type Enabled: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/SetTriggerEnabled", data={
            "Id": Id, 
            "Enabled": Enabled, 
        })

    async def Core_SetTriggerEnabledAsync(self, Id: str, Enabled: bool):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :param Enabled: 
        :type Enabled: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/SetTriggerEnabled", data={
            "Id": Id, 
            "Enabled": Enabled, 
        })

    def Core_AddTask(self, TriggerID: str, MethodID: str, ParameterMapping: dict[str, str]):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param MethodID: 
        :type MethodID: strFalse
            AMP Type: String
        :param ParameterMapping: 
        :type ParameterMapping: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/AddTask", data={
            "TriggerID": TriggerID, 
            "MethodID": MethodID, 
            "ParameterMapping": ParameterMapping, 
        })

    async def Core_AddTaskAsync(self, TriggerID: str, MethodID: str, ParameterMapping: dict[str, str]):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param MethodID: 
        :type MethodID: strFalse
            AMP Type: String
        :param ParameterMapping: 
        :type ParameterMapping: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/AddTask", data={
            "TriggerID": TriggerID, 
            "MethodID": MethodID, 
            "ParameterMapping": ParameterMapping, 
        })

    def Core_EditTask(self, TriggerID: str, TaskID: str, ParameterMapping: dict[str, str]):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param TaskID: 
        :type TaskID: strFalse
            AMP Type: Guid
        :param ParameterMapping: 
        :type ParameterMapping: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/EditTask", data={
            "TriggerID": TriggerID, 
            "TaskID": TaskID, 
            "ParameterMapping": ParameterMapping, 
        })

    async def Core_EditTaskAsync(self, TriggerID: str, TaskID: str, ParameterMapping: dict[str, str]):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param TaskID: 
        :type TaskID: strFalse
            AMP Type: Guid
        :param ParameterMapping: 
        :type ParameterMapping: dict[str, str]False
            AMP Type: Dictionary<String, String>
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/EditTask", data={
            "TriggerID": TriggerID, 
            "TaskID": TaskID, 
            "ParameterMapping": ParameterMapping, 
        })

    def Core_ChangeTaskOrder(self, TriggerID: str, TaskID: str, NewOrder: int):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param TaskID: 
        :type TaskID: strFalse
            AMP Type: Guid
        :param NewOrder: 
        :type NewOrder: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/ChangeTaskOrder", data={
            "TriggerID": TriggerID, 
            "TaskID": TaskID, 
            "NewOrder": NewOrder, 
        })

    async def Core_ChangeTaskOrderAsync(self, TriggerID: str, TaskID: str, NewOrder: int):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param TaskID: 
        :type TaskID: strFalse
            AMP Type: Guid
        :param NewOrder: 
        :type NewOrder: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/ChangeTaskOrder", data={
            "TriggerID": TriggerID, 
            "TaskID": TaskID, 
            "NewOrder": NewOrder, 
        })

    def Core_DeleteTask(self, TriggerID: str, TaskID: str):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param TaskID: 
        :type TaskID: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/DeleteTask", data={
            "TriggerID": TriggerID, 
            "TaskID": TaskID, 
        })

    async def Core_DeleteTaskAsync(self, TriggerID: str, TaskID: str):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :param TaskID: 
        :type TaskID: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/DeleteTask", data={
            "TriggerID": TriggerID, 
            "TaskID": TaskID, 
        })

    def Core_DeleteTrigger(self, TriggerID: str):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/DeleteTrigger", data={
            "TriggerID": TriggerID, 
        })

    async def Core_DeleteTriggerAsync(self, TriggerID: str):
        """
        :param TriggerID: 
        :type TriggerID: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/DeleteTrigger", data={
            "TriggerID": TriggerID, 
        })

    def Core_GetActiveAMPSessions(self):
        """
        :returns: AMP Type: IEnumerable<WebSessionSummary>
        :rtype: list
        """
        return self.APICall(endpoint="Core/GetActiveAMPSessions")

    async def Core_GetActiveAMPSessionsAsync(self):
        """
        :returns: AMP Type: IEnumerable<WebSessionSummary>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="Core/GetActiveAMPSessions")

    def Core_EndUserSession(self, Id: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/EndUserSession", data={
            "Id": Id, 
        })

    async def Core_EndUserSessionAsync(self, Id: str):
        """
        :param Id: 
        :type Id: strFalse
            AMP Type: Guid
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/EndUserSession", data={
            "Id": Id, 
        })

    def Core_GetAMPUsersSummary(self):
        """
        :returns: AMP Type: Task<IEnumerable<UserInfoSummary>>
        """
        return self.APICall(endpoint="Core/GetAMPUsersSummary")

    async def Core_GetAMPUsersSummaryAsync(self):
        """
        :returns: AMP Type: Task<IEnumerable<UserInfoSummary>>
        """
        return await self.APICallAsync(endpoint="Core/GetAMPUsersSummary")

    def Core_GetAMPUserInfo(self, Username: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :returns: AMP Type: Task<UserInfo>
        """
        return self.APICall(endpoint="Core/GetAMPUserInfo", data={
            "Username": Username, 
        })

    async def Core_GetAMPUserInfoAsync(self, Username: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :returns: AMP Type: Task<UserInfo>
        """
        return await self.APICallAsync(endpoint="Core/GetAMPUserInfo", data={
            "Username": Username, 
        })

    def Core_GetAllAMPUserInfo(self):
        """
        :returns: AMP Type: Task<IEnumerable<UserInfo>>
        """
        return self.APICall(endpoint="Core/GetAllAMPUserInfo")

    async def Core_GetAllAMPUserInfoAsync(self):
        """
        :returns: AMP Type: Task<IEnumerable<UserInfo>>
        """
        return await self.APICallAsync(endpoint="Core/GetAllAMPUserInfo")

    def Core_SetAMPUserRoleMembership(self, UserId: str, RoleId: str, IsMember: bool):
        """
        :param UserId: 
        :type UserId: strFalse
            AMP Type: Guid
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :param IsMember: 
        :type IsMember: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/SetAMPUserRoleMembership", data={
            "UserId": UserId, 
            "RoleId": RoleId, 
            "IsMember": IsMember, 
        })

    async def Core_SetAMPUserRoleMembershipAsync(self, UserId: str, RoleId: str, IsMember: bool):
        """
        :param UserId: 
        :type UserId: strFalse
            AMP Type: Guid
        :param RoleId: 
        :type RoleId: strFalse
            AMP Type: Guid
        :param IsMember: 
        :type IsMember: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/SetAMPUserRoleMembership", data={
            "UserId": UserId, 
            "RoleId": RoleId, 
            "IsMember": IsMember, 
        })

    def Core_GetPermissionsSpec(self):
        """
        :returns: AMP Type: IList<IPermissionsTreeNode>
        :rtype: list
        """
        return self.APICall(endpoint="Core/GetPermissionsSpec")

    async def Core_GetPermissionsSpecAsync(self):
        """
        :returns: AMP Type: IList<IPermissionsTreeNode>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="Core/GetPermissionsSpec")

    def Core_CreateUser(self, Username: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult<Guid>>
        """
        return self.APICall(endpoint="Core/CreateUser", data={
            "Username": Username, 
        })

    async def Core_CreateUserAsync(self, Username: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult<Guid>>
        """
        return await self.APICallAsync(endpoint="Core/CreateUser", data={
            "Username": Username, 
        })

    def Core_DeleteUser(self, Username: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/DeleteUser", data={
            "Username": Username, 
        })

    async def Core_DeleteUserAsync(self, Username: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/DeleteUser", data={
            "Username": Username, 
        })

    def Core_UpdateUserInfo(self, Username: str, Disabled: bool, PasswordExpires: bool, CannotChangePassword: bool, MustChangePassword: bool, EmailAddress: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param Disabled: 
        :type Disabled: boolFalse
            AMP Type: Boolean
        :param PasswordExpires: 
        :type PasswordExpires: boolFalse
            AMP Type: Boolean
        :param CannotChangePassword: 
        :type CannotChangePassword: boolFalse
            AMP Type: Boolean
        :param MustChangePassword: 
        :type MustChangePassword: boolFalse
            AMP Type: Boolean
        :param EmailAddress: 
        :type EmailAddress: strTrue
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/UpdateUserInfo", data={
            "Username": Username, 
            "Disabled": Disabled, 
            "PasswordExpires": PasswordExpires, 
            "CannotChangePassword": CannotChangePassword, 
            "MustChangePassword": MustChangePassword, 
            "EmailAddress": EmailAddress, 
        })

    async def Core_UpdateUserInfoAsync(self, Username: str, Disabled: bool, PasswordExpires: bool, CannotChangePassword: bool, MustChangePassword: bool, EmailAddress: str):
        """
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param Disabled: 
        :type Disabled: boolFalse
            AMP Type: Boolean
        :param PasswordExpires: 
        :type PasswordExpires: boolFalse
            AMP Type: Boolean
        :param CannotChangePassword: 
        :type CannotChangePassword: boolFalse
            AMP Type: Boolean
        :param MustChangePassword: 
        :type MustChangePassword: boolFalse
            AMP Type: Boolean
        :param EmailAddress: 
        :type EmailAddress: strTrue
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/UpdateUserInfo", data={
            "Username": Username, 
            "Disabled": Disabled, 
            "PasswordExpires": PasswordExpires, 
            "CannotChangePassword": CannotChangePassword, 
            "MustChangePassword": MustChangePassword, 
            "EmailAddress": EmailAddress, 
        })

    def Core_GetWebauthnChallenge(self):
        """
        :returns: AMP Type: ActionResult<String>
        """
        return self.APICall(endpoint="Core/GetWebauthnChallenge")

    async def Core_GetWebauthnChallengeAsync(self):
        """
        :returns: AMP Type: ActionResult<String>
        """
        return await self.APICallAsync(endpoint="Core/GetWebauthnChallenge")

    def Core_GetWebauthnCredentialIDs(self, username: str):
        """
        :param username: 
        :type username: strFalse
            AMP Type: String
        :returns: AMP Type: WebauthnLoginInfo
        """
        return self.APICall(endpoint="Core/GetWebauthnCredentialIDs", data={
            "username": username, 
        })

    async def Core_GetWebauthnCredentialIDsAsync(self, username: str):
        """
        :param username: 
        :type username: strFalse
            AMP Type: String
        :returns: AMP Type: WebauthnLoginInfo
        """
        return await self.APICallAsync(endpoint="Core/GetWebauthnCredentialIDs", data={
            "username": username, 
        })

    def Core_WebauthnRegister(self, attestationObject: str, clientDataJSON: str, description: str):
        """
        :param attestationObject: 
        :type attestationObject: strFalse
            AMP Type: String
        :param clientDataJSON: 
        :type clientDataJSON: strFalse
            AMP Type: String
        :param description: 
        :type description: strTrue
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/WebauthnRegister", data={
            "attestationObject": attestationObject, 
            "clientDataJSON": clientDataJSON, 
            "description": description, 
        })

    async def Core_WebauthnRegisterAsync(self, attestationObject: str, clientDataJSON: str, description: str):
        """
        :param attestationObject: 
        :type attestationObject: strFalse
            AMP Type: String
        :param clientDataJSON: 
        :type clientDataJSON: strFalse
            AMP Type: String
        :param description: 
        :type description: strTrue
            AMP Type: String
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/WebauthnRegister", data={
            "attestationObject": attestationObject, 
            "clientDataJSON": clientDataJSON, 
            "description": description, 
        })

    def Core_GetWebauthnCredentialSummaries(self):
        """
        :returns: AMP Type: IEnumerable<WebauthnCredentialSummary>
        :rtype: list
        """
        return self.APICall(endpoint="Core/GetWebauthnCredentialSummaries")

    async def Core_GetWebauthnCredentialSummariesAsync(self):
        """
        :returns: AMP Type: IEnumerable<WebauthnCredentialSummary>
        :rtype: list
        """
        return await self.APICallAsync(endpoint="Core/GetWebauthnCredentialSummaries")

    def Core_RevokeWebauthnCredential(self, ID: int):
        """
        :param ID: 
        :type ID: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/RevokeWebauthnCredential", data={
            "ID": ID, 
        })

    async def Core_RevokeWebauthnCredentialAsync(self, ID: int):
        """
        :param ID: 
        :type ID: intFalse
            AMP Type: Int32
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/RevokeWebauthnCredential", data={
            "ID": ID, 
        })

    def Core_UpdateAccountInfo(self, EmailAddress: str, TwoFactorPIN: str):
        """
        :param EmailAddress: 
        :type EmailAddress: strFalse
            AMP Type: String
        :param TwoFactorPIN: 
        :type TwoFactorPIN: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/UpdateAccountInfo", data={
            "EmailAddress": EmailAddress, 
            "TwoFactorPIN": TwoFactorPIN, 
        })

    async def Core_UpdateAccountInfoAsync(self, EmailAddress: str, TwoFactorPIN: str):
        """
        :param EmailAddress: 
        :type EmailAddress: strFalse
            AMP Type: String
        :param TwoFactorPIN: 
        :type TwoFactorPIN: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/UpdateAccountInfo", data={
            "EmailAddress": EmailAddress, 
            "TwoFactorPIN": TwoFactorPIN, 
        })

    def Core_EnableTwoFactor(self, Username: str, Password: str):
        """Sets up two-factor authentication for the given user. ConfirmTwoFactorSetup must be invoked to complete setup.
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param Password: 
        :type Password: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult<TwoFactorSetupInfo>>
        """
        return self.APICall(endpoint="Core/EnableTwoFactor", data={
            "Username": Username, 
            "Password": Password, 
        })

    async def Core_EnableTwoFactorAsync(self, Username: str, Password: str):
        """Sets up two-factor authentication for the given user. ConfirmTwoFactorSetup must be invoked to complete setup.
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param Password: 
        :type Password: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult<TwoFactorSetupInfo>>
        """
        return await self.APICallAsync(endpoint="Core/EnableTwoFactor", data={
            "Username": Username, 
            "Password": Password, 
        })

    def Core_ConfirmTwoFactorSetup(self, Username: str, TwoFactorCode: str):
        """Completes two-factor setup by supplying a valid two factor code based on the secret provided by EnableTwoFactor
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param TwoFactorCode: 
        :type TwoFactorCode: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/ConfirmTwoFactorSetup", data={
            "Username": Username, 
            "TwoFactorCode": TwoFactorCode, 
        })

    async def Core_ConfirmTwoFactorSetupAsync(self, Username: str, TwoFactorCode: str):
        """Completes two-factor setup by supplying a valid two factor code based on the secret provided by EnableTwoFactor
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param TwoFactorCode: 
        :type TwoFactorCode: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/ConfirmTwoFactorSetup", data={
            "Username": Username, 
            "TwoFactorCode": TwoFactorCode, 
        })

    def Core_DisableTwoFactor(self, Password: str, TwoFactorCode: str):
        """
        :param Password: 
        :type Password: strFalse
            AMP Type: String
        :param TwoFactorCode: 
        :type TwoFactorCode: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/DisableTwoFactor", data={
            "Password": Password, 
            "TwoFactorCode": TwoFactorCode, 
        })

    async def Core_DisableTwoFactorAsync(self, Password: str, TwoFactorCode: str):
        """
        :param Password: 
        :type Password: strFalse
            AMP Type: String
        :param TwoFactorCode: 
        :type TwoFactorCode: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/DisableTwoFactor", data={
            "Password": Password, 
            "TwoFactorCode": TwoFactorCode, 
        })

    def Core_ResetUserPassword(self, Username: str, NewPassword: str):
        """For administrative users to alter the password of another user
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param NewPassword: 
        :type NewPassword: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/ResetUserPassword", data={
            "Username": Username, 
            "NewPassword": NewPassword, 
        })

    async def Core_ResetUserPasswordAsync(self, Username: str, NewPassword: str):
        """For administrative users to alter the password of another user
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param NewPassword: 
        :type NewPassword: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/ResetUserPassword", data={
            "Username": Username, 
            "NewPassword": NewPassword, 
        })

    def Core_DeleteInstanceUsers(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/DeleteInstanceUsers", data={
            "InstanceId": InstanceId, 
        })

    async def Core_DeleteInstanceUsersAsync(self, InstanceId: str):
        """
        :param InstanceId: 
        :type InstanceId: strFalse
            AMP Type: Guid
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/DeleteInstanceUsers", data={
            "InstanceId": InstanceId, 
        })

    def Core_ChangeUserPassword(self, Username: str, OldPassword: str, NewPassword: str, TwoFactorPIN: str):
        """For a user to change their own password, requires knowing the old password
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param OldPassword: 
        :type OldPassword: strFalse
            AMP Type: String
        :param NewPassword: 
        :type NewPassword: strFalse
            AMP Type: String
        :param TwoFactorPIN: 
        :type TwoFactorPIN: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return self.APICall(endpoint="Core/ChangeUserPassword", data={
            "Username": Username, 
            "OldPassword": OldPassword, 
            "NewPassword": NewPassword, 
            "TwoFactorPIN": TwoFactorPIN, 
        })

    async def Core_ChangeUserPasswordAsync(self, Username: str, OldPassword: str, NewPassword: str, TwoFactorPIN: str):
        """For a user to change their own password, requires knowing the old password
            
        :param Username: 
        :type Username: strFalse
            AMP Type: String
        :param OldPassword: 
        :type OldPassword: strFalse
            AMP Type: String
        :param NewPassword: 
        :type NewPassword: strFalse
            AMP Type: String
        :param TwoFactorPIN: 
        :type TwoFactorPIN: strFalse
            AMP Type: String
        :returns: AMP Type: Task<ActionResult>
        """
        return await self.APICallAsync(endpoint="Core/ChangeUserPassword", data={
            "Username": Username, 
            "OldPassword": OldPassword, 
            "NewPassword": NewPassword, 
            "TwoFactorPIN": TwoFactorPIN, 
        })

    def Core_GetUpdates(self):
        """Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
            
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return self.APICall(endpoint="Core/GetUpdates")

    async def Core_GetUpdatesAsync(self):
        """Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
            
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="Core/GetUpdates")

    def Core_GetNewGuid(self):
        """
        :returns: AMP Type: Guid
        :rtype: str
        """
        return self.APICall(endpoint="Core/GetNewGuid")

    async def Core_GetNewGuidAsync(self):
        """
        :returns: AMP Type: Guid
        :rtype: str
        """
        return await self.APICallAsync(endpoint="Core/GetNewGuid")

    def Core_GetUserList(self):
        """Returns a list of in-application users
            
        :returns: AMP Type: Dictionary<String, String>
        :rtype: dict[str, str]
        """
        return self.APICall(endpoint="Core/GetUserList")

    async def Core_GetUserListAsync(self):
        """Returns a list of in-application users
            
        :returns: AMP Type: Dictionary<String, String>
        :rtype: dict[str, str]
        """
        return await self.APICallAsync(endpoint="Core/GetUserList")

    def Core_CurrentSessionHasPermission(self, PermissionNode: str):
        """
        :param PermissionNode: 
        :type PermissionNode: strFalse
            AMP Type: String
        :returns: AMP Type: Boolean
        :rtype: bool
        """
        return self.APICall(endpoint="Core/CurrentSessionHasPermission", data={
            "PermissionNode": PermissionNode, 
        })

    async def Core_CurrentSessionHasPermissionAsync(self, PermissionNode: str):
        """
        :param PermissionNode: 
        :type PermissionNode: strFalse
            AMP Type: String
        :returns: AMP Type: Boolean
        :rtype: bool
        """
        return await self.APICallAsync(endpoint="Core/CurrentSessionHasPermission", data={
            "PermissionNode": PermissionNode, 
        })

    def Core_GetTasks(self):
        """
        :returns: AMP Type: IEnumerable<RunningTask>
        """
        return self.APICall(endpoint="Core/GetTasks")

    async def Core_GetTasksAsync(self):
        """
        :returns: AMP Type: IEnumerable<RunningTask>
        """
        return await self.APICallAsync(endpoint="Core/GetTasks")

    def Core_GetStatus(self):
        """
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return self.APICall(endpoint="Core/GetStatus")

    async def Core_GetStatusAsync(self):
        """
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="Core/GetStatus")

    def Core_CancelTask(self, TaskId: str):
        """
        :param TaskId: 
        :type TaskId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/CancelTask", data={
            "TaskId": TaskId, 
        })

    async def Core_CancelTaskAsync(self, TaskId: str):
        """
        :param TaskId: 
        :type TaskId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/CancelTask", data={
            "TaskId": TaskId, 
        })

    def Core_DismissTask(self, TaskId: str):
        """
        :param TaskId: 
        :type TaskId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/DismissTask", data={
            "TaskId": TaskId, 
        })

    async def Core_DismissTaskAsync(self, TaskId: str):
        """
        :param TaskId: 
        :type TaskId: strFalse
            AMP Type: Guid
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/DismissTask", data={
            "TaskId": TaskId, 
        })

    def Core_DismissAllTasks(self):
        """
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/DismissAllTasks")

    async def Core_DismissAllTasksAsync(self):
        """
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/DismissAllTasks")

    def Core_GetUserInfo(self, UID: str):
        """Provides information about a given in-application user (as opposed to AMP system users)
            
        :param UID: 
        :type UID: strFalse
            AMP Type: String
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return self.APICall(endpoint="Core/GetUserInfo", data={
            "UID": UID, 
        })

    async def Core_GetUserInfoAsync(self, UID: str):
        """Provides information about a given in-application user (as opposed to AMP system users)
            
        :param UID: 
        :type UID: strFalse
            AMP Type: String
        :returns: AMP Type: JObject
        :rtype: dict
        """
        return await self.APICallAsync(endpoint="Core/GetUserInfo", data={
            "UID": UID, 
        })

    def Core_Start(self):
        """
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/Start")

    async def Core_StartAsync(self):
        """
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/Start")

    def Core_Suspend(self):
        """Prevents the current instance from being started, and stops it if it's currently running.
            
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/Suspend")

    async def Core_SuspendAsync(self):
        """Prevents the current instance from being started, and stops it if it's currently running.
            
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/Suspend")

    def Core_Resume(self):
        """Allows the service to be re-started after previously being suspended.
            
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/Resume")

    async def Core_ResumeAsync(self):
        """Allows the service to be re-started after previously being suspended.
            
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/Resume")

    def Core_Stop(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/Stop")

    async def Core_StopAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/Stop")

    def Core_Restart(self):
        """
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/Restart")

    async def Core_RestartAsync(self):
        """
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/Restart")

    def Core_Kill(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/Kill")

    async def Core_KillAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/Kill")

    def Core_Sleep(self):
        """
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/Sleep")

    async def Core_SleepAsync(self):
        """
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/Sleep")

    def Core_UpdateApplication(self):
        """
        :returns: AMP Type: ActionResult
        """
        return self.APICall(endpoint="Core/UpdateApplication")

    async def Core_UpdateApplicationAsync(self):
        """
        :returns: AMP Type: ActionResult
        """
        return await self.APICallAsync(endpoint="Core/UpdateApplication")

    def Core_AcknowledgeAMPUpdate(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/AcknowledgeAMPUpdate")

    async def Core_AcknowledgeAMPUpdateAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/AcknowledgeAMPUpdate")

    def Core_GetModuleInfo(self):
        """
        :returns: AMP Type: ModuleInfo
        """
        return self.APICall(endpoint="Core/GetModuleInfo")

    async def Core_GetModuleInfoAsync(self):
        """
        :returns: AMP Type: ModuleInfo
        """
        return await self.APICallAsync(endpoint="Core/GetModuleInfo")

    def Core_GetAPISpec(self):
        """
        :returns: AMP Type: Dictionary<String, Dictionary<String, MethodInfoSummary>>
        :rtype: dict[str, dict]
        """
        return self.APICall(endpoint="Core/GetAPISpec")

    async def Core_GetAPISpecAsync(self):
        """
        :returns: AMP Type: Dictionary<String, Dictionary<String, MethodInfoSummary>>
        :rtype: dict[str, dict]
        """
        return await self.APICallAsync(endpoint="Core/GetAPISpec")

    def Core_GetUserActionsSpec(self):
        """
        :returns: AMP Type: Object
        """
        return self.APICall(endpoint="Core/GetUserActionsSpec")

    async def Core_GetUserActionsSpecAsync(self):
        """
        :returns: AMP Type: Object
        """
        return await self.APICallAsync(endpoint="Core/GetUserActionsSpec")

    def Core_Login(self, username: str, password: str, token: str, rememberMe: bool):
        """
        :param username: 
        :type username: strFalse
            AMP Type: String
        :param password: 
        :type password: strFalse
            AMP Type: String
        :param token: 
        :type token: strFalse
            AMP Type: String
        :param rememberMe: 
        :type rememberMe: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<JObject>
        """
        return self.APICall(endpoint="Core/Login", data={
            "username": username, 
            "password": password, 
            "token": token, 
            "rememberMe": rememberMe, 
        })

    async def Core_LoginAsync(self, username: str, password: str, token: str, rememberMe: bool):
        """
        :param username: 
        :type username: strFalse
            AMP Type: String
        :param password: 
        :type password: strFalse
            AMP Type: String
        :param token: 
        :type token: strFalse
            AMP Type: String
        :param rememberMe: 
        :type rememberMe: boolFalse
            AMP Type: Boolean
        :returns: AMP Type: Task<JObject>
        """
        return await self.APICallAsync(endpoint="Core/Login", data={
            "username": username, 
            "password": password, 
            "token": token, 
            "rememberMe": rememberMe, 
        })

    def Core_GetRemoteLoginToken(self, Description: str, IsTemporary: bool):
        """
        :param Description: 
        :type Description: strTrue
            AMP Type: String
        :param IsTemporary: 
        :type IsTemporary: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: Task<String>
        """
        return self.APICall(endpoint="Core/GetRemoteLoginToken", data={
            "Description": Description, 
            "IsTemporary": IsTemporary, 
        })

    async def Core_GetRemoteLoginTokenAsync(self, Description: str, IsTemporary: bool):
        """
        :param Description: 
        :type Description: strTrue
            AMP Type: String
        :param IsTemporary: 
        :type IsTemporary: boolTrue
            AMP Type: Boolean
        :returns: AMP Type: Task<String>
        """
        return await self.APICallAsync(endpoint="Core/GetRemoteLoginToken", data={
            "Description": Description, 
            "IsTemporary": IsTemporary, 
        })

    def Core_SendConsoleMessage(self, message: str):
        """
        :param message: 
        :type message: strFalse
            AMP Type: String
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/SendConsoleMessage", data={
            "message": message, 
        })

    async def Core_SendConsoleMessageAsync(self, message: str):
        """
        :param message: 
        :type message: strFalse
            AMP Type: String
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/SendConsoleMessage", data={
            "message": message, 
        })

    def Core_UpdateAMPInstance(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/UpdateAMPInstance")

    async def Core_UpdateAMPInstanceAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/UpdateAMPInstance")

    def Core_GetUpdateInfo(self):
        """
        :returns: AMP Type: UpdateInfo
        """
        return self.APICall(endpoint="Core/GetUpdateInfo")

    async def Core_GetUpdateInfoAsync(self):
        """
        :returns: AMP Type: UpdateInfo
        """
        return await self.APICallAsync(endpoint="Core/GetUpdateInfo")

    def Core_Logout(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/Logout")

    async def Core_LogoutAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/Logout")

    def Core_RestartAMP(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/RestartAMP")

    async def Core_RestartAMPAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/RestartAMP")

    def Core_UpgradeAMP(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/UpgradeAMP")

    async def Core_UpgradeAMPAsync(self):
        """
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/UpgradeAMP")

    def Core_GetDiagnosticsInfo(self):
        """
        :returns: AMP Type: Dictionary<String, String>
        :rtype: dict[str, str]
        """
        return self.APICall(endpoint="Core/GetDiagnosticsInfo")

    async def Core_GetDiagnosticsInfoAsync(self):
        """
        :returns: AMP Type: Dictionary<String, String>
        :rtype: dict[str, str]
        """
        return await self.APICallAsync(endpoint="Core/GetDiagnosticsInfo")

    def Core_GetWebserverMetrics(self):
        """
        :returns: AMP Type: Object
        """
        return self.APICall(endpoint="Core/GetWebserverMetrics")

    async def Core_GetWebserverMetricsAsync(self):
        """
        :returns: AMP Type: Object
        """
        return await self.APICallAsync(endpoint="Core/GetWebserverMetrics")

    def Core_CreateTestTask(self):
        """DEV: Creates a non-ending task with 50% progress for testing purposes
            
        :returns: AMP Type: Void
        :rtype: None
        """
        return self.APICall(endpoint="Core/CreateTestTask")

    async def Core_CreateTestTaskAsync(self):
        """DEV: Creates a non-ending task with 50% progress for testing purposes
            
        :returns: AMP Type: Void
        :rtype: None
        """
        return await self.APICallAsync(endpoint="Core/CreateTestTask")

    def Core_AsyncTest(self):
        """DEV: Async test method
            
        :returns: AMP Type: Task<String>
        """
        return self.APICall(endpoint="Core/AsyncTest")

    async def Core_AsyncTestAsync(self):
        """DEV: Async test method
            
        :returns: AMP Type: Task<String>
        """
        return await self.APICallAsync(endpoint="Core/AsyncTest")

AMPAPIHandlerType = TypeVar("AMPAPIHandlerType", bound="AMPAPIHandler")

class AMPAPIHandler(AMPAPI):
    """Class to make handling the AMP API easier, without altering the generated code"""
    def __init__(self, baseUri: str, username: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        """Constructor for AMPAPIHandler
        :param baseUri: The base URI of the AMP instance
        :type baseUri: str
        :param username: The username to log in with
        :type username: str
        :param password: The password to log in with
        :type password: str
        :value password: ""
        :param rememberMeToken: The remember me token to log in with
        :type rememberMeToken: str
        :value rememberMeToken: ""
        :param sessionId: The session ID to log in with
        :type sessionId: str
        :value sessionId: ""
        :returns: None
        """
        super().__init__(baseUri=baseUri)
        if self.baseUri[-1] != "/": self.baseUri = self.baseUri + "/"
        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    def APICall(self, endpoint: str, data: dict = {}, retry: bool = False) -> dict:
        """Overridden APICall method to automatically relog if the call fails
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :param retry: Wether the call is a retry or not
        :type retry: bool
        :value retry: False
        :returns: dict with the result of the API call
        :rtype: dict
        """
        try:
            headers = {'Accept': 'text/javascript',}
            session = {"SESSIONID": self.sessionId}
            data_added = dict(session, **data)

            data_json = json.dumps(data_added)

            res = requests.post(
                url=f"{self.dataSource}/{endpoint}",
                headers=headers,
                data=data_json
            )
            res_json = json.loads(res.content)

            return res_json
        except Exception as e:
            # If retry is set to true, raise the exception
            if retry:
                raise e

            # Relog and retry the API call
            loginResult = self.APICall("Core/Login", {
                "username": self.username,
                "password": self.password,
                "token": self.token,
                "rememberMe": False
            })
            if "success" in loginResult.keys() and loginResult["success"]:
                self.APICall(endpoint, data, 1)

    async def APICallAsync(self, endpoint: str, data: dict = {}, retry: bool = False) -> dict:
        """Overridden APICall method to automatically relog if the call fails
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :param retry: Wether the call is a retry or not
        :type retry: bool
        :value retry: False
        :returns: dict with the result of the API call
        :rtype: dict
        """
        try:
            headers = {'accept': 'text/javascript',}
            session = {"SESSIONID": self.sessionId}
            data_added = dict(session, **data)

            data_json = json.dumps(data_added)

            async with ClientSession() as session:
                async with session.post(url=f'{self.dataSource}/{endpoint}', headers=headers, data=data_json) as post:
                    response = await post.json()
                    post.close()

            return response
        except Exception as e:
            # If retry is set to true, raise the exception
            if retry:
                raise e

            # Relog and retry the API call
            loginResult = self.APICallAsync("Core/Login", {
                "username": self.username,
                "password": self.password,
                "token": self.token,
                "rememberMe": False
            })
            if "success" in loginResult.keys() and loginResult["success"]:
                self.APICallAsync(endpoint, data, 1)

    def Login(self) -> dict:
        """Method to make the login process easier
        :returns: dict with the login result
        :rtype: dict
        """
        loginResult = self.APICall(endpoint=f"Core/Login", data={
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": False
        })
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    async def LoginAsync(self) -> dict:
        """Method to make the login process easier
        :returns: dict with the login result
        :rtype: dict
        """
        loginResult = await self.APICallAsync(endpoint=f"Core/Login", data={
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": False
        })
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    def InstanceLogin(self, instance_id: str) -> AMPAPIHandlerType | None:
        """Method to build another AMPAPIHandler for the specified instance
        :param instance_id: The instance ID to log into
        :type instance_id: str
        :returns: A new AMPAPIHandler for the specified instance
        :rtype: AMPAPIHandler | None
        """
        loginResult = self.APICall(endpoint=f"ADSModule/Servers/{instance_id}/API/Core/Login", data={
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": True
        })

        if loginResult != None and "success" in loginResult.keys() and loginResult["success"] == True:
            return AMPAPIHandler(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                password="",
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )
        else:
            return None

    async def InstanceLoginAsync(self, instance_id: str) -> AMPAPIHandlerType | None:
        """Method to build another AMPAPIHandler for the specified instance
        :param instance_id: The instance ID to log into
        :type instance_id: str
        :returns: A new AMPAPIHandler for the specified instance
        :rtype: AMPAPIHandler | None
        """
        loginResult = await self.APICallAsync(endpoint=f"ADSModule/Servers/{instance_id}/API/Core/Login", data={
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": True
        })

        if loginResult != None and "success" in loginResult.keys() and loginResult["success"] == True:
            return AMPAPIHandler(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                password="",
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )
        else:
            return None
