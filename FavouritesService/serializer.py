from UserService.models import User
from UserService.serializer import UserSerializer
from CommodityService.models import Commodity
from CommodityService.serializer import CommoditySerializer
from FavouritesService.models import Favourites_detail
from rest_framework import serializers

class Favourites_detailSerializer(serializers.Serializer):
    #user_id = serializers.IntegerField(label="用户ID",allow_null=True,required=False)
    #commodity_id = serializers.IntegerField(label="商品ID",allow_null=True,required=False)
    collect_time = serializers.DateTimeField(label="收藏时间",allow_null=True,required=False)
    user = UserSerializer(required=False)
    commodity = CommoditySerializer(required=False)

    def create(self,validated_data):
        return Favourites_detail.objects.create(**validated_data)