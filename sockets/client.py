

from pydoc import cli
from ClientConfig import ClientConfig
from MessageModel import MessageModel
from ActionsEnum import ActionsEnum 
import socket
import json

from ClientConfig import ClientConfig


def menu():
    print("***Menu***")
    print("Exit Program (1)")
    print("Show users (2)")
    print("Send massage (3)")
    
client_config = ClientConfig()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_config.server_ip_address, client_config.server_port))

print("Wellcome")
user_name = input("Enter your nick: ")
menu()

msg = MessageModel(user_name, "", "", ActionsEnum.LOGIN)
json_str = json.dumps(msg.__dict__)
client_socket.send(json_str.encode())



while(True):
    action = input("Chose operation from menu:")
    
    match action:
        case "1":
            msg = MessageModel(user_name,"","", ActionsEnum.EXIT)
            json_str = json.dumps(msg.__dict__)
            client_socket.send(json_str.encode())
            client_socket.close()
            exit(0)
        case "2":
            msg = MessageModel(user_name,"","", ActionsEnum.USERS)
            json_str = json.dumps(msg.__dict__)
            client_socket.send(json_str.encode())
            data =  client_socket.recv(1500)
            msg = json.loads(data.decode(), object_hook=MessageModel.from_json)
            print(f"User list: {msg.text}")
            continue
        case "3":
            text = input("Massage: ")
            to_user = input("To user:") 
            msg = MessageModel(user_name,to_user,text, ActionsEnum.USERS)
            json_str = json.dumps(msg.__dict__)
            client_socket.send(json_str.encode())
            
        
    
        
    
    

