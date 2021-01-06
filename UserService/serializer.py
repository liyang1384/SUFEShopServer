from rest_framework import serializers
from .models import User
class UserSerializer(serializers.Serializer):
    SEX_CHOICES = (
        ('MALE','男性'),
        ('FEMALE','女性'),
    )    
    ACCOUNT_STATE_CHOICES = (
        ('AVAILABLE','可用'),
        ('DISABLE','禁用'),
    )
    ONLINE_STATE_CHOICES = (
        ('ONLINE','在线'),
        ('OFFLINE','离线'),
    )
    IDENTITY_CHOICES = (
        ('USER','用户'),
        ('ADMINISTRATOR','管理员'),
    )
    IDENTITY_CHOICES = (
        ('USER','用户'),
        ('ADMINISTRATOR','管理员'),
    )
    user_id = serializers.IntegerField(label='用户ID',allow_null=True,required=False)
    user_name = serializers.CharField(max_length=30,label='用户名',allow_null=True,required=False)
    password = serializers.CharField(max_length=20,label='密码',allow_null=True,required=False)
    nickname = serializers.CharField(max_length=30,label='用户昵称',allow_null=True,required=False)
    avatar = serializers.ImageField(label='头像',allow_null=True,required=False)
    real_name = serializers.CharField(max_length=30,label='真实姓名',allow_null=True,required=False)
    sex = serializers.ChoiceField(choices=SEX_CHOICES,label='性别',allow_null=True,required=False)
    mobile = serializers.CharField(max_length=11,min_length=11,label='手机号码',allow_null=True,required=False)
    email = serializers.EmailField(label='邮箱地址',allow_null=True,required=False)
    online_state = serializers.ChoiceField(choices=ONLINE_STATE_CHOICES,label='在线状态',allow_null=True,required=False)
    identity = serializers.ChoiceField(choices=IDENTITY_CHOICES,label='身份',allow_null=True,required=False)
# user_id = models.AutoField(primary_key=True,unique=True)
#     user_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
#     avatar  = models.ImageField()
#     real_name = models.CharField(max_length=30)
#     sex = models.CharField(max_length=1,choices=SEX_CHOICES)
#     mobile = models.CharField(max_length=11)
#     email = models.EmailField()
#     account_state = models.CharField(choices=ACCOUNT_STATE_CHOICES)
#     credit_score = models.IntegerField()
#     online_state = models.CharField(choices=ONLINE_STATE_CHOICES)
#     identity = models.CharField()

    def create(self,validated_data):
        return User.objects.create(**validated_data)

