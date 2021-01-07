from .serializer import RefundApplicationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .service import RefundApplicationService
from utils import delete_null
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.

class RefundDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request):
        serializer = RefundApplicationSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # refundapplication = RefundApplicationService.getRefundDetail(pk=serializer.data.get('refund_id'))
        # serializer = RefundApplicationSerializer(refundapplication)
        # return Response(serializer.data)
        return Response(serializer.data)
    
    def patch(self,request):
        serializer=RefundApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validate_data = delete_null(serializer.data)
        RefundApplicationService.processRefund(serializer.data.get('refund_id'),validate_data)
        return Response(serializer.data)

    def post(self,request):
        serializer = RefundApplicationSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        validate_data = delete_null(serializer.data)
        RefundApplicationService.insertRefundDetail(validate_data)
        return Response(serializer.data)