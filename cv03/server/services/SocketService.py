
import socket
import threading
import json

from constants.SocketOperationEnum import SocketOperationEnum
from models.MessagesModel import MessagesModel


class SocketService:
    def __int__(self, pa_ip_address, pa_port):
        self._ip_address = pa_ip_address
        self._pa_port = pa_port
        self.running = True


    def run_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self._ip_address, self._pa_port))
        sock.listen(10)
        while self.running:
            (clientSock, clientAddr) = sock.accept()
            thread = threading.Thread(target=self._handle_socket, args=(clientSock, clientAddr))
            thread.start()


    @staticmethod
    def _handle_socket(pa_client_socket, pa_client_add):
        while(True):
            data = pa_client_socket.recv(1500)
            message = json.loads(data.decode(), object_hook=MessagesModel.from_json)
            print(message)
            if message.metaData.operation == SocketOperationEnum.ADD_MOVIE:
                print("add move")
            if message.metaData.operation == SocketOperationEnum.REMOVE_MOVIE:
                print("remove move")
            if message.metaData.operation == SocketOperationEnum.REMOVE_MOVIE:
                print("Client disconnected: {}:{}, nick: {}".format(pa_client_add[0], pa_client_add[1], message.metaData.user_name))
                print("exit")
            if message.metaData.operation == SocketOperationEnum.SHUT_DOWN:
                print("Client disconnected: {}:{}, nick: {}".format(pa_client_add[0], pa_client_add[1], message.metaData.user_name))
                print("Showt Down Server")






