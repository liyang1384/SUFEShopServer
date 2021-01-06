from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from OrderService.service import OrderService
from OrderService.serializer import OrderSerializer,BuyerReviewSerializer,SellerReviewSerializer,PaymentRecordSerializer
from utils import delete_null
from rest_framework import status

# Create your views here.
class OrderDetail(APIView):
    def get(self, request):
        serializer = OrderSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = OrderService.getOrderDetail(order_id=serializer.data)
        serializer = OrderSerializer(instance)
        return Response(serializer.data)


class OrderList(APIView):
    def get(self, request):
        qurey_params = request.query_params.copy()
        min_amount = qurey_params.get('min_amount')
        max_amount = qurey_params.get('max_amount')
        qurey_params.pop('min_amount')
        qurey_params.pop('max_amount')
        serializer = OrderSerializer(data=qurey_params)
        serializer.is_valid(raise_exception=True)
        query_criteria = serializer.data
        delete_null(query_criteria)
        query_criteria.update({'amount__gte': min_amount,'amount__lte': max_amount})
        if query_criteria.order_type == 0:
            query_set = OrderService.listBoughtOrder(query_criteria.user_id)
        else:
            query_set = OrderService.listSoldOrder(query_criteria.user_id)
        serializer = OrderSerializer(query_set,many=True)
        return Response(serializer.data)


class BuyerReviewDetail(APIView):
    def post(self, request):
        serializer = BuyerReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertBuyerReview(serializer.data)
        return Response(serializer.data)


class SellerReviewDetail(APIView):
    def get(self, request):
        serializer = OrderSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = OrderService.getOrderDetail(order_id=serializer.data.order_id)
        serializer = OrderSerializer(instance)
        return Response(serializer.data)
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
   

