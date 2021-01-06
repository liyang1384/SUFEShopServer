from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from FavouritesService.service import FavouritesService
from FavouritesService.serializer import Favourites_detailSerializer

# Create your views here.
# FavouritesItem/
class FavouritesDetail(APIView):
    def get(self, request):
        qurey_params = request.query_params
        min_amount = qurey_params.get('min_amount')
        max_amount = qurey_params.get('max_amount')
        qurey_params.pop('min_amount')
        qurey_params.pop('max_amount')
        serializer = Favourites_detailSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        query_criteria = serializer.data
        query_criteria.update({'amount__gte': min_amount,'amount__lte': max_amount})
        instance = FavouritesService.getFavourites(query_criteria.user_id)
        serializer = Favourites_detailSerializer(instance,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Favourites_detailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        FavouritesService.insertCommodity(validated_data=serializer.data)
        return Response(serializer.data)

    def delete(self, request):
        serializer = Favourites_detailSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        FavouritesService.deleteCommodityFromFavourites(serializer.data.commodity_id,serializer.data.user_id)
        return Response({'msg':'删除成功!'})
