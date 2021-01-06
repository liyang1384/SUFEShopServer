from UserService.models import User
from CommunicationService.models import Message

class CommunicationService():
    @staticmethod
    def getMessage(receive_user):
        return Message.objects.filter(receive_user=receive_user,message_state="未读")

    @staticmethod
    def insertMessage(validated_data):
        messagedata = validated_data['user','receive_user','message_content']
        Message.objects.create(messagedata)

    @staticmethod
    def countMessage(receive_user):
        return Message.objects.filter(receive_user=receive_user,message_state="未读").count

       