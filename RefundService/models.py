from django.db import models

# Create your models here.
class RefundApplicationManager(models.Manager):
    def create(self,validated_data):
        return super().create(**validated_data)

    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.refund_state = validated_data.get('refund_state',instance.refund_state)
        instance.refund_reason = validated_data.get('refund_reason',instance.refund_reason)
        instance.refund_time = validated_data.get('refund_time',instance.refund_time)
        instance.order = validated_data.get('order',instance.order)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance
    
    def all(self):
        return super().filter(if_delete=False)


#退款记录
class RefundApplication(models.Model):
    REFUND_STATE_CHOICES =(
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','同意退款'),
        ('REJECTED','拒绝退款'),
    )
    refund_id = models.AutoField(primary_key=True)
    refund_state = models.CharField(choices=REFUND_STATE_CHOICES,default='TO_BE_REVIEWED',max_length=20)
    refund_apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    refund_reason = models.TextField()
    refund_time = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True)
    '''！！！外键引用有可能出现问题！！！'''
    order = models.ForeignKey("OrderService.Order",to_field='order_id',on_delete=models.CASCADE)
    if_delete = models.BooleanField(default=False)
    objects = RefundApplicationManager()