from UserService.models import User
from CommodityService.models import Commodity
from OrderService.models import Order,BuyerReview,SellerReview,PaymentRecord

class OrderService():
    @staticmethod
    def listBoughtOrder(buyer):
        return Order.objects.filter(buyer=buyer)

    @staticmethod
    def listSoldOrder(seller):
        return Order.objects.filter(seller=seller)

    @staticmethod
    def getOrderDetail(order_id):
        return Order.objects.filter(pk=order_id)

    @staticmethod
    def insertOrder(validated_data):
        orderdata = validated_data['commodity_id','seller','buyer','amount']
        neworder = Order.objects.create(orderdata)
        commodity_id = neworder.commodity
        Commodity.objects.update(commodity_id,{'state':'已预定'})

    @staticmethod 
    def payOrder(order_id):
        OrderService.pay(order_id)
        Order.objects.update(order_id,{'order_state':"已付款"})
        paidorder = Order.objects.get(order_id=order_id)
        commodity_id = paidorder.commodity
        Commodity.objects.update(commodity_id,{'state':'已售出'})

    @staticmethod
    def insertPaymentRecord(validated_data):
        paymentRecorddata = validated_data['order_id','payment_platform','payment_type','amount']
        PaymentRecord.objects.create(paymentRecorddata)
        
    @staticmethod
    def pay(order_id):
        pass
    
    @staticmethod
    def insertSellerReview(validated_data):
        sellerreviewdata = validated_data['order_id','commodity_quality','deal_speed','seller_attitude','comment']
        SellerReview.objects.create(sellerreviewdata)

    @staticmethod
    def insertBuyerReview(validated_data):
        buyerreviewdata = validated_data['order_id','score','comment']
        BuyerReview.objects.create(buyerreviewdata)

    @staticmethod
    def updateOrderState(order_id):
        Order.objects.update(order_id,{'order_state':"已收货"})