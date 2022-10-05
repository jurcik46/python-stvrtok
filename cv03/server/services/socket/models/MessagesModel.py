from ast import Num

from cv03.server.services.socket.models.MessagesMetaDataModel import MessagesMetaDataModel


class MessagesModel:
    def __int__(self,pa_messages_meta_data:MessagesMetaDataModel, pa_data:str):
        self.metaData:MessagesMetaDataModel = pa_messages_meta_data
        self.data:str = pa_data



    @staticmethod
    def fromJson( pa_socket_data:object):
        return MessagesModel(pa_socket_data['metaData'], pa_socket_data['data'])
