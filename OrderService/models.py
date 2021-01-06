from django.db import models
from datetime import datetime
from UserService.models import User
from CommodityService.models import Commodity

# Create your models here.
class OrderManager(models.Manager):
    
    def create(self,validated_data):
        return super().create(**validated_data)
    
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.amount = validated_data.get('amount',instance.amount)
        instance.order_state = validated_data.get('order_state',instance.order_state)
        instance.order_time = validated_data.get('order_time',instance.order_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance


class BuyerReviewManager(models.Manager):
    
    def create(self,validated_data):
        return super().create(**validated_data)
    
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.score = validated_data.get('score',instance.score)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.review_time = validated_data.get('review_time',instance.review_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance

    def delete(self,pk):
        instance = super().get(pk=pk)
        instance.if_delete = True
        instance.save()
        return instance


class SellerReviewManager(models.Manager):
    
    def create(self,validated_data):
        return super().create(**validated_data)
    
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.commodity_quality = validated_data.get('commodity_quality',instance.commodity_quality)
        instance.deal_speed = validated_data.get('deal_speed',instance.deal_speed)
        instance.seller_attitude = validated_data.get('seller_attitude',instance.seller_attitude)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.review_time = validated_data.get('review_time',instance.review_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance

    def delete(self,pk):
        instance = super().get(pk=pk)
        instance.if_delete = True
        instance.save()
        return instance


class PaymentRecordManager(models.Manager):
    
    def create(self,validated_data):
        return super().create(**validated_data)
    
    def update(self,pk,validated_data):
        instance = super().get(pk=pk)
        instance.amount = validated_data.get('amount',instance.amount)
        instance.payment_type = validated_data.get('payment_type',instance.payment_type)
        instance.payment_platform = validated_data.get('payment_platform',instance.payment_platform)
        instance.payment_time = validated_data.get('payment_time',instance.payment_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance

    def delete(self,pk):
        instance = super().get(pk=pk)
        instance.if_delete = True
        instance.save()
        return instance


class Order(models.Model):
    ORDER_STATUS = (
        ("paying", "待付款"),
        ("paid", "已付款"),
        ("received", "已收货"),
        ("refunded", "已退款"),
        ("cancelled", "已取消"),
    )

    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, verbose_name="商品")
    seller = models.ForeignKey(User, on_delete=models.CASCADE,related_name='seller', verbose_name="卖家")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='buyer', verbose_name="买家")
    order_id = models.AutoField(primary_key=True)
    amount = models.FloatField(default=0, verbose_name="订单金额")
    order_state = models.CharField(choices=ORDER_STATUS, default="待付款", max_length=30, verbose_name="订单状态")
    order_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True, verbose_name="下单时间")
    if_delete = models.BooleanField(default=False)
    objects = OrderManager()

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_id)


class BuyerReview(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单")
    buyer_review_id = models.AutoField(primary_key=True)
    score = models.IntegerField(default=0, verbose_name="综合评分")
    comment = models.TextField(default="", max_length=200, verbose_name="文字评价")
    review_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True, verbose_name="评价时间")
    if_delete = models.BooleanField(default=False)
    objects = BuyerReviewManager()

    class Meta:
        verbose_name = "对买家的评价"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.comment)


class SellerReview(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单")
    seller_review_id = models.AutoField(primary_key=True)
    commodity_quality = models.IntegerField(default=0, verbose_name="商品质量")
    deal_speed = models.IntegerField(default=0, verbose_name="交易速度")
    seller_attitude = models.IntegerField(default=0, verbose_name="卖家态度")
    comment = models.TextField(default="", max_length=200, verbose_name="文字评价")
    review_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True, verbose_name="评价时间")
    if_delete = models.BooleanField(default=False)
    objects = SellerReviewManager()

    class Meta:
        verbose_name = "对卖家的评价"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.comment)


class PaymentRecord(models.Model):
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

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单")
    payment_id = models.AutoField(primary_key=True)
    amount = models.FloatField(default=0, verbose_name="支付金额")
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=30, verbose_name="支付类型")
    payment_platform = models.CharField(choices=PAYMENT_PLATFORM, max_length=20, verbose_name="支付平台")
    payment_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True, verbose_name="支付时间")
    if_delete = models.BooleanField(default=False)
    objects = PaymentRecordManager()

    class Meta:
        verbose_name = "支付记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.payment_id)
