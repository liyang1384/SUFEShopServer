from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from OrderService.service import OrderService
from OrderService.serializer import OrderSerializer,BuyerReviewSerializer,SellerReviewSerializer,PaymentRecordSerializer

# Create your views here.
class OrderDetail(APIView):
    def get(self, request):
        serializer = OrderSerializer(request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = OrderService.getOrderDetail(order_id=serializer.data.order_id)
        serializer = OrderSerializer(instance)
        return Response(serializer.data)


class BoughtOrderList(APIView):
    def get(self, request):
        serializer = OrderSerializer(request.query_params)
        serializer.is_valid(raise_exception=True)
        query_set = OrderService.listBoughtOrder(serializer.data.buyer)
        serializer = OrderSerializer(query_set,many=True)
        return Response(serializer.data)


class SoldOrderList(APIView):
    def get(self, request):
        serializer = OrderSerializer(request.query_params)
        serializer.is_valid(raise_exception=True)
        query_set = OrderService.listSoldOrder(serializer.data.seller)
        serializer = OrderSerializer(query_set,many=True)
        return Response(serializer.data)


class BuyerReviewDetail(APIView):
    def post(self, request):
        serializer = BuyerReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertBuyerReview(serializer.data)
        return Response(serializer.data)


class SellerReviewDetail(APIView):
    def post(self, request):
        serializer = SellerReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertSellerReview(serializer.data)
        return Response(serializer.data)
    

class PayOrderDetail(APIView):
    def post(self, request):
        serializer = PaymentRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.payOrder(serializer.data.order_id)
        OrderService.insertPaymentRecord(serializer.data)
        return Response(serializer.data)


class GenerateOrderDetail(APIView):
    def post(self, request):
        serializer=OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertOrder(serializer.data)
        return Response(serializer.data)
   

