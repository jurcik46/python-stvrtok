
import socket
from enum import IntEnum
import threading
import json

class SocketService:
    def __int__(self, pa_ip_address:str, pa_port:int):
        self._ip_address:str =pa_ip_address
        self._pa_port:int = pa_port
        self.running:bool = True


    def run_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self._ip_address, self._pa_port))
        sock.listen(10)
        while self.running:
            (clientSock, clientAddr) = sock.accept()
            thread = threading.Thread(target=self._handle_socket, args=(clientSock, clientAddr))
            thread.start()


    def _handle_socket(self,pa_client_socket, pa_client_add):
        while(True):
            data = pa_client_socket.recv(1500)
            sprava = json.loads(data.decode(), object_hook=Sprava.jsonParser)




