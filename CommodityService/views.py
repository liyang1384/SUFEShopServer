from django.shortcuts import render
from .service import CommodityService
from .serializer import CommoditySerializer,CommodityApplicationSerializer,BrowserHisorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .service import CommodityService

# CommodityItem?
class CommodityDetail(APIView):
    # 查询一件商品
    def get(self, request):
        serializer = CommoditySerializer(request.data)
        instance = CommodityService.getCommodityDetail(commodity_id=serializer.data.commodity_id)
        serializer = CommoditySerializer(instance)
        return Response(serializer.data)
    # 发布一件商品 申请有问题！
    def post(self, request):
        serializer=CommoditySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommodityService.insertCommodity(validated_data=serializer.data)
        return Response(serializer.data)

    def put(self, request):
        serializer = CommoditySerializer(request.data)
        CommodityService.updateMyCommodityDetail(serializer.data.commodity_id,serializer.data)
        return Response(serializer.data)
    # 删除商品
    def delete(self, request):
        serializer = CommoditySerializer(request.data)
        CommodityService.updateMyCommodityDetail(serializer.data.commodity_id,{'if_delete':'True'})
        return Response({'msg':'删除成功'})        

class MyCommodityList(APIView):
    def get(self, request):
        serializer = CommoditySerializer(request.data)
        query_set = CommodityService.listMyCommodity(serializer.data.user)
        serializer = CommoditySerializer(query_set)
        return Response(serializer.data)
    # listcommodities()

class CommodityList(APIView):
    def get(self, request):
        query_set = CommodityService.listCommodities()
        serializer = CommoditySerializer(query_set)
        return Response(serializer.data)

class AuditCommodityList(APIView):
    def get(self, request):
        query_set = CommodityService.listUnauditedCommodities()
        serializer = CommodityApplicationSerializer(query_set,many=True)
        return Response(serializer.data)
    def patch(self, request):
        serializer = CommodityApplicationSerializer(request.data)
        CommodityService.processUnauditedCommodity(serializer.data.application_id,serializer.data)
        return Response(serializer.data)

class BrowseHistoryList(APIView):
    def get(self, request):
        serializer = CommoditySerializer(request.data)
        query_set = CommodityService.listBrowseHistory(serializer.data.user)
        serializer = BrowserHisorySerializer(query_set,many=True)
        return Response(serializer.data)