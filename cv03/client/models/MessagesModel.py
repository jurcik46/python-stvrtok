from cv03.server.models.MessagesMetaDataModel import MessagesMetaDataModel


class MessagesModel:
    def __int__(self,pa_messages_meta_data:MessagesMetaDataModel, pa_data:str):
        self.metaData:MessagesMetaDataModel = pa_messages_meta_data
        self.data:str = pa_data



    @staticmethod
    def from_json( pa_socket_data:object):
        return MessagesModel(pa_socket_data['metaData'], pa_socket_data['data'])
