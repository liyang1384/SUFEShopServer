from django.db import models

# 商品管理器
class CommodityManager(models.Manager):
    def create(self,validated_data):
        return super().create(**validated_data)
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.commodity_name = validated_data.get('commodity_name',instance.commodity_name)
        instance.commodity_type = validated_data.get('commodity_type',instance.commodity_type)
        instance.commodity_picture = validated_data.get('commodity_picture',instance.commodity_picture)
        instance.price =validated_data.get('price',instance.price)
        instance.detail = validated_data.get('detail',instance.detail)
        instance.state = validated_data.get('state',instance.state)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance
class CommodityApplicationManager(models.Manager):
    def create(self,validated_data):
        return super().create(**validated_data)
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.commodity = validated_data.get('commodity',instance.commodity)
        instance.application_state = validated_data.get('application_state',instance.application_state)
        instance.auditor = validated_data.get('auditor',instance.auditor)
        instance.audit_time = validated_data.get('audit_time',instance.audit_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance

class BrowserHisoryManager(models.Manager):
    def create(self,validated_data):
        return super().create(**validated_data)
    def delete(self,pk):
        instance = super().get(pk=pk)
        instance.if_delete = True
        instance.save()
        return instance

#商品
class Commodity(models.Model):
    STATE_CHOICES = (
    ('TO_BE_REVIEWED','待审核'),
    ('REJECTED','未通过'),
    ('ON_THE_SHELVES','已上架'),
    ('RESERVED','已预定'),
    ('SALED','已售出'),
    ('DELETED','已删除'),
    )
    commodity_id = models.AutoField(primary_key=True)
    commodity_name = models.CharField(max_length=50)
    commodity_type = models.CharField( max_length=20)
    commodity_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    detail = models.TextField()
    on_shelf_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    state = models.CharField(choices=STATE_CHOICES,max_length=20,default='TO_BE_REVIEWED')
    if_delete = models.BooleanField(default=False)
    objects = CommodityManager()

#申请记录
class CommodityApplication(models.Model):
    APPLICATION_STATE_CHOICES = (
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','审核通过'),
        ('REJECTED','审核未通过'),
    )
    application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("UserService.User",related_name='applier',to_field='user_id',on_delete=models.CASCADE)
    Commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
    apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    application_state = models.CharField(choices=APPLICATION_STATE_CHOICES,max_length=20,default='TO_BE_REVIEWED')
    auditor = models.ForeignKey("UserService.User",related_name='auditor',to_field='user_id',on_delete=models.CASCADE,blank=True)
    audit_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    if_delete = models.BooleanField(default=False)
    # commodity = models.OneToOneField("Commodity")
    objects = CommodityApplicationManager()

#浏览记录
class BrowserHisory(models.Model):
    browser_history_id = models.AutoField(primary_key=True)
    commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
    user = models.ForeignKey("UserService.User",to_field='user_id', on_delete=models.CASCADE)
    browse_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    if_delete = models.BooleanField(default=False)
    objects = BrowserHisoryManager()
