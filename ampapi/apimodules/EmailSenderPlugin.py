#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class EmailSenderPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the EmailSenderPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def TestSMTPSettings(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return self.api_call("EmailSenderPlugin/TestSMTPSettings", { 
        })

    async def TestSMTPSettingsAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        return await self.api_call_async("EmailSenderPlugin/TestSMTPSettings", { 
        })

