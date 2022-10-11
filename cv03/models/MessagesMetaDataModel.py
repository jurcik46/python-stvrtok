from constants import SocketOperationEnum
from datetime import datetime as d, datetime


class MessagesMetaDataModel:
    def __init__(self, pa_operation: SocketOperationEnum, pa_user_name:str, pa_send_time:datetime, pa_received_time:datetime):
        self.operation: SocketOperationEnum = pa_operation
        self.user_name = pa_user_name
        self.send_time:datetime = pa_send_time
        self.received_time:datetime = pa_received_time

    @staticmethod
    def from_json(pa_socket_data:object):
        return MessagesMetaDataModel(pa_socket_data['operation'],pa_socket_data['user_name'], pa_socket_data['send_time'], pa_socket_data['received_time'])

