#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class RCONPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the RCONPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def Dummy(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("RCONPlugin/Dummy", { 
        })

    async def DummyAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("RCONPlugin/Dummy", { 
        })

