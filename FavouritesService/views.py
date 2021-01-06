from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from FavouritesService.service import FavouritesService
from FavouritesService.serializer import Favourites_detailSerializer
from rest_framework import status
from utils import delete_null
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
# FavouritesItem/
class FavouritesDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        serializer = Favourites_detailSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = FavouritesService.getFavourites(user_id=serializer.data.user_id)
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
