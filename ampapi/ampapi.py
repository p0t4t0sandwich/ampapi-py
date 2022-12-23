#!/bin/python3

from dataclasses import dataclass

import requests
import json

from aiohttp import ClientSession

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

class AMPAPIAsync():
    def __init__(self, baseUri: str) -> None:
        self.baseUri = baseUri
        self.sessionId = ""
        self.dataSource = ""

        if not self.baseUri[-1] == "/":
            self.dataSource = self.baseUri + "/API"
        else:
            self.dataSource = self.baseUri + "API"

    async def APICallAsync(self, endpoint: str, data: dict = {}) -> dict:
        headers = {'accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)

        data_json = json.dumps(data_added)

        async with ClientSession() as session:
            async with session.post(url=f'{self.dataSource}{endpoint}', headers=headers, data=data_json) as post:
                response = await post.json()
                post.close()

        return response

    async def ADSModule_AddDatastoreAsync(self, newDatastore):
        data = {"newDatastore": newDatastore, }
        return await self.APICallAsync(endpoint="/ADSModule/AddDatastore", data=data)

    async def ADSModule_DeleteDatastoreAsync(self, id):
        data = {"id": id, }
        return await self.APICallAsync(endpoint="/ADSModule/DeleteDatastore", data=data)

    async def ADSModule_UpdateDatastoreAsync(self, updatedDatastore):
        data = {"updatedDatastore": updatedDatastore, }
        return await self.APICallAsync(endpoint="/ADSModule/UpdateDatastore", data=data)

    async def ADSModule_GetDatastoresAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetDatastores", data=data)

    async def ADSModule_RequestDatastoreSizeCalculationAsync(self, datastoreId):
        data = {"datastoreId": datastoreId, }
        return await self.APICallAsync(endpoint="/ADSModule/RequestDatastoreSizeCalculation", data=data)

    async def ADSModule_GetDatastoreAsync(self, id):
        data = {"id": id, }
        return await self.APICallAsync(endpoint="/ADSModule/GetDatastore", data=data)

    async def ADSModule_RepairDatastoreAsync(self, id):
        data = {"id": id, }
        return await self.APICallAsync(endpoint="/ADSModule/RepairDatastore", data=data)

    async def ADSModule_GetDatastoreInstancesAsync(self, datastoreId):
        data = {"datastoreId": datastoreId, }
        return await self.APICallAsync(endpoint="/ADSModule/GetDatastoreInstances", data=data)

    async def ADSModule_MoveInstanceDatastoreAsync(self, instanceId, datastoreId):
        data = {"instanceId": instanceId, "datastoreId": datastoreId, }
        return await self.APICallAsync(endpoint="/ADSModule/MoveInstanceDatastore", data=data)

    async def ADSModule_GetDeploymentTemplatesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetDeploymentTemplates", data=data)

    async def ADSModule_CreateDeploymentTemplateAsync(self, Name):
        data = {"Name": Name, }
        return await self.APICallAsync(endpoint="/ADSModule/CreateDeploymentTemplate", data=data)

    async def ADSModule_UpdateDeploymentTemplateAsync(self, templateToUpdate):
        data = {"templateToUpdate": templateToUpdate, }
        return await self.APICallAsync(endpoint="/ADSModule/UpdateDeploymentTemplate", data=data)

    async def ADSModule_DeleteDeploymentTemplateAsync(self, Id):
        data = {"Id": Id, }
        return await self.APICallAsync(endpoint="/ADSModule/DeleteDeploymentTemplate", data=data)

    async def ADSModule_CloneTemplateAsync(self, Id, NewName):
        data = {"Id": Id, "NewName": NewName, }
        return await self.APICallAsync(endpoint="/ADSModule/CloneTemplate", data=data)

    async def ADSModule_ApplyTemplateAsync(self, InstanceID, TemplateID, NewFriendlyName, Secret, RestartIfPreviouslyRunning):
        data = {"InstanceID": InstanceID, "TemplateID": TemplateID, "NewFriendlyName": NewFriendlyName, "Secret": Secret, "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning, }
        return await self.APICallAsync(endpoint="/ADSModule/ApplyTemplate", data=data)

    async def ADSModule_DeployTemplateAsync(self, TemplateID, NewUsername, NewPassword, NewEmail, RequiredTags, Tag, FriendlyName, Secret, PostCreate, ExtraProvisionSettings):
        data = {"TemplateID": TemplateID, "NewUsername": NewUsername, "NewPassword": NewPassword, "NewEmail": NewEmail, "RequiredTags": RequiredTags, "Tag": Tag, "FriendlyName": FriendlyName, "Secret": Secret, "PostCreate": PostCreate, "ExtraProvisionSettings": ExtraProvisionSettings, }
        return await self.APICallAsync(endpoint="/ADSModule/DeployTemplate", data=data)

    async def ADSModule_GetTargetInfoAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetTargetInfo", data=data)

    async def ADSModule_GetSupportedApplicationsAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetSupportedApplications", data=data)

    async def ADSModule_RefreshAppCacheAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/RefreshAppCache", data=data)

    async def ADSModule_RefreshRemoteConfigStoresAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/RefreshRemoteConfigStores", data=data)

    async def ADSModule_GetApplicationEndpointsAsync(self, instanceId):
        data = {"instanceId": instanceId, }
        return await self.APICallAsync(endpoint="/ADSModule/GetApplicationEndpoints", data=data)

    async def ADSModule_ReactivateLocalInstancesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/ReactivateLocalInstances", data=data)

    async def ADSModule_GetInstancesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetInstances", data=data)

    async def ADSModule_GetInstanceAsync(self, InstanceId):
        data = {"InstanceId": InstanceId, }
        return await self.APICallAsync(endpoint="/ADSModule/GetInstance", data=data)

    async def ADSModule_ModifyCustomFirewallRuleAsync(self, instanceId, PortNumber, Range, Protocol, Description, Open):
        data = {"instanceId": instanceId, "PortNumber": PortNumber, "Range": Range, "Protocol": Protocol, "Description": Description, "Open": Open, }
        return await self.APICallAsync(endpoint="/ADSModule/ModifyCustomFirewallRule", data=data)

    async def ADSModule_ManageInstanceAsync(self, InstanceId):
        data = {"InstanceId": InstanceId, }
        return await self.APICallAsync(endpoint="/ADSModule/ManageInstance", data=data)

    async def ADSModule_GetGroupAsync(self, GroupId):
        data = {"GroupId": GroupId, }
        return await self.APICallAsync(endpoint="/ADSModule/GetGroup", data=data)

    async def ADSModule_RefreshGroupAsync(self, GroupId):
        data = {"GroupId": GroupId, }
        return await self.APICallAsync(endpoint="/ADSModule/RefreshGroup", data=data)

    async def ADSModule_GetLocalInstancesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetLocalInstances", data=data)

    async def ADSModule_GetInstanceStatusesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetInstanceStatuses", data=data)

    async def ADSModule_GetProvisionFitnessAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/GetProvisionFitness", data=data)

    async def ADSModule_AttachADSAsync(self, Friendly, IsHTTPS, Host, Port, InstanceID):
        data = {"Friendly": Friendly, "IsHTTPS": IsHTTPS, "Host": Host, "Port": Port, "InstanceID": InstanceID, }
        return await self.APICallAsync(endpoint="/ADSModule/AttachADS", data=data)

    async def ADSModule_DetatchTargetAsync(self, Id):
        data = {"Id": Id, }
        return await self.APICallAsync(endpoint="/ADSModule/DetatchTarget", data=data)

    async def ADSModule_UpdateTargetInfoAsync(self, Id, FriendlyName, Url, Description, Tags):
        data = {"Id": Id, "FriendlyName": FriendlyName, "Url": Url, "Description": Description, "Tags": Tags, }
        return await self.APICallAsync(endpoint="/ADSModule/UpdateTargetInfo", data=data)

    async def ADSModule_ConvertToManagedAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/ConvertToManaged", data=data)

    async def ADSModule_GetInstanceNetworkInfoAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/GetInstanceNetworkInfo", data=data)

    async def ADSModule_SetInstanceNetworkInfoAsync(self, InstanceId, PortMappings):
        data = {"InstanceId": InstanceId, "PortMappings": PortMappings, }
        return await self.APICallAsync(endpoint="/ADSModule/SetInstanceNetworkInfo", data=data)

    async def ADSModule_ApplyInstanceConfigurationAsync(self, InstanceID, Flags):
        data = {"InstanceID": InstanceID, "Flags": Flags, }
        return await self.APICallAsync(endpoint="/ADSModule/ApplyInstanceConfiguration", data=data)

    async def ADSModule_CreateLocalInstanceAsync(self, Instance, PostCreate):
        data = {"Instance": Instance, "PostCreate": PostCreate, }
        return await self.APICallAsync(endpoint="/ADSModule/CreateLocalInstance", data=data)

    async def ADSModule_CreateInstanceAsync(self, TargetADSInstance, NewInstanceId, Module, InstanceName, FriendlyName, IPBinding, PortNumber, AdminUsername, AdminPassword, ProvisionSettings, AutoConfigure, PostCreate, StartOnBoot, DisplayImageSource, TargetDatastore):
        data = {"TargetADSInstance": TargetADSInstance, "NewInstanceId": NewInstanceId, "Module": Module, "InstanceName": InstanceName, "FriendlyName": FriendlyName, "IPBinding": IPBinding, "PortNumber": PortNumber, "AdminUsername": AdminUsername, "AdminPassword": AdminPassword, "ProvisionSettings": ProvisionSettings, "AutoConfigure": AutoConfigure, "PostCreate": PostCreate, "StartOnBoot": StartOnBoot, "DisplayImageSource": DisplayImageSource, "TargetDatastore": TargetDatastore, }
        return await self.APICallAsync(endpoint="/ADSModule/CreateInstance", data=data)

    async def ADSModule_SetInstanceConfigAsync(self, InstanceName, SettingNode, Value):
        data = {"InstanceName": InstanceName, "SettingNode": SettingNode, "Value": Value, }
        return await self.APICallAsync(endpoint="/ADSModule/SetInstanceConfig", data=data)

    async def ADSModule_RefreshInstanceConfigAsync(self, InstanceId):
        data = {"InstanceId": InstanceId, }
        return await self.APICallAsync(endpoint="/ADSModule/RefreshInstanceConfig", data=data)

    async def ADSModule_HandoutInstanceConfigsAsync(self, ForModule, SettingNode, Values):
        data = {"ForModule": ForModule, "SettingNode": SettingNode, "Values": Values, }
        return await self.APICallAsync(endpoint="/ADSModule/HandoutInstanceConfigs", data=data)

    async def ADSModule_GetProvisionArgumentsAsync(self, ModuleName):
        data = {"ModuleName": ModuleName, }
        return await self.APICallAsync(endpoint="/ADSModule/GetProvisionArguments", data=data)

    async def ADSModule_TestADSLoginDetailsAsync(self, url, username, password):
        data = {"url": url, "username": username, "password": password, }
        return await self.APICallAsync(endpoint="/ADSModule/TestADSLoginDetails", data=data)

    async def ADSModule_RegisterTargetAsync(self, controllerUrl, myUrl, username, password, twoFactorToken, friendlyName):
        data = {"controllerUrl": controllerUrl, "myUrl": myUrl, "username": username, "password": password, "twoFactorToken": twoFactorToken, "friendlyName": friendlyName, }
        return await self.APICallAsync(endpoint="/ADSModule/RegisterTarget", data=data)

    async def ADSModule_UpdateTargetAsync(self, TargetID):
        data = {"TargetID": TargetID, }
        return await self.APICallAsync(endpoint="/ADSModule/UpdateTarget", data=data)

    async def ADSModule_UpdateInstanceInfoAsync(self, InstanceId, FriendlyName, Description, StartOnBoot, Suspended, ExcludeFromFirewall, RunInContainer, ContainerMemory, MemoryPolicy, ContainerMaxCPU):
        data = {"InstanceId": InstanceId, "FriendlyName": FriendlyName, "Description": Description, "StartOnBoot": StartOnBoot, "Suspended": Suspended, "ExcludeFromFirewall": ExcludeFromFirewall, "RunInContainer": RunInContainer, "ContainerMemory": ContainerMemory, "MemoryPolicy": MemoryPolicy, "ContainerMaxCPU": ContainerMaxCPU, }
        return await self.APICallAsync(endpoint="/ADSModule/UpdateInstanceInfo", data=data)

    async def ADSModule_SetInstanceSuspendedAsync(self, InstanceName, Suspended):
        data = {"InstanceName": InstanceName, "Suspended": Suspended, }
        return await self.APICallAsync(endpoint="/ADSModule/SetInstanceSuspended", data=data)

    async def ADSModule_UpgradeInstanceAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/UpgradeInstance", data=data)

    async def ADSModule_StartAllInstancesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/StartAllInstances", data=data)

    async def ADSModule_StopAllInstancesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/ADSModule/StopAllInstances", data=data)

    async def ADSModule_UpgradeAllInstancesAsync(self, RestartRunning):
        data = {"RestartRunning": RestartRunning, }
        return await self.APICallAsync(endpoint="/ADSModule/UpgradeAllInstances", data=data)

    async def ADSModule_StartInstanceAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/StartInstance", data=data)

    async def ADSModule_RestartInstanceAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/RestartInstance", data=data)

    async def ADSModule_StopInstanceAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/StopInstance", data=data)

    async def ADSModule_DeleteInstanceUsersAsync(self, InstanceId):
        data = {"InstanceId": InstanceId, }
        return await self.APICallAsync(endpoint="/ADSModule/DeleteInstanceUsers", data=data)

    async def ADSModule_DeleteInstanceAsync(self, InstanceName):
        data = {"InstanceName": InstanceName, }
        return await self.APICallAsync(endpoint="/ADSModule/DeleteInstance", data=data)

    async def ADSModule_ExtractEverywhereAsync(self, SourceArchive):
        data = {"SourceArchive": SourceArchive, }
        return await self.APICallAsync(endpoint="/ADSModule/ExtractEverywhere", data=data)

    async def ADSModule_ServersAsync(self, id, REQ_RAWJSON):
        data = {"id": id, "REQ_RAWJSON": REQ_RAWJSON, }
        return await self.APICallAsync(endpoint="/ADSModule/Servers", data=data)

    async def FileManagerPlugin_DummyAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/FileManagerPlugin/Dummy", data=data)

    async def FileManagerPlugin_CalculateFileMD5SumAsync(self, FilePath):
        data = {"FilePath": FilePath, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/CalculateFileMD5Sum", data=data)

    async def FileManagerPlugin_ChangeExclusionAsync(self, ModifyPath, AsDirectory, Exclude):
        data = {"ModifyPath": ModifyPath, "AsDirectory": AsDirectory, "Exclude": Exclude, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/ChangeExclusion", data=data)

    async def FileManagerPlugin_CreateArchiveAsync(self, PathToArchive):
        data = {"PathToArchive": PathToArchive, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/CreateArchive", data=data)

    async def FileManagerPlugin_ExtractArchiveAsync(self, ArchivePath, DestinationPath):
        data = {"ArchivePath": ArchivePath, "DestinationPath": DestinationPath, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/ExtractArchive", data=data)

    async def FileManagerPlugin_GetDirectoryListingAsync(self, Dir):
        data = {"Dir": Dir, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/GetDirectoryListing", data=data)

    async def FileManagerPlugin_GetFileChunkAsync(self, Filename, Position, Length):
        data = {"Filename": Filename, "Position": Position, "Length": Length, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/GetFileChunk", data=data)

    async def FileManagerPlugin_AppendFileChunkAsync(self, Filename, Data, Delete):
        data = {"Filename": Filename, "Data": Data, "Delete": Delete, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/AppendFileChunk", data=data)

    async def FileManagerPlugin_WriteFileChunkAsync(self, Filename, Position, Data):
        data = {"Filename": Filename, "Position": Position, "Data": Data, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/WriteFileChunk", data=data)

    async def FileManagerPlugin_DownloadFileFromURLAsync(self, Source, TargetDirectory):
        data = {"Source": Source, "TargetDirectory": TargetDirectory, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/DownloadFileFromURL", data=data)

    async def FileManagerPlugin_RenameFileAsync(self, Filename, NewFilename):
        data = {"Filename": Filename, "NewFilename": NewFilename, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/RenameFile", data=data)

    async def FileManagerPlugin_CopyFileAsync(self, Origin, TargetDirectory):
        data = {"Origin": Origin, "TargetDirectory": TargetDirectory, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/CopyFile", data=data)

    async def FileManagerPlugin_TrashFileAsync(self, Filename):
        data = {"Filename": Filename, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/TrashFile", data=data)

    async def FileManagerPlugin_TrashDirectoryAsync(self, DirectoryName):
        data = {"DirectoryName": DirectoryName, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/TrashDirectory", data=data)

    async def FileManagerPlugin_EmptyTrashAsync(self, TrashDirectoryName):
        data = {"TrashDirectoryName": TrashDirectoryName, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/EmptyTrash", data=data)

    async def FileManagerPlugin_CreateDirectoryAsync(self, NewPath):
        data = {"NewPath": NewPath, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/CreateDirectory", data=data)

    async def FileManagerPlugin_RenameDirectoryAsync(self, oldDirectory, NewDirectoryName):
        data = {"oldDirectory": oldDirectory, "NewDirectoryName": NewDirectoryName, }
        return await self.APICallAsync(endpoint="/FileManagerPlugin/RenameDirectory", data=data)

    async def EmailSenderPlugin_TestSMTPSettingsAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/EmailSenderPlugin/TestSMTPSettings", data=data)

    async def LocalFileBackupPlugin_UploadToS3Async(self, BackupId):
        data = {"BackupId": BackupId, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/UploadToS3", data=data)

    async def LocalFileBackupPlugin_DownloadFromS3Async(self, BackupId):
        data = {"BackupId": BackupId, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/DownloadFromS3", data=data)

    async def LocalFileBackupPlugin_DeleteFromS3Async(self, BackupId):
        data = {"BackupId": BackupId, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/DeleteFromS3", data=data)

    async def LocalFileBackupPlugin_GetBackupsAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/GetBackups", data=data)

    async def LocalFileBackupPlugin_RestoreBackupAsync(self, BackupId, DeleteExistingData):
        data = {"BackupId": BackupId, "DeleteExistingData": DeleteExistingData, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/RestoreBackup", data=data)

    async def LocalFileBackupPlugin_DeleteLocalBackupAsync(self, BackupId):
        data = {"BackupId": BackupId, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/DeleteLocalBackup", data=data)

    async def LocalFileBackupPlugin_SetBackupStickyAsync(self, BackupId, Sticky):
        data = {"BackupId": BackupId, "Sticky": Sticky, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/SetBackupSticky", data=data)

    async def LocalFileBackupPlugin_TakeBackupAsync(self, Title, Description, Sticky):
        data = {"Title": Title, "Description": Description, "Sticky": Sticky, }
        return await self.APICallAsync(endpoint="/LocalFileBackupPlugin/TakeBackup", data=data)

    async def Core_GetAuditLogEntriesAsync(self, Before, Count):
        data = {"Before": Before, "Count": Count, }
        return await self.APICallAsync(endpoint="/Core/GetAuditLogEntries", data=data)

    async def Core_GetSettingsSpecAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetSettingsSpec", data=data)

    async def Core_RefreshSettingValueListAsync(self, Node):
        data = {"Node": Node, }
        return await self.APICallAsync(endpoint="/Core/RefreshSettingValueList", data=data)

    async def Core_RefreshSettingsSourceCacheAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/RefreshSettingsSourceCache", data=data)

    async def Core_GetSettingValuesAsync(self, SettingNode, WithRefresh):
        data = {"SettingNode": SettingNode, "WithRefresh": WithRefresh, }
        return await self.APICallAsync(endpoint="/Core/GetSettingValues", data=data)

    async def Core_GetProvisionSpecAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetProvisionSpec", data=data)

    async def Core_GetConfigAsync(self, node):
        data = {"node": node, }
        return await self.APICallAsync(endpoint="/Core/GetConfig", data=data)

    async def Core_GetConfigsAsync(self, nodes):
        data = {"nodes": nodes, }
        return await self.APICallAsync(endpoint="/Core/GetConfigs", data=data)

    async def Core_SetConfigsAsync(self, data):
        data = {"data": data, }
        return await self.APICallAsync(endpoint="/Core/SetConfigs", data=data)

    async def Core_SetConfigAsync(self, node, value):
        data = {"node": node, "value": value, }
        return await self.APICallAsync(endpoint="/Core/SetConfig", data=data)

    async def Core_GetRoleDataAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetRoleData", data=data)

    async def Core_GetRoleIdsAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetRoleIds", data=data)

    async def Core_GetRoleAsync(self, RoleId):
        data = {"RoleId": RoleId, }
        return await self.APICallAsync(endpoint="/Core/GetRole", data=data)

    async def Core_CreateRoleAsync(self, Name, AsCommonRole):
        data = {"Name": Name, "AsCommonRole": AsCommonRole, }
        return await self.APICallAsync(endpoint="/Core/CreateRole", data=data)

    async def Core_DeleteRoleAsync(self, RoleId):
        data = {"RoleId": RoleId, }
        return await self.APICallAsync(endpoint="/Core/DeleteRole", data=data)

    async def Core_RenameRoleAsync(self, RoleId, NewName):
        data = {"RoleId": RoleId, "NewName": NewName, }
        return await self.APICallAsync(endpoint="/Core/RenameRole", data=data)

    async def Core_SetAMPRolePermissionAsync(self, RoleId, PermissionNode, Enabled):
        data = {"RoleId": RoleId, "PermissionNode": PermissionNode, "Enabled": Enabled, }
        return await self.APICallAsync(endpoint="/Core/SetAMPRolePermission", data=data)

    async def Core_GetAMPRolePermissionsAsync(self, RoleId):
        data = {"RoleId": RoleId, }
        return await self.APICallAsync(endpoint="/Core/GetAMPRolePermissions", data=data)

    async def Core_GetScheduleDataAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetScheduleData", data=data)

    async def Core_AddEventTriggerAsync(self, triggerId):
        data = {"triggerId": triggerId, }
        return await self.APICallAsync(endpoint="/Core/AddEventTrigger", data=data)

    async def Core_RunEventTriggerImmediatelyAsync(self, triggerId):
        data = {"triggerId": triggerId, }
        return await self.APICallAsync(endpoint="/Core/RunEventTriggerImmediately", data=data)

    async def Core_AddIntervalTriggerAsync(self, months, days, hours, minutes, daysOfMonth, description):
        data = {"months": months, "days": days, "hours": hours, "minutes": minutes, "daysOfMonth": daysOfMonth, "description": description, }
        return await self.APICallAsync(endpoint="/Core/AddIntervalTrigger", data=data)

    async def Core_GetTimeIntervalTriggerAsync(self, Id):
        data = {"Id": Id, }
        return await self.APICallAsync(endpoint="/Core/GetTimeIntervalTrigger", data=data)

    async def Core_EditIntervalTriggerAsync(self, Id, months, days, hours, minutes, daysOfMonth, description):
        data = {"Id": Id, "months": months, "days": days, "hours": hours, "minutes": minutes, "daysOfMonth": daysOfMonth, "description": description, }
        return await self.APICallAsync(endpoint="/Core/EditIntervalTrigger", data=data)

    async def Core_AddTaskAsync(self, TriggerID, MethodID, ParameterMapping):
        data = {"TriggerID": TriggerID, "MethodID": MethodID, "ParameterMapping": ParameterMapping, }
        return await self.APICallAsync(endpoint="/Core/AddTask", data=data)

    async def Core_EditTaskAsync(self, TriggerID, TaskID, ParameterMapping):
        data = {"TriggerID": TriggerID, "TaskID": TaskID, "ParameterMapping": ParameterMapping, }
        return await self.APICallAsync(endpoint="/Core/EditTask", data=data)

    async def Core_ChangeTaskOrderAsync(self, TriggerID, TaskID, NewOrder):
        data = {"TriggerID": TriggerID, "TaskID": TaskID, "NewOrder": NewOrder, }
        return await self.APICallAsync(endpoint="/Core/ChangeTaskOrder", data=data)

    async def Core_DeleteTaskAsync(self, TriggerID, TaskID):
        data = {"TriggerID": TriggerID, "TaskID": TaskID, }
        return await self.APICallAsync(endpoint="/Core/DeleteTask", data=data)

    async def Core_DeleteTriggerAsync(self, TriggerID):
        data = {"TriggerID": TriggerID, }
        return await self.APICallAsync(endpoint="/Core/DeleteTrigger", data=data)

    async def Core_GetActiveAMPSessionsAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetActiveAMPSessions", data=data)

    async def Core_EndUserSessionAsync(self, Id):
        data = {"Id": Id, }
        return await self.APICallAsync(endpoint="/Core/EndUserSession", data=data)

    async def Core_GetAMPUsersSummaryAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetAMPUsersSummary", data=data)

    async def Core_GetAMPUserInfoAsync(self, Username):
        data = {"Username": Username, }
        return await self.APICallAsync(endpoint="/Core/GetAMPUserInfo", data=data)

    async def Core_GetAllAMPUserInfoAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetAllAMPUserInfo", data=data)

    async def Core_SetAMPUserRoleMembershipAsync(self, UserId, RoleId, IsMember):
        data = {"UserId": UserId, "RoleId": RoleId, "IsMember": IsMember, }
        return await self.APICallAsync(endpoint="/Core/SetAMPUserRoleMembership", data=data)

    async def Core_GetPermissionsSpecAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetPermissionsSpec", data=data)

    async def Core_CreateUserAsync(self, Username):
        data = {"Username": Username, }
        return await self.APICallAsync(endpoint="/Core/CreateUser", data=data)

    async def Core_DeleteUserAsync(self, Username):
        data = {"Username": Username, }
        return await self.APICallAsync(endpoint="/Core/DeleteUser", data=data)

    async def Core_UpdateUserInfoAsync(self, Username, Disabled, PasswordExpires, CannotChangePassword, MustChangePassword, EmailAddress):
        data = {"Username": Username, "Disabled": Disabled, "PasswordExpires": PasswordExpires, "CannotChangePassword": CannotChangePassword, "MustChangePassword": MustChangePassword, "EmailAddress": EmailAddress, }
        return await self.APICallAsync(endpoint="/Core/UpdateUserInfo", data=data)

    async def Core_GetWebauthnChallengeAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetWebauthnChallenge", data=data)

    async def Core_GetWebauthnCredentialIDsAsync(self, username):
        data = {"username": username, }
        return await self.APICallAsync(endpoint="/Core/GetWebauthnCredentialIDs", data=data)

    async def Core_WebauthnRegisterAsync(self, attestationObject, clientDataJSON, description):
        data = {"attestationObject": attestationObject, "clientDataJSON": clientDataJSON, "description": description, }
        return await self.APICallAsync(endpoint="/Core/WebauthnRegister", data=data)

    async def Core_GetWebauthnCredentialSummariesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetWebauthnCredentialSummaries", data=data)

    async def Core_RevokeWebauthnCredentialAsync(self, ID):
        data = {"ID": ID, }
        return await self.APICallAsync(endpoint="/Core/RevokeWebauthnCredential", data=data)

    async def Core_UpdateAccountInfoAsync(self, EmailAddress, TwoFactorPIN):
        data = {"EmailAddress": EmailAddress, "TwoFactorPIN": TwoFactorPIN, }
        return await self.APICallAsync(endpoint="/Core/UpdateAccountInfo", data=data)

    async def Core_EnableTwoFactorAsync(self, Username, Password):
        data = {"Username": Username, "Password": Password, }
        return await self.APICallAsync(endpoint="/Core/EnableTwoFactor", data=data)

    async def Core_ConfirmTwoFactorSetupAsync(self, Username, TwoFactorCode):
        data = {"Username": Username, "TwoFactorCode": TwoFactorCode, }
        return await self.APICallAsync(endpoint="/Core/ConfirmTwoFactorSetup", data=data)

    async def Core_DisableTwoFactorAsync(self, Password, TwoFactorCode):
        data = {"Password": Password, "TwoFactorCode": TwoFactorCode, }
        return await self.APICallAsync(endpoint="/Core/DisableTwoFactor", data=data)

    async def Core_ResetUserPasswordAsync(self, Username, NewPassword):
        data = {"Username": Username, "NewPassword": NewPassword, }
        return await self.APICallAsync(endpoint="/Core/ResetUserPassword", data=data)

    async def Core_DeleteInstanceUsersAsync(self, InstanceId):
        data = {"InstanceId": InstanceId, }
        return await self.APICallAsync(endpoint="/Core/DeleteInstanceUsers", data=data)

    async def Core_ChangeUserPasswordAsync(self, Username, OldPassword, NewPassword, TwoFactorPIN):
        data = {"Username": Username, "OldPassword": OldPassword, "NewPassword": NewPassword, "TwoFactorPIN": TwoFactorPIN, }
        return await self.APICallAsync(endpoint="/Core/ChangeUserPassword", data=data)

    async def Core_GetUpdatesAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetUpdates", data=data)

    async def Core_GetNewGuidAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetNewGuid", data=data)

    async def Core_GetUserListAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetUserList", data=data)

    async def Core_CurrentSessionHasPermissionAsync(self, PermissionNode):
        data = {"PermissionNode": PermissionNode, }
        return await self.APICallAsync(endpoint="/Core/CurrentSessionHasPermission", data=data)

    async def Core_GetTasksAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetTasks", data=data)

    async def Core_GetStatusAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetStatus", data=data)

    async def Core_CancelTaskAsync(self, TaskId):
        data = {"TaskId": TaskId, }
        return await self.APICallAsync(endpoint="/Core/CancelTask", data=data)

    async def Core_DismissTaskAsync(self, TaskId):
        data = {"TaskId": TaskId, }
        return await self.APICallAsync(endpoint="/Core/DismissTask", data=data)

    async def Core_GetUserInfoAsync(self, UID):
        data = {"UID": UID, }
        return await self.APICallAsync(endpoint="/Core/GetUserInfo", data=data)

    async def Core_StartAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Start", data=data)

    async def Core_SuspendAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Suspend", data=data)

    async def Core_ResumeAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Resume", data=data)

    async def Core_StopAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Stop", data=data)

    async def Core_RestartAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Restart", data=data)

    async def Core_KillAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Kill", data=data)

    async def Core_SleepAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Sleep", data=data)

    async def Core_UpdateApplicationAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/UpdateApplication", data=data)

    async def Core_AcknowledgeAMPUpdateAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/AcknowledgeAMPUpdate", data=data)

    async def Core_GetModuleInfoAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetModuleInfo", data=data)

    async def Core_GetAPISpecAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetAPISpec", data=data)

    async def Core_GetUserActionsSpecAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetUserActionsSpec", data=data)

    async def Core_LoginAsync(self, username, password, token, rememberMe):
        data = {"username": username, "password": password, "token": token, "rememberMe": rememberMe, }
        return await self.APICallAsync(endpoint="/Core/Login", data=data)

    async def Core_GetRemoteLoginTokenAsync(self, Description, IsTemporary):
        data = {"Description": Description, "IsTemporary": IsTemporary, }
        return await self.APICallAsync(endpoint="/Core/GetRemoteLoginToken", data=data)

    async def Core_SendConsoleMessageAsync(self, message):
        data = {"message": message, }
        return await self.APICallAsync(endpoint="/Core/SendConsoleMessage", data=data)

    async def Core_UpdateAMPInstanceAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/UpdateAMPInstance", data=data)

    async def Core_GetUpdateInfoAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetUpdateInfo", data=data)

    async def Core_LogoutAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/Logout", data=data)

    async def Core_RestartAMPAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/RestartAMP", data=data)

    async def Core_UpgradeAMPAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/UpgradeAMP", data=data)

    async def Core_GetDiagnosticsInfoAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/GetDiagnosticsInfo", data=data)

    async def Core_CreateTestTaskAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/CreateTestTask", data=data)

    async def Core_AsyncTestAsync(self, ):
        data = {}
        return await self.APICallAsync(endpoint="/Core/AsyncTest", data=data)


class AMPAPIHandler(AMPAPI):
    def __init__(self, baseUri: str, username: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        super().__init__(baseUri=baseUri)
        if self.baseUri[-1] != "/": self.baseUri = self.baseUri + "/"
        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    def Login(self):
        loginResult = self.Core.Login(self.username, self.password, self.rememberMeToken, True)
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    def initHandler(self):
        try:
            # Perform first-stage API initialization.
            APIInitOK = self.init()

            if not APIInitOK:
                print("API Init failed")
                return

            # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
            loginResult = self.Login()

            if "success" in loginResult.keys() and loginResult["success"]:
                print("Login successful")

                # Perform second-stage API initialization, we only get the full API data once we're logged in.
                APIInitOK = self.init()
                if not APIInitOK:
                    print("API Stage 2 Init failed")
                    return
            else:
                print("Login failed")
                print(loginResult)

        except Exception as err:
            print(err)

    def APICallDirect(self, endpoint: str, data: dict = {}) -> dict:
        headers = {'accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)

        data_json = json.dumps(data_added)

        res = requests.post(
            url=f'{self.dataSource}{endpoint}',
            headers=headers,
            data=data_json
        )
        res_json = json.loads(res.content)

        return res_json

    def InstanceAPICall(self, instance_id: str, endpoint: str, data: dict = {}) -> dict:
        result = self.APICallDirect(
            endpoint=f"/ADSModule/Servers/{instance_id}{endpoint}",
            data=data
        )
        return result

    def InstanceLogin(self, instance_id: str):
        loginResult = self.InstanceAPICall(
            instance_id=instance_id,
            endpoint="/API/Core/Login",
            data={
                "username": self.username,
                "password": self.password,
                "token": "",
                "rememberMe": True
            }
        )

        if "success" in loginResult.keys() and loginResult["success"]:
            return AMPAPIHandler(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                password=self.password,
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )


class AMPAPIHandlerAsync(AMPAPIAsync):
    def __init__(self, baseUri: str, username: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        super().__init__(baseUri=baseUri)
        if self.baseUri[-1] != "/": self.baseUri = self.baseUri + "/"
        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    async def LoginAsync(self):
        loginResult = await self.Core_LoginAsync(self.username, self.password, self.rememberMeToken, True)
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    async def InstanceAPICallAsync(self, instance_id: str, endpoint: str, data: dict = {}) -> dict:
        result = await self.APICallAsync(
            endpoint=f"/ADSModule/Servers/{instance_id}{endpoint}",
            data=data
        )
        return result

    async def InstanceLoginAsync(self, instance_id: str):
        loginResult = await self.InstanceAPICallAsync(
            instance_id=instance_id,
            endpoint="/API/Core/Login",
            data={
                "username": self.username,
                "password": self.password,
                "token": "",
                "rememberMe": True
            }
        )

        if "success" in loginResult.keys() and loginResult["success"]:
            return AMPAPIHandlerAsync(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )