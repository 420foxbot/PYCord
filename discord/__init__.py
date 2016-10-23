import http.client
import json
conn = http.client.HTTPSConnection("discordapp.com")

class Client:
    """A Discord Client"""

    def __init__(self,token):
        self.token = token
    def sendMessage(self,id,content):
        payload = {
            "content":content
        }

        headers = {
            'authorization': self.token,
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        conn.request("POST", "/api/channels/112233445566778899/messages", json.dumps(payload), headers)

        data = conn.getresponse()
        res = data.read()
        print(res)
