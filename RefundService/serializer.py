from rest_framework import serializers
from .models import RefundApplication

class RefundApplicationSerializer(serializers.Serializer):
    
    REFUND_STATE_CHOICES =(
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','同意退款'),
        ('REJECTED','拒绝退款'),
    )
    refund_id = serializers.IntegerField(label='退款申请ID',allow_null=True,required=False)
    refund_state = serializers.ChoiceField(choices=REFUND_STATE_CHOICES,label='退款状态',allow_null=True,required=False)
    refund_reason = serializers.CharField(label='退款理由',allow_null=True,required=False)
    refund_time = serializers.DateTimeField(label='退款时间',allow_null=True,required=False)
    order = serializers.CharField(label='订单编号',allow_null=True,required=False)
    # if_delete = serializers.BooleanField(label='是否删除')
    def create(self,validated_data):
        return RefundApplication.objects.create(**validated_data)

# refund_id = models.AutoField(primary_key=True)
#     refund_state = models.CharField(choices=REFUND_STATE_CHOICES)
#     refund_apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
#     refund_reason = models.CharField(max_length=20)
#     refund_time = models.DateTimeField(auto_now=False, auto_now_add=False)
#     '''！！！外键引用有可能出现问题！！！'''
#     order = models.ForeignKey("OrderService.Order",to_field='order_id',on_delete=models.CASCADE)