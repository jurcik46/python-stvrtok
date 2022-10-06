from ast import arg
from MessageModel import MessageModel
from ActionsEnum import ActionsEnum

import socket
import threading
import json

from ServerConfig import ServerConfig

users = list()

def handle_client(pa_client_socket, pa_client_address):
    while(True):
        data = pa_client_socket.recv(1500)
        print(data)
        msg = json.loads(data.decode(), object_hook=MessageModel.from_json)
        match msg.action:
            case ActionsEnum.LOGIN:
                users.append(msg.from_user)
                print(f"User {msg.from_user} are log in. IP: {pa_client_address[0]}:{pa_client_address[1]} ")
                continue
            case ActionsEnum.EXIT:
                users.remove(msg.from_user)
                print(f"User {msg.from_user}  loget out. IP: {pa_client_address[0]}:{pa_client_address[1]} ")
                pa_client_socket.close()
                return
            case ActionsEnum.USERS:
                 msg_to_user = MessageModel("Server","", users, ActionsEnum.USERS)
                 json_str = json.dumps(msg_to_user.__dict__)
                 pa_client_socket.send(json_str)
                 continue
        print(f"Massage {pa_client_address[0]}:{pa_client_address[1]}, from {msg.from_user} to {msg.to_user}, text: {msg.text}")
            
 


server_config = ServerConfig()

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((server_config.ip_address, server_config.port))

server_socket.listen(10)

print(f"Server is running on IP {server_config.ip_address}:{server_config.port}")



while(True):
    (client_socket, client_address) = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
    



