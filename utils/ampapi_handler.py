from typing import TypeVar
from ampapi import AMPAPI
import requests
import json
from aiohttp import ClientSession

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
