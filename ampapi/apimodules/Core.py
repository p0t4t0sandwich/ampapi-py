#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class Core(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the Core class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AcknowledgeAMPUpdate(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/AcknowledgeAMPUpdate", { 
        })

    async def AcknowledgeAMPUpdateAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/AcknowledgeAMPUpdate", { 
        })

    def AddEventTrigger(self, triggerId: str) -> Any:
        """
        Name Description Optional
        :param triggerId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/AddEventTrigger", { 
            "triggerId": triggerId,
        })

    async def AddEventTriggerAsync(self, triggerId: str) -> Any:
        """
        Name Description Optional
        :param triggerId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/AddEventTrigger", { 
            "triggerId": triggerId,
        })

    def AddIntervalTrigger(self, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> Any:
        """
        Name Description Optional
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: Any
        """
        return self.api_call("Core/AddIntervalTrigger", { 
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })

    async def AddIntervalTriggerAsync(self, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> Any:
        """
        Name Description Optional
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/AddIntervalTrigger", { 
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })

    def AddTask(self, TriggerID: str, MethodID: str, ParameterMapping: dict[str, str]) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param MethodID: {str}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: Any
        """
        return self.api_call("Core/AddTask", { 
            "TriggerID": TriggerID,
            "MethodID": MethodID,
            "ParameterMapping": ParameterMapping,
        })

    async def AddTaskAsync(self, TriggerID: str, MethodID: str, ParameterMapping: dict[str, str]) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param MethodID: {str}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: Any
        """
        return await self.api_call_async("Core/AddTask", { 
            "TriggerID": TriggerID,
            "MethodID": MethodID,
            "ParameterMapping": ParameterMapping,
        })

    def AsyncTest(self, ) -> Any:
        """
     * DEV: Async test method
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/AsyncTest", { 
        })

    async def AsyncTestAsync(self, ) -> Any:
        """
     * DEV: Async test method
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/AsyncTest", { 
        })

    def CancelTask(self, TaskId: str) -> Any:
        """
        Name Description Optional
        :param TaskId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/CancelTask", { 
            "TaskId": TaskId,
        })

    async def CancelTaskAsync(self, TaskId: str) -> Any:
        """
        Name Description Optional
        :param TaskId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/CancelTask", { 
            "TaskId": TaskId,
        })

    def ChangeTaskOrder(self, TriggerID: str, TaskID: str, NewOrder: int) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param TaskID: {str}  False
        :param NewOrder: {int}  False
        :returns: Any
        """
        return self.api_call("Core/ChangeTaskOrder", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "NewOrder": NewOrder,
        })

    async def ChangeTaskOrderAsync(self, TriggerID: str, TaskID: str, NewOrder: int) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param TaskID: {str}  False
        :param NewOrder: {int}  False
        :returns: Any
        """
        return await self.api_call_async("Core/ChangeTaskOrder", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "NewOrder": NewOrder,
        })

    def ChangeUserPassword(self, Username: str, OldPassword: str, NewPassword: str, TwoFactorPIN: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param OldPassword: {str}  False
        :param NewPassword: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: Any
        """
        return self.api_call("Core/ChangeUserPassword", { 
            "Username": Username,
            "OldPassword": OldPassword,
            "NewPassword": NewPassword,
            "TwoFactorPIN": TwoFactorPIN,
        })

    async def ChangeUserPasswordAsync(self, Username: str, OldPassword: str, NewPassword: str, TwoFactorPIN: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param OldPassword: {str}  False
        :param NewPassword: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/ChangeUserPassword", { 
            "Username": Username,
            "OldPassword": OldPassword,
            "NewPassword": NewPassword,
            "TwoFactorPIN": TwoFactorPIN,
        })

    def ConfirmTwoFactorSetup(self, Username: str, TwoFactorCode: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: Any
        """
        return self.api_call("Core/ConfirmTwoFactorSetup", { 
            "Username": Username,
            "TwoFactorCode": TwoFactorCode,
        })

    async def ConfirmTwoFactorSetupAsync(self, Username: str, TwoFactorCode: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/ConfirmTwoFactorSetup", { 
            "Username": Username,
            "TwoFactorCode": TwoFactorCode,
        })

    def CreateRole(self, Name: str, AsCommonRole: bool) -> Any:
        """
        Name Description Optional
        :param Name: {str}  False
        :param AsCommonRole: {bool}  True
        :returns: Any
        """
        return self.api_call("Core/CreateRole", { 
            "Name": Name,
            "AsCommonRole": AsCommonRole,
        })

    async def CreateRoleAsync(self, Name: str, AsCommonRole: bool) -> Any:
        """
        Name Description Optional
        :param Name: {str}  False
        :param AsCommonRole: {bool}  True
        :returns: Any
        """
        return await self.api_call_async("Core/CreateRole", { 
            "Name": Name,
            "AsCommonRole": AsCommonRole,
        })

    def CreateTestTask(self, ) -> None:
        """
     * DEV: Creates a non-ending task with 50% progress for testing purposes
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/CreateTestTask", { 
        })

    async def CreateTestTaskAsync(self, ) -> None:
        """
     * DEV: Creates a non-ending task with 50% progress for testing purposes
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/CreateTestTask", { 
        })

    def CreateUser(self, Username: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: Any
        """
        return self.api_call("Core/CreateUser", { 
            "Username": Username,
        })

    async def CreateUserAsync(self, Username: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/CreateUser", { 
            "Username": Username,
        })

    def CurrentSessionHasPermission(self, PermissionNode: str) -> bool:
        """
        Name Description Optional
        :param PermissionNode: {str}  False
        :returns: bool
        """
        return self.api_call("Core/CurrentSessionHasPermission", { 
            "PermissionNode": PermissionNode,
        })

    async def CurrentSessionHasPermissionAsync(self, PermissionNode: str) -> bool:
        """
        Name Description Optional
        :param PermissionNode: {str}  False
        :returns: bool
        """
        return await self.api_call_async("Core/CurrentSessionHasPermission", { 
            "PermissionNode": PermissionNode,
        })

    def DeleteInstanceUsers(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })

    async def DeleteInstanceUsersAsync(self, InstanceId: str) -> Any:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })

    def DeleteRole(self, RoleId: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DeleteRole", { 
            "RoleId": RoleId,
        })

    async def DeleteRoleAsync(self, RoleId: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DeleteRole", { 
            "RoleId": RoleId,
        })

    def DeleteTask(self, TriggerID: str, TaskID: str) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param TaskID: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DeleteTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
        })

    async def DeleteTaskAsync(self, TriggerID: str, TaskID: str) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param TaskID: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DeleteTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
        })

    def DeleteTrigger(self, TriggerID: str) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DeleteTrigger", { 
            "TriggerID": TriggerID,
        })

    async def DeleteTriggerAsync(self, TriggerID: str) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DeleteTrigger", { 
            "TriggerID": TriggerID,
        })

    def DeleteUser(self, Username: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DeleteUser", { 
            "Username": Username,
        })

    async def DeleteUserAsync(self, Username: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DeleteUser", { 
            "Username": Username,
        })

    def DisableTwoFactor(self, Password: str, TwoFactorCode: str) -> Any:
        """
        Name Description Optional
        :param Password: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DisableTwoFactor", { 
            "Password": Password,
            "TwoFactorCode": TwoFactorCode,
        })

    async def DisableTwoFactorAsync(self, Password: str, TwoFactorCode: str) -> Any:
        """
        Name Description Optional
        :param Password: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DisableTwoFactor", { 
            "Password": Password,
            "TwoFactorCode": TwoFactorCode,
        })

    def DismissAllTasks(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/DismissAllTasks", { 
        })

    async def DismissAllTasksAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/DismissAllTasks", { 
        })

    def DismissTask(self, TaskId: str) -> Any:
        """
        Name Description Optional
        :param TaskId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/DismissTask", { 
            "TaskId": TaskId,
        })

    async def DismissTaskAsync(self, TaskId: str) -> Any:
        """
        Name Description Optional
        :param TaskId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/DismissTask", { 
            "TaskId": TaskId,
        })

    def EditIntervalTrigger(self, Id: str, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: Any
        """
        return self.api_call("Core/EditIntervalTrigger", { 
            "Id": Id,
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })

    async def EditIntervalTriggerAsync(self, Id: str, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/EditIntervalTrigger", { 
            "Id": Id,
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })

    def EditTask(self, TriggerID: str, TaskID: str, ParameterMapping: dict[str, str]) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param TaskID: {str}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: Any
        """
        return self.api_call("Core/EditTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "ParameterMapping": ParameterMapping,
        })

    async def EditTaskAsync(self, TriggerID: str, TaskID: str, ParameterMapping: dict[str, str]) -> Any:
        """
        Name Description Optional
        :param TriggerID: {str}  False
        :param TaskID: {str}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: Any
        """
        return await self.api_call_async("Core/EditTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "ParameterMapping": ParameterMapping,
        })

    def EnableTwoFactor(self, Username: str, Password: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Password: {str}  False
        :returns: Any
        """
        return self.api_call("Core/EnableTwoFactor", { 
            "Username": Username,
            "Password": Password,
        })

    async def EnableTwoFactorAsync(self, Username: str, Password: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Password: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/EnableTwoFactor", { 
            "Username": Username,
            "Password": Password,
        })

    def EndUserSession(self, Id: str) -> None:
        """
        Name Description Optional
        :param Id: {str}  False
        :returns: None
        """
        return self.api_call("Core/EndUserSession", { 
            "Id": Id,
        })

    async def EndUserSessionAsync(self, Id: str) -> None:
        """
        Name Description Optional
        :param Id: {str}  False
        :returns: None
        """
        return await self.api_call_async("Core/EndUserSession", { 
            "Id": Id,
        })

    def GetAMPRolePermissions(self, RoleId: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/GetAMPRolePermissions", { 
            "RoleId": RoleId,
        })

    async def GetAMPRolePermissionsAsync(self, RoleId: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/GetAMPRolePermissions", { 
            "RoleId": RoleId,
        })

    def GetAMPUserInfo(self, Username: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: Any
        """
        return self.api_call("Core/GetAMPUserInfo", { 
            "Username": Username,
        })

    async def GetAMPUserInfoAsync(self, Username: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/GetAMPUserInfo", { 
            "Username": Username,
        })

    def GetAMPUsersSummary(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetAMPUsersSummary", { 
        })

    async def GetAMPUsersSummaryAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetAMPUsersSummary", { 
        })

    def GetAPISpec(self, ) -> dict[str, dict]:
        """
        Name Description Optional
        :returns: dict[str, dict]
        """
        return self.api_call("Core/GetAPISpec", { 
        })

    async def GetAPISpecAsync(self, ) -> dict[str, dict]:
        """
        Name Description Optional
        :returns: dict[str, dict]
        """
        return await self.api_call_async("Core/GetAPISpec", { 
        })

    def GetActiveAMPSessions(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("Core/GetActiveAMPSessions", { 
        })

    async def GetActiveAMPSessionsAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("Core/GetActiveAMPSessions", { 
        })

    def GetAllAMPUserInfo(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetAllAMPUserInfo", { 
        })

    async def GetAllAMPUserInfoAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetAllAMPUserInfo", { 
        })

    def GetAuditLogEntries(self, Before: Any, Count: int) -> dict:
        """
        Name Description Optional
        :param Before: {Any}  False
        :param Count: {int}  False
        :returns: dict
        """
        return self.api_call("Core/GetAuditLogEntries", { 
            "Before": Before,
            "Count": Count,
        })

    async def GetAuditLogEntriesAsync(self, Before: Any, Count: int) -> dict:
        """
        Name Description Optional
        :param Before: {Any}  False
        :param Count: {int}  False
        :returns: dict
        """
        return await self.api_call_async("Core/GetAuditLogEntries", { 
            "Before": Before,
            "Count": Count,
        })

    def GetConfig(self, node: str) -> dict:
        """
        Name Description Optional
        :param node: {str}  False
        :returns: dict
        """
        return self.api_call("Core/GetConfig", { 
            "node": node,
        })

    async def GetConfigAsync(self, node: str) -> dict:
        """
        Name Description Optional
        :param node: {str}  False
        :returns: dict
        """
        return await self.api_call_async("Core/GetConfig", { 
            "node": node,
        })

    def GetConfigs(self, nodes: list[str]) -> list[dict]:
        """
        Name Description Optional
        :param nodes: {list[str]}  False
        :returns: list[dict]
        """
        return self.api_call("Core/GetConfigs", { 
            "nodes": nodes,
        })

    async def GetConfigsAsync(self, nodes: list[str]) -> list[dict]:
        """
        Name Description Optional
        :param nodes: {list[str]}  False
        :returns: list[dict]
        """
        return await self.api_call_async("Core/GetConfigs", { 
            "nodes": nodes,
        })

    def GetDiagnosticsInfo(self, ) -> dict[str, str]:
        """
        Name Description Optional
        :returns: dict[str, str]
        """
        return self.api_call("Core/GetDiagnosticsInfo", { 
        })

    async def GetDiagnosticsInfoAsync(self, ) -> dict[str, str]:
        """
        Name Description Optional
        :returns: dict[str, str]
        """
        return await self.api_call_async("Core/GetDiagnosticsInfo", { 
        })

    def GetModuleInfo(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetModuleInfo", { 
        })

    async def GetModuleInfoAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetModuleInfo", { 
        })

    def GetNewGuid(self, ) -> str:
        """
        Name Description Optional
        :returns: str
        """
        return self.api_call("Core/GetNewGuid", { 
        })

    async def GetNewGuidAsync(self, ) -> str:
        """
        Name Description Optional
        :returns: str
        """
        return await self.api_call_async("Core/GetNewGuid", { 
        })

    def GetPermissionsSpec(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("Core/GetPermissionsSpec", { 
        })

    async def GetPermissionsSpecAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("Core/GetPermissionsSpec", { 
        })

    def GetPortSummaries(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("Core/GetPortSummaries", { 
        })

    async def GetPortSummariesAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("Core/GetPortSummaries", { 
        })

    def GetProvisionSpec(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return self.api_call("Core/GetProvisionSpec", { 
        })

    async def GetProvisionSpecAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return await self.api_call_async("Core/GetProvisionSpec", { 
        })

    def GetRemoteLoginToken(self, Description: str, IsTemporary: bool) -> Any:
        """
        Name Description Optional
        :param Description: {str}  True
        :param IsTemporary: {bool}  True
        :returns: Any
        """
        return self.api_call("Core/GetRemoteLoginToken", { 
            "Description": Description,
            "IsTemporary": IsTemporary,
        })

    async def GetRemoteLoginTokenAsync(self, Description: str, IsTemporary: bool) -> Any:
        """
        Name Description Optional
        :param Description: {str}  True
        :param IsTemporary: {bool}  True
        :returns: Any
        """
        return await self.api_call_async("Core/GetRemoteLoginToken", { 
            "Description": Description,
            "IsTemporary": IsTemporary,
        })

    def GetRole(self, RoleId: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/GetRole", { 
            "RoleId": RoleId,
        })

    async def GetRoleAsync(self, RoleId: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/GetRole", { 
            "RoleId": RoleId,
        })

    def GetRoleData(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetRoleData", { 
        })

    async def GetRoleDataAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetRoleData", { 
        })

    def GetRoleIds(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetRoleIds", { 
        })

    async def GetRoleIdsAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetRoleIds", { 
        })

    def GetScheduleData(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetScheduleData", { 
        })

    async def GetScheduleDataAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetScheduleData", { 
        })

    def GetSettingValues(self, SettingNode: str, WithRefresh: bool) -> dict[str, str]:
        """
        Name Description Optional
        :param SettingNode: {str}  False
        :param WithRefresh: {bool}  True
        :returns: dict[str, str]
        """
        return self.api_call("Core/GetSettingValues", { 
            "SettingNode": SettingNode,
            "WithRefresh": WithRefresh,
        })

    async def GetSettingValuesAsync(self, SettingNode: str, WithRefresh: bool) -> dict[str, str]:
        """
        Name Description Optional
        :param SettingNode: {str}  False
        :param WithRefresh: {bool}  True
        :returns: dict[str, str]
        """
        return await self.api_call_async("Core/GetSettingValues", { 
            "SettingNode": SettingNode,
            "WithRefresh": WithRefresh,
        })

    def GetSettingsSpec(self, ) -> dict[str, list[dict]]:
        """
        Name Description Optional
        :returns: dict[str, list[dict]]
        """
        return self.api_call("Core/GetSettingsSpec", { 
        })

    async def GetSettingsSpecAsync(self, ) -> dict[str, list[dict]]:
        """
        Name Description Optional
        :returns: dict[str, list[dict]]
        """
        return await self.api_call_async("Core/GetSettingsSpec", { 
        })

    def GetStatus(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return self.api_call("Core/GetStatus", { 
        })

    async def GetStatusAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("Core/GetStatus", { 
        })

    def GetTasks(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetTasks", { 
        })

    async def GetTasksAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetTasks", { 
        })

    def GetTimeIntervalTrigger(self, Id: str) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :returns: Any
        """
        return self.api_call("Core/GetTimeIntervalTrigger", { 
            "Id": Id,
        })

    async def GetTimeIntervalTriggerAsync(self, Id: str) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/GetTimeIntervalTrigger", { 
            "Id": Id,
        })

    def GetUpdateInfo(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetUpdateInfo", { 
        })

    async def GetUpdateInfoAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetUpdateInfo", { 
        })

    def GetUpdates(self, ) -> dict:
        """
     * Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
        Name Description Optional
        :returns: dict
        """
        return self.api_call("Core/GetUpdates", { 
        })

    async def GetUpdatesAsync(self, ) -> dict:
        """
     * Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("Core/GetUpdates", { 
        })

    def GetUserActionsSpec(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetUserActionsSpec", { 
        })

    async def GetUserActionsSpecAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetUserActionsSpec", { 
        })

    def GetUserInfo(self, UID: str) -> dict:
        """
        Name Description Optional
        :param UID: {str}  False
        :returns: dict
        """
        return self.api_call("Core/GetUserInfo", { 
            "UID": UID,
        })

    async def GetUserInfoAsync(self, UID: str) -> dict:
        """
        Name Description Optional
        :param UID: {str}  False
        :returns: dict
        """
        return await self.api_call_async("Core/GetUserInfo", { 
            "UID": UID,
        })

    def GetUserList(self, ) -> dict[str, str]:
        """
     * Returns a list of in-application users
        Name Description Optional
        :returns: dict[str, str]
        """
        return self.api_call("Core/GetUserList", { 
        })

    async def GetUserListAsync(self, ) -> dict[str, str]:
        """
     * Returns a list of in-application users
        Name Description Optional
        :returns: dict[str, str]
        """
        return await self.api_call_async("Core/GetUserList", { 
        })

    def GetWebauthnChallenge(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetWebauthnChallenge", { 
        })

    async def GetWebauthnChallengeAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetWebauthnChallenge", { 
        })

    def GetWebauthnCredentialIDs(self, username: str) -> Any:
        """
        Name Description Optional
        :param username: {str}  False
        :returns: Any
        """
        return self.api_call("Core/GetWebauthnCredentialIDs", { 
            "username": username,
        })

    async def GetWebauthnCredentialIDsAsync(self, username: str) -> Any:
        """
        Name Description Optional
        :param username: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/GetWebauthnCredentialIDs", { 
            "username": username,
        })

    def GetWebauthnCredentialSummaries(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return self.api_call("Core/GetWebauthnCredentialSummaries", { 
        })

    async def GetWebauthnCredentialSummariesAsync(self, ) -> list:
        """
        Name Description Optional
        :returns: list
        """
        return await self.api_call_async("Core/GetWebauthnCredentialSummaries", { 
        })

    def GetWebserverMetrics(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/GetWebserverMetrics", { 
        })

    async def GetWebserverMetricsAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/GetWebserverMetrics", { 
        })

    def Kill(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/Kill", { 
        })

    async def KillAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/Kill", { 
        })

    def Login(self, username: str, password: str, token: str, rememberMe: bool) -> Any:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :param token: {str}  False
        :param rememberMe: {bool}  False
        :returns: Any
        """
        return self.api_call("Core/Login", { 
            "username": username,
            "password": password,
            "token": token,
            "rememberMe": rememberMe,
        })

    async def LoginAsync(self, username: str, password: str, token: str, rememberMe: bool) -> Any:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :param token: {str}  False
        :param rememberMe: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("Core/Login", { 
            "username": username,
            "password": password,
            "token": token,
            "rememberMe": rememberMe,
        })

    def Logout(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/Logout", { 
        })

    async def LogoutAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/Logout", { 
        })

    def RefreshSettingValueList(self, Node: str) -> Any:
        """
        Name Description Optional
        :param Node: {str}  False
        :returns: Any
        """
        return self.api_call("Core/RefreshSettingValueList", { 
            "Node": Node,
        })

    async def RefreshSettingValueListAsync(self, Node: str) -> Any:
        """
        Name Description Optional
        :param Node: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/RefreshSettingValueList", { 
            "Node": Node,
        })

    def RefreshSettingsSourceCache(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/RefreshSettingsSourceCache", { 
        })

    async def RefreshSettingsSourceCacheAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/RefreshSettingsSourceCache", { 
        })

    def RenameRole(self, RoleId: str, NewName: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :param NewName: {str}  False
        :returns: Any
        """
        return self.api_call("Core/RenameRole", { 
            "RoleId": RoleId,
            "NewName": NewName,
        })

    async def RenameRoleAsync(self, RoleId: str, NewName: str) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :param NewName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/RenameRole", { 
            "RoleId": RoleId,
            "NewName": NewName,
        })

    def ResetUserPassword(self, Username: str, NewPassword: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param NewPassword: {str}  False
        :returns: Any
        """
        return self.api_call("Core/ResetUserPassword", { 
            "Username": Username,
            "NewPassword": NewPassword,
        })

    async def ResetUserPasswordAsync(self, Username: str, NewPassword: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param NewPassword: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/ResetUserPassword", { 
            "Username": Username,
            "NewPassword": NewPassword,
        })

    def Restart(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/Restart", { 
        })

    async def RestartAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/Restart", { 
        })

    def RestartAMP(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/RestartAMP", { 
        })

    async def RestartAMPAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/RestartAMP", { 
        })

    def Resume(self, ) -> None:
        """
     * Allows the service to be re-started after previously being suspended.
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/Resume", { 
        })

    async def ResumeAsync(self, ) -> None:
        """
     * Allows the service to be re-started after previously being suspended.
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/Resume", { 
        })

    def RevokeWebauthnCredential(self, ID: int) -> Any:
        """
        Name Description Optional
        :param ID: {int}  False
        :returns: Any
        """
        return self.api_call("Core/RevokeWebauthnCredential", { 
            "ID": ID,
        })

    async def RevokeWebauthnCredentialAsync(self, ID: int) -> Any:
        """
        Name Description Optional
        :param ID: {int}  False
        :returns: Any
        """
        return await self.api_call_async("Core/RevokeWebauthnCredential", { 
            "ID": ID,
        })

    def RunEventTriggerImmediately(self, triggerId: str) -> Any:
        """
        Name Description Optional
        :param triggerId: {str}  False
        :returns: Any
        """
        return self.api_call("Core/RunEventTriggerImmediately", { 
            "triggerId": triggerId,
        })

    async def RunEventTriggerImmediatelyAsync(self, triggerId: str) -> Any:
        """
        Name Description Optional
        :param triggerId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/RunEventTriggerImmediately", { 
            "triggerId": triggerId,
        })

    def SendConsoleMessage(self, message: str) -> None:
        """
        Name Description Optional
        :param message: {str}  False
        :returns: None
        """
        return self.api_call("Core/SendConsoleMessage", { 
            "message": message,
        })

    async def SendConsoleMessageAsync(self, message: str) -> None:
        """
        Name Description Optional
        :param message: {str}  False
        :returns: None
        """
        return await self.api_call_async("Core/SendConsoleMessage", { 
            "message": message,
        })

    def SetAMPRolePermission(self, RoleId: str, PermissionNode: str, Enabled: bool | None) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :param PermissionNode: {str}  False
        :param Enabled: {bool | None}  False
        :returns: Any
        """
        return self.api_call("Core/SetAMPRolePermission", { 
            "RoleId": RoleId,
            "PermissionNode": PermissionNode,
            "Enabled": Enabled,
        })

    async def SetAMPRolePermissionAsync(self, RoleId: str, PermissionNode: str, Enabled: bool | None) -> Any:
        """
        Name Description Optional
        :param RoleId: {str}  False
        :param PermissionNode: {str}  False
        :param Enabled: {bool | None}  False
        :returns: Any
        """
        return await self.api_call_async("Core/SetAMPRolePermission", { 
            "RoleId": RoleId,
            "PermissionNode": PermissionNode,
            "Enabled": Enabled,
        })

    def SetAMPUserRoleMembership(self, UserId: str, RoleId: str, IsMember: bool) -> Any:
        """
        Name Description Optional
        :param UserId: {str}  False
        :param RoleId: {str}  False
        :param IsMember: {bool}  False
        :returns: Any
        """
        return self.api_call("Core/SetAMPUserRoleMembership", { 
            "UserId": UserId,
            "RoleId": RoleId,
            "IsMember": IsMember,
        })

    async def SetAMPUserRoleMembershipAsync(self, UserId: str, RoleId: str, IsMember: bool) -> Any:
        """
        Name Description Optional
        :param UserId: {str}  False
        :param RoleId: {str}  False
        :param IsMember: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("Core/SetAMPUserRoleMembership", { 
            "UserId": UserId,
            "RoleId": RoleId,
            "IsMember": IsMember,
        })

    def SetConfig(self, node: str, value: str) -> Any:
        """
        Name Description Optional
        :param node: {str}  False
        :param value: {str}  False
        :returns: Any
        """
        return self.api_call("Core/SetConfig", { 
            "node": node,
            "value": value,
        })

    async def SetConfigAsync(self, node: str, value: str) -> Any:
        """
        Name Description Optional
        :param node: {str}  False
        :param value: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/SetConfig", { 
            "node": node,
            "value": value,
        })

    def SetConfigs(self, data: dict[str, str]) -> bool:
        """
        Name Description Optional
        :param data: {dict[str, str]}  False
        :returns: bool
        """
        return self.api_call("Core/SetConfigs", { 
            "data": data,
        })

    async def SetConfigsAsync(self, data: dict[str, str]) -> bool:
        """
        Name Description Optional
        :param data: {dict[str, str]}  False
        :returns: bool
        """
        return await self.api_call_async("Core/SetConfigs", { 
            "data": data,
        })

    def SetTriggerEnabled(self, Id: str, Enabled: bool) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :param Enabled: {bool}  False
        :returns: Any
        """
        return self.api_call("Core/SetTriggerEnabled", { 
            "Id": Id,
            "Enabled": Enabled,
        })

    async def SetTriggerEnabledAsync(self, Id: str, Enabled: bool) -> Any:
        """
        Name Description Optional
        :param Id: {str}  False
        :param Enabled: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("Core/SetTriggerEnabled", { 
            "Id": Id,
            "Enabled": Enabled,
        })

    def Sleep(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/Sleep", { 
        })

    async def SleepAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/Sleep", { 
        })

    def Start(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/Start", { 
        })

    async def StartAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/Start", { 
        })

    def Stop(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/Stop", { 
        })

    async def StopAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/Stop", { 
        })

    def Suspend(self, ) -> None:
        """
     * Prevents the current instance from being started, and stops it if it's currently running.
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/Suspend", { 
        })

    async def SuspendAsync(self, ) -> None:
        """
     * Prevents the current instance from being started, and stops it if it's currently running.
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/Suspend", { 
        })

    def UpdateAMPInstance(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/UpdateAMPInstance", { 
        })

    async def UpdateAMPInstanceAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/UpdateAMPInstance", { 
        })

    def UpdateAccountInfo(self, EmailAddress: str, TwoFactorPIN: str) -> Any:
        """
        Name Description Optional
        :param EmailAddress: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: Any
        """
        return self.api_call("Core/UpdateAccountInfo", { 
            "EmailAddress": EmailAddress,
            "TwoFactorPIN": TwoFactorPIN,
        })

    async def UpdateAccountInfoAsync(self, EmailAddress: str, TwoFactorPIN: str) -> Any:
        """
        Name Description Optional
        :param EmailAddress: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: Any
        """
        return await self.api_call_async("Core/UpdateAccountInfo", { 
            "EmailAddress": EmailAddress,
            "TwoFactorPIN": TwoFactorPIN,
        })

    def UpdateApplication(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("Core/UpdateApplication", { 
        })

    async def UpdateApplicationAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("Core/UpdateApplication", { 
        })

    def UpdateUserInfo(self, Username: str, Disabled: bool, PasswordExpires: bool, CannotChangePassword: bool, MustChangePassword: bool, EmailAddress: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Disabled: {bool}  False
        :param PasswordExpires: {bool}  False
        :param CannotChangePassword: {bool}  False
        :param MustChangePassword: {bool}  False
        :param EmailAddress: {str}  True
        :returns: Any
        """
        return self.api_call("Core/UpdateUserInfo", { 
            "Username": Username,
            "Disabled": Disabled,
            "PasswordExpires": PasswordExpires,
            "CannotChangePassword": CannotChangePassword,
            "MustChangePassword": MustChangePassword,
            "EmailAddress": EmailAddress,
        })

    async def UpdateUserInfoAsync(self, Username: str, Disabled: bool, PasswordExpires: bool, CannotChangePassword: bool, MustChangePassword: bool, EmailAddress: str) -> Any:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Disabled: {bool}  False
        :param PasswordExpires: {bool}  False
        :param CannotChangePassword: {bool}  False
        :param MustChangePassword: {bool}  False
        :param EmailAddress: {str}  True
        :returns: Any
        """
        return await self.api_call_async("Core/UpdateUserInfo", { 
            "Username": Username,
            "Disabled": Disabled,
            "PasswordExpires": PasswordExpires,
            "CannotChangePassword": CannotChangePassword,
            "MustChangePassword": MustChangePassword,
            "EmailAddress": EmailAddress,
        })

    def UpgradeAMP(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("Core/UpgradeAMP", { 
        })

    async def UpgradeAMPAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("Core/UpgradeAMP", { 
        })

    def WebauthnRegister(self, attestationObject: str, clientDataJSON: str, description: str) -> Any:
        """
        Name Description Optional
        :param attestationObject: {str}  False
        :param clientDataJSON: {str}  False
        :param description: {str}  True
        :returns: Any
        """
        return self.api_call("Core/WebauthnRegister", { 
            "attestationObject": attestationObject,
            "clientDataJSON": clientDataJSON,
            "description": description,
        })

    async def WebauthnRegisterAsync(self, attestationObject: str, clientDataJSON: str, description: str) -> Any:
        """
        Name Description Optional
        :param attestationObject: {str}  False
        :param clientDataJSON: {str}  False
        :param description: {str}  True
        :returns: Any
        """
        return await self.api_call_async("Core/WebauthnRegister", { 
            "attestationObject": attestationObject,
            "clientDataJSON": clientDataJSON,
            "description": description,
        })

