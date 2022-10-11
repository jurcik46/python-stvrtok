import socket
from enum import IntEnum
import json
from datetime import datetime as d, datetime
from configClient import ClientConfig
from constants.SocketOperationEnum import SocketOperationEnum
from models.MessagesMetaDataModel import MessagesMetaDataModel
from models.MessagesModel import MessagesModel
import jsonpickle
client_config = ClientConfig()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client_config.server_ip_address)
print(client_config.server_port)
sock.connect((client_config.server_ip_address, client_config.server_port))

msg = MessagesModel(MessagesMetaDataModel(SocketOperationEnum.ADD_MOVIE, client_config.user_name, d.now(), d.now()),"sadasdasd")
# print( jsonpickle.encode(msg))
# jsonStr =jsonpickle.encode(msg)
jsonStr = json.dumps(msg, default=lambda o: o.__dict__, indent=4)
sock.send(jsonStr.encode())