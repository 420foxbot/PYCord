var request = require("request")
var baseurl = "https://discordapp.com/api/"

class Client {

function sendMessage(channel,content){
var options = { method: 'POST',
  url: baseurl+"channels/"+channel+"/messages,
  headers: 
   {
     'cache-control': 'no-cache',
     'content-type': 'application/json',
     authorization: 'Bot '+this.token },
  body: { content: content },
  json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error)
});
}

}
  
