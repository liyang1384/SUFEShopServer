from UserService.models import User
from CommodityService.models import Commodity
from FavouritesService.models import Favourites_detail

class FavouritesService():
    @staticmethod
    def getFavourites(user_id):
        return Favourites_detail.objects.filter(user_id=user_id, if_delete=False)

    @staticmethod
    def deleteCommodityFromFavourites(commodity_id,user_id):
        favouritesdetaildata = Favourites_detail.objects.filter(commodity_id=commodity_id,user_id=user_id)
        favourites_detail_id = favouritesdetaildata.favourites_detail_id
        return Favourites_detail.objects.delete(favourites_detail_id)

    @staticmethod
    def insertCommodity(validated_data):
        favouritesdetaildata = validated_data['commodity_id','user_id']
        Favourites_detail.objects.create(favouritesdetaildata)
