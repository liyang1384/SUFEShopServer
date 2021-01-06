from rest_framework import routers
from django.urls import include, path
from OrderService.views import OrderDetail,OrderList,BuyerReviewDetail,SellerReviewDetail,PayOrderDetail,GenerateOrderDetail

urlpatterns = [
    path('orderdetail/',OrderDetail.as_view()),
    path('orderlist/',OrderList.as_view()),
    path('buyerreviewdetail/',BuyerReviewDetail.as_view()),
    path('sellerreviewdetail/',SellerReviewDetail.as_view()),
    path('payorderdetail/',PayOrderDetail.as_view()),
    path('generateorderdetail/',GenerateOrderDetail.as_view()),
    
]