from UserService.models import User
from UserService.serializer import UserSerializer
from CommodityService.models import Commodity
from CommodityService.serializer import CommoditySerializer
from OrderService.models import Order,BuyerReview,SellerReview,PaymentRecord
from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    ORDER_STATUS = (
        ("paying", "待付款"),
        ("paid", "已付款"),
        ("refunded", "已退款"),
        ("cancelled", "已取消"),
    )

    order_id = serializers.IntegerField(label='订单ID',allow_null=True,required=False)
    #commodity_id = serializers.IntegerField(label="商品ID",allow_null=True,required=False)
    #seller = serializers.IntegerField(label="卖家",allow_null=True,required=False)
    #buyer = serializers.IntegerField(label="买家",allow_null=True,required=False)
    amount = serializers.FloatField(label="订单金额",allow_null=True,required=False)
    order_state = serializers.ChoiceField(choices=ORDER_STATUS, label="订单状态",allow_null=True,required=False)
    order_time = serializers.DateTimeField(label="下单时间",allow_null=True,required=False)
    commodity = CommoditySerializer(required=False)
    seller = UserSerializer(required=False)
    buyer = UserSerializer(required=False)

    def create(self,validated_data):
        return Order.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return Order.objects.update(pk,validated_data)


class BuyerReviewSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(label="订单ID",allow_null=True,required=False)
    score = serializers.IntegerField(label="综合评分",allow_null=True,required=False)
    comment = serializers.CharField(label="文字评价",allow_null=True,required=False)
    review_time = serializers.DateTimeField(label="评价时间",allow_null=True,required=False)

    def create(self,validated_data):
        return BuyerReview.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return BuyerReview.objects.update(pk,validated_data)


class SellerReviewSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(label="订单ID",allow_null=True,required=False)
    commodity_quality = serializers.IntegerField(label="商品质量",allow_null=True,required=False)
    deal_speed = serializers.IntegerField(label="交易速度",allow_null=True,required=False)
    seller_attitude = serializers.IntegerField(label="卖家态度",allow_null=True,required=False)
    comment = serializers.CharField(label="文字评价",allow_null=True,required=False)
    review_time = serializers.DateTimeField(label="评价时间",allow_null=True,required=False)

    def create(self,validated_data):
        return SellerReview.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return SellerReview.objects.update(pk,validated_data)


class PaymentRecordSerializer(serializers.Serializer):
    PAYMENT_TYPE = (
        ("B2P", "买家付款给平台"),
        ("P2S", "平台付款给卖家"),
        ("S2B", "卖家退款给买家"),
        ("P2B", "平台退款给买家"),
    )

    PAYMENT_PLATFORM = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )

    #order_id = serializers.IntegerField(label="订单ID",allow_null=True,required=False)
    payment_id = serializers.IntegerField(label="支付记录ID",allow_null=True,required=False)
    amount = serializers.FloatField(label="支付金额",allow_null=True,required=False)
    payment_type = serializers.ChoiceField(choices=PAYMENT_TYPE, label="支付类型",allow_null=True,required=False)
    payment_platform = serializers.ChoiceField(choices=PAYMENT_PLATFORM, label="支付平台",allow_null=True,required=False)
    payment_time = serializers.DateTimeField(label="支付时间",allow_null=True,required=False)
    order = OrderSerializer(required=False)

    def create(self,validated_data):
        return PaymentRecord.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return PaymentRecord.objects.update(pk,validated_data)