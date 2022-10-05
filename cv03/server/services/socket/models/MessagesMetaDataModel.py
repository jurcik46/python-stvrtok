from cv03.server.services.socket.constants import SocketOperationEnum
from datetime import datetime as d, datetime


class MessagesMetaDataModel:

    def __int__(self, pa_operation:SocketOperationEnum,pa_send_time:datetime):
        self.operation:SocketOperationEnum = pa_operation
        self.send_time:datetime = pa_send_time
        self.received_time:datetime = d.now()

    @staticmethod
    def fromJson(pa_socket_data:object):
        return MessagesMetaDataModel(pa_socket_data['operation'], pa_socket_data['send_time'], pa_socket_data['received_time'])

