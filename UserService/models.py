from django.db import models
# Create your models here.
#用户
class UserManager(models.Manager):
    
    def create(self,validated_data):
        return super().create(**validated_data)

    
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.nick_name = validated_data.get('nick_name',instance.nick_name)
        instance.password = validated_data.get('password',instance.password)
        instance.avator = validated_data.get('avator',instance.avator)
        instance.real_name = validated_data.get('real_name',instance.real_name)
        instance.sex = validated_data.get('sex',instance.sex)
        instance.mobile = validated_data.get('mobile',instance.mobile)
        instance.email = validated_data.get('email',instance.email)
        instance.account_state = validated_data.get('account_state',instance.account_state)
        instance.online_state = validated_data.get('online_state',instance.online_state)
        instance.identity = validated_data.get('identity',instance.identity)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance
    
    # def find(self,query_criteria):
    #     return super().filter(**query_criteria)
    
    # def find_one(self,pk):
    #     return super().get(pk=pk)

class User(models.Model):
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
    user_id = models.AutoField(primary_key=True,unique=True)
    user_name = models.CharField(max_length=30,unique=True)
    nickname = models.CharField(max_length=30,default = 'new_user')
    password = models.CharField(max_length=20)
    avatar  = models.ImageField()
    real_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6,choices=SEX_CHOICES)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    account_state = models.CharField(choices=ACCOUNT_STATE_CHOICES,max_length=20)
    credit_score = models.IntegerField(default=80)
    online_state = models.CharField(choices=ONLINE_STATE_CHOICES,max_length=20)
    identity = models.CharField(choices=IDENTITY_CHOICES,default='USER',max_length=20)
    if_delete = models.BooleanField(default=False)
    objects = UserManager()
    
