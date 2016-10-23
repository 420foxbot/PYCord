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
            'authorization': "Bot " + self.token,
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        conn.request("POST", "/api/channels/{}/messages".format(id), json.dumps(payload), headers)
