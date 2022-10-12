

from pydoc import cli
from ClientConfig import ClientConfig
from MessageModel import MessageModel
from ActionsEnum import ActionsEnum 
import socket
import json

from ClientConfig import ClientConfig
from ClientMenuActionsEnum import ClientMenuActionsEnum


def menu():
    print("***Menu***")
    print(f"Exit Program ({ClientMenuActionsEnum.EXIT_PROGRAM.value})")
    print(f"Show users ({ClientMenuActionsEnum.SHOW_USERS.value})")
    print(f"Send massage ({ClientMenuActionsEnum.SEND_MESSAGE.value})")
    
client_config = ClientConfig()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_config.server_ip_address, client_config.server_port))

print("Wellcome")
user_name = input("Enter your nick: ")

msg = MessageModel(user_name, "", "", ActionsEnum.LOGIN)
json_str = json.dumps(msg.__dict__)
client_socket.send(json_str.encode())



while(True):

    menu()
    action = input("Chose operation from menu:")
    print("------ Start Result -------")

    if action is ClientMenuActionsEnum.EXIT_PROGRAM.value :
        msg = MessageModel(user_name,"","", ActionsEnum.EXIT)
        json_str = json.dumps(msg.__dict__)
        client_socket.send(json_str.encode())
        client_socket.close()
        exit(0)
    if action is ClientMenuActionsEnum.SHOW_USERS.value :
        msg = MessageModel(user_name,"","", ActionsEnum.USERS)
        json_str = json.dumps(msg.__dict__)
        client_socket.send(json_str.encode())
        data =  client_socket.recv(1500)
        msg = json.loads(data.decode(), object_hook=MessageModel.from_json)
        print(f"User list: {msg.text}")
    if action is ClientMenuActionsEnum.SEND_MESSAGE.value :
        text = input("Massage: ")
        to_user = input("To user:")
        msg = MessageModel(user_name,to_user,text, ActionsEnum.USERS)
        json_str = json.dumps(msg.__dict__)
        client_socket.send(json_str.encode())

    print("------ End Result -------")

    
        
    
    

