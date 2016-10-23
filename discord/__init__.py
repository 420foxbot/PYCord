import requests
import json
baseurl = "https://discordapp.com/api/"

class Client:
    """A Discord Client"""

    def __init__(self,token):
        self.token = token

    def sendMessage(self,id,content,tts : bool = False):
        payload = {
            "content":content,
            "tts":tts
        }

        headers = {
            'authorization': "Bot " + self.token,
            'content-type': "application/json",
            'cache-control': "no-cache"
            "user-agent":"DiscordBot (https://github.com/developerCodex/PYCord, 1.2.1)"
        }
        url = baseurl+"channels/{}".format(id)
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.text

    def getMessage(self,channel,messageid):
        payload = {}
        headers = {
            'authorization': "Bot " + self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
            "user-agent":"DiscordBot (https://github.com/developerCodex/PYCord, 1.2.1)"
        }
        url = baseurl+"channels/{}/messages/{}".format(channel,messageid)
        response = requests.request("GET", url, data=json.dumps(payload), headers=json.dumps(headers))
        return response.text
