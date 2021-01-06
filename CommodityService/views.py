from django.shortcuts import render
from .service import CommodityService
from .serializer import CommoditySerializer,CommodityApplicationSerializer,BrowserHisorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .service import CommodityService
from utils import delete_null
# CommodityItem?
class CommodityDetail(APIView):
    # 查询一件商品
    def get(self, request):
        serializer = CommoditySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = CommodityService.getCommodityDetail(commodity_id=serializer.data.get('commodity_id'))
        serializer = CommoditySerializer(instance)
        return Response(serializer.data)
    # 发布一件商品
    def post(self, request):
        # serializer=CommoditySerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        CommodityService.insertCommodity(validated_data=request.data)# 包含创建申请过程
        return Response(request.data)

    def put(self, request):
        serializer = CommoditySerializer(request.data)
        serializer.is_valid(raise_exception=True)
        CommodityService.updateMyCommodityDetail(serializer.data.get('commodity_id'),serializer.data)
        return Response(serializer.data)
    # 删除商品申请以及商品
    def delete(self, request):
        serializer = CommoditySerializer(request.data)
        serializer.is_valid(raise_exception=True)
        CommodityService.updateMyCommodityDetail(serializer.data.get('commodity_id'),{'if_delete':'True','state':'DELETED'})
        commodityapplication = CommodityService.listCommodities({'commodity':serializer.data.get('commodity_id')}).first()
        CommodityService.updateMyCommodityApplicationDetail(commodityapplication.get('application_id'),{'if_delete':'True'})
        return Response({'msg':'删除成功'})        

class MyCommodityList(APIView):
    def get(self, request):
        serializer = CommoditySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        query_set = CommodityService.listMyCommodity(serializer.data.get('user'))
        serializer = CommoditySerializer(query_set,many=True)
        return Response(serializer.data)
    # listcommodities()

class CommodityList(APIView):
    def get(self, request):
        qurey_params = request.query_params.copy()
        min_price = qurey_params.get('min_price')
        max_price = qurey_params.get('max_price')
        qurey_params.pop('min_price')
        qurey_params.pop('max_price')
        serializer = CommoditySerializer(data=qurey_params)
        serializer.is_valid(raise_exception=True)
        query_criteria = serializer.data
        query_criteria.update({'price__gte': min_price,'price__lte': max_price})
        query_criteria = delete_null(query_criteria)
        query_set = CommodityService.listCommodities(query_criteria)
        serializer = CommoditySerializer(query_set,many=True)
        return Response(serializer.data)
        # return Response(query_criteria)

class AuditCommodityList(APIView):
    def get(self, request):
        # serializer = CommoditySerializer(data=request.query_params)
        # serializer.is_valid(raise_exception=True)
        # query_set = CommodityService.listCommodities(serializer.data)
        # serializer = CommodityApplicationSerializer(query_set,many=True)
        # return Response(serializer.data)
        qurey_params = request.query_params.copy()
        min_price = qurey_params.get('min_price')
        max_price = qurey_params.get('max_price')
        qurey_params.pop('min_price')
        qurey_params.pop('max_price')
        serializer = CommoditySerializer(data=qurey_params)
        serializer.is_valid(raise_exception=True)
        query_criteria = serializer.data
        query_criteria = delete_null(query_criteria)
        query_criteria.update({'price__gte': min_price,'price__lte': max_price})
        query_set = CommodityService.listCommodities(query_criteria)# 取得所有商品
        serializer = CommoditySerializer(query_set,many=True)
        # return Response(query_set)
        return Response(serializer.data)
        # return Response(query_criteria)
    def patch(self, request):
        serializer = CommodityApplicationSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        commodityapplication = CommodityService.getMyCommodityApplicationDetail(serializer.data.get('application_id'))
        CommodityService.processUnauditedCommodity(serializer.data.get('application_id'),serializer.data)
        # 同步修改商品状态
        if serializer.data.application_state == 'APPROVED':
            CommodityService.updateMyCommodityDetail(commodityapplication.commodity,{'state':'ON_THE_SHELVES'})
        elif serializer.data.application_state == 'REJECTED':
            CommodityService.updateMyCommodityDetail(commodityapplication.commodity,{'state':'REJECTED'})
        else:
            pass
        return Response(serializer.data)

class BrowseHistoryList(APIView):
    def get(self, request):
        serializer = CommoditySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        query_set = CommodityService.listBrowseHistory(serializer.data.get('user'))
        serializer = BrowserHisorySerializer(query_set,many=True)
        return Response(serializer.data)