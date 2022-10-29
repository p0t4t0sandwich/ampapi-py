from dotenv import load_dotenv
import os

from ampapi.ampapi import AMPAPI

load_dotenv()
username = os.getenv("AMP_API_USER")
password = os.getenv("AMP_API_PASSWORD")

def generate_async(spec):
    f = open("async_gen.py","w+")
    for module in spec.keys():
        methods = spec[module]
        for method in methods.keys():
            methodParams = spec[module][method]["Parameters"]
            data = {methodParams[i]["Name"]:methodParams[i]["Name"] for i in range(len(methodParams))}

            data_string = "{"
            for i in range(len(methodParams)):
                data_string += '"' + methodParams[i]["Name"] + '": ' + methodParams[i]["Name"] + ", "
            data_string += "}"

            keys = "self, " + str([i for i in data.keys()]).replace("[","").replace("]","").replace("'","")

            template = f"""    async def {module}_{method}Async({keys}):
        data = {data_string}
        return await self.APICallAsync(endpoint="/{module}/{method}", data=data)\n\n"""
            f.write(template)
    f.close()


def start() -> None:
    API = AMPAPI("http://172.16.1.172:8080")

    # try:
    APIInitOK = API.init()

    if not APIInitOK:
        print("API Init failed")
        return

    loginResult = API.Core.Login(username, password, "", False)

    if "success" in loginResult.keys() and loginResult["success"]:
        print("Login successful")
        API.sessionId = loginResult["sessionID"]

        APIInitOK = API.init()
        if not APIInitOK:
            print("API Stage 2 Init failed")
            return

        # Grab the APISpec
        spec = API.Core.GetAPISpec()["result"]
        generate_async(spec)

    else:
        print("Login failed")
        print(loginResult)

    # except Exception as err:
    #     print(err)

start()
