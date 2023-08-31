#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class ADSModule(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the ADSModule class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AddDatastore(self, newDatastore: Any) -> Any:
        """
        Name Description Optional
        :param newDatastore: {Any}  False
        :returns: Any
        """
        return self.api_call("ADSModule/AddDatastore", { 
            "newDatastore": newDatastore,
        })

    async def AddDatastoreAsync(self, newDatastore: Any) -> Any:
        """
        Name Description Optional
        :param newDatastore: {Any}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/AddDatastore", { 
            "newDatastore": newDatastore,
        })

    def ApplyInstanceConfiguration(self, InstanceID: str, Args: dict[str, str], RebuildConfiguration: bool) -> Any:
        """
        Name Description Optional
        :param InstanceID: {str}  False
        :param Args: {dict[str, str]}  False
        :param RebuildConfiguration: {bool}  True
        :returns: Any
        """
        return self.api_call("ADSModule/ApplyInstanceConfiguration", { 
            "InstanceID": InstanceID,
            "Args": Args,
            "RebuildConfiguration": RebuildConfiguration,
        })

    async def ApplyInstanceConfigurationAsync(self, InstanceID: str, Args: dict[str, str], RebuildConfiguration: bool) -> Any:
        """
        Name Description Optional
        :param InstanceID: {str}  False
        :param Args: {dict[str, str]}  False
        :param RebuildConfiguration: {bool}  True
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ApplyInstanceConfiguration", { 
            "InstanceID": InstanceID,
            "Args": Args,
            "RebuildConfiguration": RebuildConfiguration,
        })

    def ApplyTemplate(self, InstanceID: str, TemplateID: int, NewFriendlyName: str, Secret: str, RestartIfPreviouslyRunning: bool) -> Any:
        """
        Name Description Optional
        :param InstanceID: {str}  False
        :param TemplateID: {int}  False
        :param NewFriendlyName: {str}  True
        :param Secret: {str}  True
        :param RestartIfPreviouslyRunning: {bool}  True
        :returns: Any
        """
        return self.api_call("ADSModule/ApplyTemplate", { 
            "InstanceID": InstanceID,
            "TemplateID": TemplateID,
            "NewFriendlyName": NewFriendlyName,
            "Secret": Secret,
            "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning,
        })

    async def ApplyTemplateAsync(self, InstanceID: str, TemplateID: int, NewFriendlyName: str, Secret: str, RestartIfPreviouslyRunning: bool) -> Any:
        """
        Name Description Optional
        :param InstanceID: {str}  False
        :param TemplateID: {int}  False
        :param NewFriendlyName: {str}  True
        :param Secret: {str}  True
        :param RestartIfPreviouslyRunning: {bool}  True
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ApplyTemplate", { 
            "InstanceID": InstanceID,
            "TemplateID": TemplateID,
            "NewFriendlyName": NewFriendlyName,
            "Secret": Secret,
            "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning,
        })

    def AttachADS(self, Friendly: str, IsHTTPS: bool, Host: str, Port: int, InstanceID: str) -> Any:
        """
        Name Description Optional
        :param Friendly: {str}  False
        :param IsHTTPS: {bool}  False
        :param Host: {str}  False
        :param Port: {int}  False
        :param InstanceID: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/AttachADS", { 
            "Friendly": Friendly,
            "IsHTTPS": IsHTTPS,
            "Host": Host,
            "Port": Port,
            "InstanceID": InstanceID,
        })

    async def AttachADSAsync(self, Friendly: str, IsHTTPS: bool, Host: str, Port: int, InstanceID: str) -> Any:
        """
        Name Description Optional
        :param Friendly: {str}  False
        :param IsHTTPS: {bool}  False
        :param Host: {str}  False
        :param Port: {int}  False
        :param InstanceID: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/AttachADS", { 
            "Friendly": Friendly,
            "IsHTTPS": IsHTTPS,
            "Host": Host,
            "Port": Port,
            "InstanceID": InstanceID,
        })

    def CloneTemplate(self, Id: int, NewName: str) -> Any:
        """
        Name Description Optional
        :param Id: {int}  False
        :param NewName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/CloneTemplate", { 
            "Id": Id,
            "NewName": NewName,
        })

    async def CloneTemplateAsync(self, Id: int, NewName: str) -> Any:
        """
        Name Description Optional
        :param Id: {int}  False
        :param NewName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/CloneTemplate", { 
            "Id": Id,
            "NewName": NewName,
        })

    def ConvertToManaged(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/ConvertToManaged", { 
            "InstanceName": InstanceName,
        })

    async def ConvertToManagedAsync(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ConvertToManaged", { 
            "InstanceName": InstanceName,
        })

    def CreateDeploymentTemplate(self, Name: str) -> Any:
        """
        Name Description Optional
        :param Name: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/CreateDeploymentTemplate", { 
            "Name": Name,
        })

    async def CreateDeploymentTemplateAsync(self, Name: str) -> Any:
        """
        Name Description Optional
        :param Name: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/CreateDeploymentTemplate", { 
            "Name": Name,
        })

    def CreateInstance(self, TargetADSInstance: str, NewInstanceId: str, Module: str, InstanceName: str, FriendlyName: str, IPBinding: str, PortNumber: int, AdminUsername: str, AdminPassword: str, ProvisionSettings: dict[str, str], AutoConfigure: bool, PostCreate: Any, StartOnBoot: bool, DisplayImageSource: str, TargetDatastore: int) -> Any:
        """
        Name Description Optional
        :param TargetADSInstance: {str}  False
        :param NewInstanceId: {str}  False
        :param Module: {str}  False
        :param InstanceName: {str}  False
        :param FriendlyName: {str}  False
        :param IPBinding: {str}  False
        :param PortNumber: {int}  False
        :param AdminUsername: {str}  False
        :param AdminPassword: {str}  False
        :param ProvisionSettings: {dict[str, str]}  False
        :param AutoConfigure: {bool} When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values. True
        :param PostCreate: {Any}  True
        :param StartOnBoot: {bool}  True
        :param DisplayImageSource: {str}  True
        :param TargetDatastore: {int}  True
        :returns: Any
        """
        return self.api_call("ADSModule/CreateInstance", { 
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

    async def CreateInstanceAsync(self, TargetADSInstance: str, NewInstanceId: str, Module: str, InstanceName: str, FriendlyName: str, IPBinding: str, PortNumber: int, AdminUsername: str, AdminPassword: str, ProvisionSettings: dict[str, str], AutoConfigure: bool, PostCreate: Any, StartOnBoot: bool, DisplayImageSource: str, TargetDatastore: int) -> Any:
        """
        Name Description Optional
        :param TargetADSInstance: {str}  False
        :param NewInstanceId: {str}  False
        :param Module: {str}  False
        :param InstanceName: {str}  False
        :param FriendlyName: {str}  False
        :param IPBinding: {str}  False
        :param PortNumber: {int}  False
        :param AdminUsername: {str}  False
        :param AdminPassword: {str}  False
        :param ProvisionSettings: {dict[str, str]}  False
        :param AutoConfigure: {bool} When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values. True
        :param PostCreate: {Any}  True
        :param StartOnBoot: {bool}  True
        :param DisplayImageSource: {str}  True
        :param TargetDatastore: {int}  True
        :returns: Any
        """
        return await self.api_call_async("ADSModule/CreateInstance", { 
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

    def CreateLocalInstance(self, Instance: Any, PostCreate: Any) -> Any:
        """
        Name Description Optional
        :param Instance: {Any}  False
        :param PostCreate: {Any}  True
        :returns: Any
        """
        return self.api_call("ADSModule/CreateLocalInstance", { 
            "Instance": Instance,
            "PostCreate": PostCreate,
        })

    async def CreateLocalInstanceAsync(self, Instance: Any, PostCreate: Any) -> Any:
        """
        Name Description Optional
        :param Instance: {Any}  False
        :param PostCreate: {Any}  True
        :returns: Any
        """
        return await self.api_call_async("ADSModule/CreateLocalInstance", { 
            "Instance": Instance,
            "PostCreate": PostCreate,
        })

    def DeleteDatastore(self, id: int) -> Any:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: Any
        """
        return self.api_call("ADSModule/DeleteDatastore", { 
            "id": id,
        })

    async def DeleteDatastoreAsync(self, id: int) -> Any:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/DeleteDatastore", { 
            "id": id,
        })

    def DeleteDeploymentTemplate(self, Id: int) -> Any:
        """
        Name Description Optional
        :param Id: {int}  False
        :returns: Any
        """
        return self.api_call("ADSModule/DeleteDeploymentTemplate", { 
            "Id": Id,
        })

    async def DeleteDeploymentTemplateAsync(self, Id: int) -> Any:
        """
        Name Description Optional
        :param Id: {int}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/DeleteDeploymentTemplate", { 
            "Id": Id,
        })

    def DeleteInstance(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/DeleteInstance", { 
            "InstanceName": InstanceName,
        })

    async def DeleteInstanceAsync(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/DeleteInstance", { 
            "InstanceName": InstanceName,
        })

    def DeleteInstanceUsers(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })

    async def DeleteInstanceUsersAsync(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })

    def DeployTemplate(self, TemplateID: int, NewUsername: str, NewPassword: str, NewEmail: str, RequiredTags: list[str], Tag: str, FriendlyName: str, Secret: str, PostCreate: Any, ExtraProvisionSettings: dict[str, str]) -> Any:
        """A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself.
        Name Description Optional
        :param TemplateID: {int} The ID of the template to be deployed, as per the Template Management UI in AMP itself. False
        :param NewUsername: {str} If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user. True
        :param NewPassword: {str} If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user. True
        :param NewEmail: {str} If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user. True
        :param RequiredTags: {list[str]} If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings. True
        :param Tag: {str} Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique. True
        :param FriendlyName: {str} A friendly name for this instance. If left blank, AMP will generate one for you. True
        :param Secret: {str} Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request. True
        :param PostCreate: {Any} 0: Do nothing, 1: Start instance only, 2: Start instance and update application, 3: Full application startup. True
        :param ExtraProvisionSettings: {dict[str, str]} A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself. True
        :returns: Any
        """
        return self.api_call("ADSModule/DeployTemplate", { 
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

    async def DeployTemplateAsync(self, TemplateID: int, NewUsername: str, NewPassword: str, NewEmail: str, RequiredTags: list[str], Tag: str, FriendlyName: str, Secret: str, PostCreate: Any, ExtraProvisionSettings: dict[str, str]) -> Any:
        """A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself.
        Name Description Optional
        :param TemplateID: {int} The ID of the template to be deployed, as per the Template Management UI in AMP itself. False
        :param NewUsername: {str} If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user. True
        :param NewPassword: {str} If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user. True
        :param NewEmail: {str} If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user. True
        :param RequiredTags: {list[str]} If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings. True
        :param Tag: {str} Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique. True
        :param FriendlyName: {str} A friendly name for this instance. If left blank, AMP will generate one for you. True
        :param Secret: {str} Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request. True
        :param PostCreate: {Any} 0: Do nothing, 1: Start instance only, 2: Start instance and update application, 3: Full application startup. True
        :param ExtraProvisionSettings: {dict[str, str]} A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself. True
        :returns: Any
        """
        return await self.api_call_async("ADSModule/DeployTemplate", { 
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

    def DetatchTarget(self, Id: str) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/DetatchTarget", { 
            "Id": Id,
        })

    async def DetatchTargetAsync(self, Id: str) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/DetatchTarget", { 
            "Id": Id,
        })

    def ExtractEverywhere(self, SourceArchive: str) -> Any:
        """
        Name Description Optional
        :param SourceArchive: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/ExtractEverywhere", { 
            "SourceArchive": SourceArchive,
        })

    async def ExtractEverywhereAsync(self, SourceArchive: str) -> Any:
        """
        Name Description Optional
        :param SourceArchive: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ExtractEverywhere", { 
            "SourceArchive": SourceArchive,
        })

    def GetApplicationEndpoints(self, instanceId: str) -> list:
        """
        Name Description Optional
        :param instanceId: {str}  False
        :returns: list
        """
        return self.api_call("ADSModule/GetApplicationEndpoints", { 
            "instanceId": instanceId,
        })

    async def GetApplicationEndpointsAsync(self, instanceId: str) -> list:
        """
        Name Description Optional
        :param instanceId: {str}  False
        :returns: list
        """
        return await self.api_call_async("ADSModule/GetApplicationEndpoints", { 
            "instanceId": instanceId,
        })

    def GetDatastore(self, id: int) -> Any:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: Any
        """
        return self.api_call("ADSModule/GetDatastore", { 
            "id": id,
        })

    async def GetDatastoreAsync(self, id: int) -> Any:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/GetDatastore", { 
            "id": id,
        })

    def GetDatastoreInstances(self, datastoreId: int) -> list[dict]:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: list[dict]
        """
        return self.api_call("ADSModule/GetDatastoreInstances", { 
            "datastoreId": datastoreId,
        })

    async def GetDatastoreInstancesAsync(self, datastoreId: int) -> list[dict]:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: list[dict]
        """
        return await self.api_call_async("ADSModule/GetDatastoreInstances", { 
            "datastoreId": datastoreId,
        })

    def GetDatastores(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("ADSModule/GetDatastores", { 
        })

    async def GetDatastoresAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("ADSModule/GetDatastores", { 
        })

    def GetDeploymentTemplates(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("ADSModule/GetDeploymentTemplates", { 
        })

    async def GetDeploymentTemplatesAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("ADSModule/GetDeploymentTemplates", { 
        })

    def GetGroup(self, GroupId: str) -> bool:
        """
        Name Description Optional
        :param GroupId: {str}  False
        :returns: bool
        """
        return self.api_call("ADSModule/GetGroup", { 
            "GroupId": GroupId,
        })

    async def GetGroupAsync(self, GroupId: str) -> bool:
        """
        Name Description Optional
        :param GroupId: {str}  False
        :returns: bool
        """
        return await self.api_call_async("ADSModule/GetGroup", { 
            "GroupId": GroupId,
        })

    def GetInstance(self, InstanceId: str) -> dict:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: dict
        """
        return self.api_call("ADSModule/GetInstance", { 
            "InstanceId": InstanceId,
        })

    async def GetInstanceAsync(self, InstanceId: str) -> dict:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: dict
        """
        return await self.api_call_async("ADSModule/GetInstance", { 
            "InstanceId": InstanceId,
        })

    def GetInstanceNetworkInfo(self, InstanceName: str) -> list:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: list
        """
        return self.api_call("ADSModule/GetInstanceNetworkInfo", { 
            "InstanceName": InstanceName,
        })

    async def GetInstanceNetworkInfoAsync(self, InstanceName: str) -> list:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: list
        """
        return await self.api_call_async("ADSModule/GetInstanceNetworkInfo", { 
            "InstanceName": InstanceName,
        })

    def GetInstanceStatuses(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return self.api_call("ADSModule/GetInstanceStatuses", { 
        })

    async def GetInstanceStatusesAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return await self.api_call_async("ADSModule/GetInstanceStatuses", { 
        })

    def GetInstances(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("ADSModule/GetInstances", { 
        })

    async def GetInstancesAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("ADSModule/GetInstances", { 
        })

    def GetLocalInstances(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return self.api_call("ADSModule/GetLocalInstances", { 
        })

    async def GetLocalInstancesAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return await self.api_call_async("ADSModule/GetLocalInstances", { 
        })

    def GetProvisionArguments(self, ModuleName: str) -> list[dict]:
        """
        Name Description Optional
        :param ModuleName: {str}  False
        :returns: list[dict]
        """
        return self.api_call("ADSModule/GetProvisionArguments", { 
            "ModuleName": ModuleName,
        })

    async def GetProvisionArgumentsAsync(self, ModuleName: str) -> list[dict]:
        """
        Name Description Optional
        :param ModuleName: {str}  False
        :returns: list[dict]
        """
        return await self.api_call_async("ADSModule/GetProvisionArguments", { 
            "ModuleName": ModuleName,
        })

    def GetProvisionFitness(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return self.api_call("ADSModule/GetProvisionFitness", { 
        })

    async def GetProvisionFitnessAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("ADSModule/GetProvisionFitness", { 
        })

    def GetSupportedApplications(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("ADSModule/GetSupportedApplications", { 
        })

    async def GetSupportedApplicationsAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("ADSModule/GetSupportedApplications", { 
        })

    def GetTargetInfo(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("ADSModule/GetTargetInfo", { 
        })

    async def GetTargetInfoAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("ADSModule/GetTargetInfo", { 
        })

    def HandoutInstanceConfigs(self, ForModule: str, SettingNode: str, Values: list[str]) -> Any:
        """
        Name Description Optional
        :param ForModule: {str}  False
        :param SettingNode: {str}  False
        :param Values: {list[str]}  False
        :returns: Any
        """
        return self.api_call("ADSModule/HandoutInstanceConfigs", { 
            "ForModule": ForModule,
            "SettingNode": SettingNode,
            "Values": Values,
        })

    async def HandoutInstanceConfigsAsync(self, ForModule: str, SettingNode: str, Values: list[str]) -> Any:
        """
        Name Description Optional
        :param ForModule: {str}  False
        :param SettingNode: {str}  False
        :param Values: {list[str]}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/HandoutInstanceConfigs", { 
            "ForModule": ForModule,
            "SettingNode": SettingNode,
            "Values": Values,
        })

    def ManageInstance(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/ManageInstance", { 
            "InstanceId": InstanceId,
        })

    async def ManageInstanceAsync(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ManageInstance", { 
            "InstanceId": InstanceId,
        })

    def ModifyCustomFirewallRule(self, instanceId: str, PortNumber: int, Range: int, Protocol: str, Description: str, Open: bool) -> Any:
        """
        Name Description Optional
        :param instanceId: {str}  False
        :param PortNumber: {int}  False
        :param Range: {int}  False
        :param Protocol: {str}  False
        :param Description: {str}  False
        :param Open: {bool}  False
        :returns: Any
        """
        return self.api_call("ADSModule/ModifyCustomFirewallRule", { 
            "instanceId": instanceId,
            "PortNumber": PortNumber,
            "Range": Range,
            "Protocol": Protocol,
            "Description": Description,
            "Open": Open,
        })

    async def ModifyCustomFirewallRuleAsync(self, instanceId: str, PortNumber: int, Range: int, Protocol: str, Description: str, Open: bool) -> Any:
        """
        Name Description Optional
        :param instanceId: {str}  False
        :param PortNumber: {int}  False
        :param Range: {int}  False
        :param Protocol: {str}  False
        :param Description: {str}  False
        :param Open: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ModifyCustomFirewallRule", { 
            "instanceId": instanceId,
            "PortNumber": PortNumber,
            "Range": Range,
            "Protocol": Protocol,
            "Description": Description,
            "Open": Open,
        })

    def MoveInstanceDatastore(self, instanceId: str, datastoreId: int) -> Any:
        """
        Name Description Optional
        :param instanceId: {str}  False
        :param datastoreId: {int}  False
        :returns: Any
        """
        return self.api_call("ADSModule/MoveInstanceDatastore", { 
            "instanceId": instanceId,
            "datastoreId": datastoreId,
        })

    async def MoveInstanceDatastoreAsync(self, instanceId: str, datastoreId: int) -> Any:
        """
        Name Description Optional
        :param instanceId: {str}  False
        :param datastoreId: {int}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/MoveInstanceDatastore", { 
            "instanceId": instanceId,
            "datastoreId": datastoreId,
        })

    def ReactivateLocalInstances(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("ADSModule/ReactivateLocalInstances", { 
        })

    async def ReactivateLocalInstancesAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("ADSModule/ReactivateLocalInstances", { 
        })

    def RefreshAppCache(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("ADSModule/RefreshAppCache", { 
        })

    async def RefreshAppCacheAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("ADSModule/RefreshAppCache", { 
        })

    def RefreshGroup(self, GroupId: str) -> Any:
        """
        Name Description Optional
        :param GroupId: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/RefreshGroup", { 
            "GroupId": GroupId,
        })

    async def RefreshGroupAsync(self, GroupId: str) -> Any:
        """
        Name Description Optional
        :param GroupId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/RefreshGroup", { 
            "GroupId": GroupId,
        })

    def RefreshInstanceConfig(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/RefreshInstanceConfig", { 
            "InstanceId": InstanceId,
        })

    async def RefreshInstanceConfigAsync(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/RefreshInstanceConfig", { 
            "InstanceId": InstanceId,
        })

    def RefreshRemoteConfigStores(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("ADSModule/RefreshRemoteConfigStores", { 
        })

    async def RefreshRemoteConfigStoresAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("ADSModule/RefreshRemoteConfigStores", { 
        })

    def RegisterTarget(self, controllerUrl: str, myUrl: str, username: str, password: str, twoFactorToken: str, friendlyName: str) -> Any:
        """
        Name Description Optional
        :param controllerUrl: {str}  False
        :param myUrl: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :param twoFactorToken: {str}  False
        :param friendlyName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/RegisterTarget", { 
            "controllerUrl": controllerUrl,
            "myUrl": myUrl,
            "username": username,
            "password": password,
            "twoFactorToken": twoFactorToken,
            "friendlyName": friendlyName,
        })

    async def RegisterTargetAsync(self, controllerUrl: str, myUrl: str, username: str, password: str, twoFactorToken: str, friendlyName: str) -> Any:
        """
        Name Description Optional
        :param controllerUrl: {str}  False
        :param myUrl: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :param twoFactorToken: {str}  False
        :param friendlyName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/RegisterTarget", { 
            "controllerUrl": controllerUrl,
            "myUrl": myUrl,
            "username": username,
            "password": password,
            "twoFactorToken": twoFactorToken,
            "friendlyName": friendlyName,
        })

    def RepairDatastore(self, id: int) -> Any:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: Any
        """
        return self.api_call("ADSModule/RepairDatastore", { 
            "id": id,
        })

    async def RepairDatastoreAsync(self, id: int) -> Any:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/RepairDatastore", { 
            "id": id,
        })

    def RequestDatastoreSizeCalculation(self, datastoreId: int) -> Any:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: Any
        """
        return self.api_call("ADSModule/RequestDatastoreSizeCalculation", { 
            "datastoreId": datastoreId,
        })

    async def RequestDatastoreSizeCalculationAsync(self, datastoreId: int) -> Any:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/RequestDatastoreSizeCalculation", { 
            "datastoreId": datastoreId,
        })

    def RestartInstance(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/RestartInstance", { 
            "InstanceName": InstanceName,
        })

    async def RestartInstanceAsync(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/RestartInstance", { 
            "InstanceName": InstanceName,
        })

    def Servers(self, id: str, REQ_RAWJSON: str) -> Any:
        """
        Name Description Optional
        :param id: {str}  False
        :param REQ_RAWJSON: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/Servers", { 
            "id": id,
            "REQ_RAWJSON": REQ_RAWJSON,
        })

    async def ServersAsync(self, id: str, REQ_RAWJSON: str) -> Any:
        """
        Name Description Optional
        :param id: {str}  False
        :param REQ_RAWJSON: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/Servers", { 
            "id": id,
            "REQ_RAWJSON": REQ_RAWJSON,
        })

    def SetInstanceConfig(self, InstanceName: str, SettingNode: str, Value: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param SettingNode: {str}  False
        :param Value: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/SetInstanceConfig", { 
            "InstanceName": InstanceName,
            "SettingNode": SettingNode,
            "Value": Value,
        })

    async def SetInstanceConfigAsync(self, InstanceName: str, SettingNode: str, Value: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param SettingNode: {str}  False
        :param Value: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/SetInstanceConfig", { 
            "InstanceName": InstanceName,
            "SettingNode": SettingNode,
            "Value": Value,
        })

    def SetInstanceNetworkInfo(self, InstanceId: str, PortMappings: dict[str, int]) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param PortMappings: {dict[str, int]}  False
        :returns: Any
        """
        return self.api_call("ADSModule/SetInstanceNetworkInfo", { 
            "InstanceId": InstanceId,
            "PortMappings": PortMappings,
        })

    async def SetInstanceNetworkInfoAsync(self, InstanceId: str, PortMappings: dict[str, int]) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param PortMappings: {dict[str, int]}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/SetInstanceNetworkInfo", { 
            "InstanceId": InstanceId,
            "PortMappings": PortMappings,
        })

    def SetInstanceSuspended(self, InstanceName: str, Suspended: bool) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param Suspended: {bool}  False
        :returns: Any
        """
        return self.api_call("ADSModule/SetInstanceSuspended", { 
            "InstanceName": InstanceName,
            "Suspended": Suspended,
        })

    async def SetInstanceSuspendedAsync(self, InstanceName: str, Suspended: bool) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param Suspended: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/SetInstanceSuspended", { 
            "InstanceName": InstanceName,
            "Suspended": Suspended,
        })

    def StartAllInstances(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("ADSModule/StartAllInstances", { 
        })

    async def StartAllInstancesAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("ADSModule/StartAllInstances", { 
        })

    def StartInstance(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/StartInstance", { 
            "InstanceName": InstanceName,
        })

    async def StartInstanceAsync(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/StartInstance", { 
            "InstanceName": InstanceName,
        })

    def StopAllInstances(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("ADSModule/StopAllInstances", { 
        })

    async def StopAllInstancesAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("ADSModule/StopAllInstances", { 
        })

    def StopInstance(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/StopInstance", { 
            "InstanceName": InstanceName,
        })

    async def StopInstanceAsync(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/StopInstance", { 
            "InstanceName": InstanceName,
        })

    def TestADSLoginDetails(self, url: str, username: str, password: str) -> Any:
        """
        Name Description Optional
        :param url: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/TestADSLoginDetails", { 
            "url": url,
            "username": username,
            "password": password,
        })

    async def TestADSLoginDetailsAsync(self, url: str, username: str, password: str) -> Any:
        """
        Name Description Optional
        :param url: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/TestADSLoginDetails", { 
            "url": url,
            "username": username,
            "password": password,
        })

    def UpdateDatastore(self, updatedDatastore: Any) -> Any:
        """
        Name Description Optional
        :param updatedDatastore: {Any}  False
        :returns: Any
        """
        return self.api_call("ADSModule/UpdateDatastore", { 
            "updatedDatastore": updatedDatastore,
        })

    async def UpdateDatastoreAsync(self, updatedDatastore: Any) -> Any:
        """
        Name Description Optional
        :param updatedDatastore: {Any}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/UpdateDatastore", { 
            "updatedDatastore": updatedDatastore,
        })

    def UpdateDeploymentTemplate(self, templateToUpdate: Any) -> Any:
        """
        Name Description Optional
        :param templateToUpdate: {Any}  False
        :returns: Any
        """
        return self.api_call("ADSModule/UpdateDeploymentTemplate", { 
            "templateToUpdate": templateToUpdate,
        })

    async def UpdateDeploymentTemplateAsync(self, templateToUpdate: Any) -> Any:
        """
        Name Description Optional
        :param templateToUpdate: {Any}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/UpdateDeploymentTemplate", { 
            "templateToUpdate": templateToUpdate,
        })

    def UpdateInstanceInfo(self, InstanceId: str, FriendlyName: str, Description: str, StartOnBoot: bool, Suspended: bool, ExcludeFromFirewall: bool, RunInContainer: bool, ContainerMemory: int, MemoryPolicy: Any, ContainerMaxCPU: Any, ContainerImage: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param FriendlyName: {str}  False
        :param Description: {str}  False
        :param StartOnBoot: {bool}  False
        :param Suspended: {bool}  False
        :param ExcludeFromFirewall: {bool}  False
        :param RunInContainer: {bool}  False
        :param ContainerMemory: {int}  False
        :param MemoryPolicy: {Any}  False
        :param ContainerMaxCPU: {Any}  False
        :param ContainerImage: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/UpdateInstanceInfo", { 
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
            "ContainerImage": ContainerImage,
        })

    async def UpdateInstanceInfoAsync(self, InstanceId: str, FriendlyName: str, Description: str, StartOnBoot: bool, Suspended: bool, ExcludeFromFirewall: bool, RunInContainer: bool, ContainerMemory: int, MemoryPolicy: Any, ContainerMaxCPU: Any, ContainerImage: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param FriendlyName: {str}  False
        :param Description: {str}  False
        :param StartOnBoot: {bool}  False
        :param Suspended: {bool}  False
        :param ExcludeFromFirewall: {bool}  False
        :param RunInContainer: {bool}  False
        :param ContainerMemory: {int}  False
        :param MemoryPolicy: {Any}  False
        :param ContainerMaxCPU: {Any}  False
        :param ContainerImage: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/UpdateInstanceInfo", { 
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
            "ContainerImage": ContainerImage,
        })

    def UpdateTarget(self, TargetID: str) -> None:
        """
        Name Description Optional
        :param TargetID: {str}  False
        :returns: None
        """
        return self.api_call("ADSModule/UpdateTarget", { 
            "TargetID": TargetID,
        })

    async def UpdateTargetAsync(self, TargetID: str) -> None:
        """
        Name Description Optional
        :param TargetID: {str}  False
        :returns: None
        """
        return await self.api_call_async("ADSModule/UpdateTarget", { 
            "TargetID": TargetID,
        })

    def UpdateTargetInfo(self, Id: str, FriendlyName: str, Url: str, Description: str, Tags: list[str]) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :param FriendlyName: {str}  False
        :param Url: {str}  False
        :param Description: {str}  False
        :param Tags: {list[str]}  False
        :returns: Any
        """
        return self.api_call("ADSModule/UpdateTargetInfo", { 
            "Id": Id,
            "FriendlyName": FriendlyName,
            "Url": Url,
            "Description": Description,
            "Tags": Tags,
        })

    async def UpdateTargetInfoAsync(self, Id: str, FriendlyName: str, Url: str, Description: str, Tags: list[str]) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :param FriendlyName: {str}  False
        :param Url: {str}  False
        :param Description: {str}  False
        :param Tags: {list[str]}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/UpdateTargetInfo", { 
            "Id": Id,
            "FriendlyName": FriendlyName,
            "Url": Url,
            "Description": Description,
            "Tags": Tags,
        })

    def UpgradeAllInstances(self, RestartRunning: bool) -> Any:
        """
        Name Description Optional
        :param RestartRunning: {bool}  False
        :returns: Any
        """
        return self.api_call("ADSModule/UpgradeAllInstances", { 
            "RestartRunning": RestartRunning,
        })

    async def UpgradeAllInstancesAsync(self, RestartRunning: bool) -> Any:
        """
        Name Description Optional
        :param RestartRunning: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/UpgradeAllInstances", { 
            "RestartRunning": RestartRunning,
        })

    def UpgradeInstance(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return self.api_call("ADSModule/UpgradeInstance", { 
            "InstanceName": InstanceName,
        })

    async def UpgradeInstanceAsync(self, InstanceName: str) -> Any:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("ADSModule/UpgradeInstance", { 
            "InstanceName": InstanceName,
        })

