from UserService.models import User
from UserService.serializer import UserSerializer
from CommunicationService.models import Message
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    MESSAGE_STATUS = (
        ('read', '已读'),
        ('unread', '未读'),
    )
    
    message_content = serializers.CharField(label="消息内容",allow_null=True)
    message_state = serializers.ChoiceField(label="消息状态",choices=MESSAGE_STATUS,allow_null=True)
    send_time = serializers.DateTimeField(label="发送时间",allow_null=True)
    user = serializers.IntegerField(label="源用户",allow_null=True)
    receive_user = serializers.IntegerField(label="目标用户",allow_null=True)

    def create(self,validated_data):
        return Message.objects.create(**validated_data)

