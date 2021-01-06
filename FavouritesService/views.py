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
        serializer = Favourites_detailSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = FavouritesService.getFavourites(user=serializer.data.user)
        serializer = Favourites_detailSerializer(instance)
        return Response(serializer.data)
    def post(self, request):
        serializer = Favourites_detailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        FavouritesService.insertCommodity(validated_data=serializer.data)
        return Response(serializer.data)
    def delete(self, request):
        serializer = Favourites_detailSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        FavouritesService.deleteCommodityFromFavourites(serializer.data.favourites_detail_id)
        return Response({'msg':'删除成功!'})
