from .serializer import RefundApplicationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .service import RefundApplicationService
# Create your views here.

class RefundDetail(APIView):
    def get(self,request):
        serializer = RefundApplicationSerializer(request.query_params)
        # serializer.is_valid(raise_exception=True)
        refundapplication = RefundApplicationService.getRefundDetail(pk=serializer.data.refund_id)
        serializer = RefundApplicationSerializer(refundapplication)
        return Response(serializer.data)
    
    def patch(self,request):
        serializer=RefundApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        RefundApplicationService.processRefund(serializer.data.refund_id,serializer.data)
        return Response(serializer.data)

    def post(self,request):
        serializer = RefundApplicationSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        RefundApplicationService.insertRefundDetail(serializer.data)
        return Response(serializer.data)