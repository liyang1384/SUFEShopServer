from .models import RefundApplication
import sys
sys.path.append("..")
from OrderService.models import Order
class RefundApplicationService():
    @staticmethod
    def getRefundDetail(pk):
        return RefundApplication.objects.get(pk=pk)
    @staticmethod
    def processRefund(pk,validated_data):
        refundapplication = RefundApplication.objects.get(pk=pk)
        order_pk = refundapplication.order
        order = Order.objects.get(pk = order_pk)
        refunder = order.seller
        refundee = order.buyer
        RefundApplicationService.refund(refunder,refundee)
        RefundApplication.objects.update(pk=pk,validated_data=validated_data)
    @staticmethod
    def insertRefundDetail(validated_data):
        RefundApplication.objects.create(validated_data)
    @staticmethod
    def refund(refunder,refundee):
        pass

