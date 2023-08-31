#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from __future__ import annotations
from typing import Any, TypeVar

import requests
import json

from aiohttp import ClientSession

class AMPAPI():
    """Class for interacting with the AMP API"""
    def __init__(self, baseUri: str, username: str, password: str, rememberMeToken: str = "", sessionId: str = "") -> None:
        """Initializes the AMP API class
        :param baseUri: The base URI of the AMP instance
        :type baseUri: str
        :returns: None
        """
        self.baseUri = baseUri

        # Check if the baseUri ends with a slash
        if not self.baseUri[-1] == "/":
            self.baseUri += "/"
        self.dataSource = self.baseUri + "API"

        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    def api_call(self, endpoint: str, data: dict = {}) -> dict:
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

    async def api_call_async(self, endpoint: str, data: dict = {}) -> dict:
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

    def Login(self) -> dict:
        """
        Simplified login function
        :returns: dict with the result of the login
        """
        data: dict = {
            "username": self.username,
            "password": self.password,
            "token": self.rememberMeToken,
            "rememberMe": True,
        }

        loginResult: dict = self.api_call("Core/Login", data)

        if "success" in loginResult.keys() and loginResult["success"] == True:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]

        return loginResult

    async def LoginAsync(self) -> dict:
        """
        Simplified login function
        :returns: dict with the result of the login
        """
        data: dict = {
            "username": self.username,
            "password": self.password,
            "token": self.rememberMeToken,
            "rememberMe": True,
        }

        loginResult: dict = await self.api_call_async("Core/Login", data)

        if "success" in loginResult.keys() and loginResult["success"] == True:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]

        return loginResult
