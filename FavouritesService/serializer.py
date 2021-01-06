from UserService.models import User
from UserService.serializer import UserSerializer
from CommodityService.models import Commodity
from CommodityService.serializer import CommoditySerializer
from FavouritesService.models import Favourites_detail
from rest_framework import serializers

class Favourites_detailSerializer(serializers.Serializer):
    user = serializers.CharField(label="用户",allow_null=True)
    commodity = serializers.CharField(label="商品",allow_null=True)
    collect_time = serializers.DateTimeField(label="收藏时间",allow_null=True)

    def create(self,validated_data):
        return Favourites_detail.objects.create(**validated_data)