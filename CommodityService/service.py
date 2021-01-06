from .models import Commodity,CommodityApplication,BrowserHisory

# 业务类不应被实例化，其中的每个方法都用@staticmethod修饰符声明为静态方法

# 商品业务类


class CommodityService():
    @staticmethod
    def getCommodityDetail(commodity_id):
        return Commodity.objects.get(pk=commodity_id)
    # @staticmethod
    # def listUnauditedCommodities():
    #     unauditedcommodities = CommodityApplication.objects.filter(application_state ='TO_BE_REVIEWED',if_delete=False).values('Commodity')
    #     return Commodity.objects.filter(commodity_id__in = unauditedcommodities,if_delete=False)
    @staticmethod
    def processUnauditedCommodity(application_id,validated_data):
        return CommodityApplication.objects.update(application_id,validated_data)
    @staticmethod
    def rejectCommodity(application_id):
        return CommodityApplication.objects.update(application_id,{'application_state':'REJECTED'})
    @staticmethod
    def insertCommodity(validated_data):
        commoditydata = validated_data['commodity_name','commodity_type','commodity_picture','price','detail']
        commodity = Commodity.objects.create(commoditydata)
        commodityapplicationdata = validated_data['user']
        commodityapplicationdata['commodity'] = commodity.commodity_id
        CommodityApplication.objects.create(commodityapplicationdata)
    @staticmethod
    def listMyCommodity(user):
        mycommodity = CommodityApplication.objects.filter(user=user).values('Commodity')
        return Commodity.objects.filter(commodity_id__in = mycommodity,if_delete=False)
    @staticmethod
    def getMyCommodityDetail(commodity_id):
        return Commodity.objects.get(pk=commodity_id)
    @staticmethod
    def updateMyCommodityDetail(commodity_id,validated_data):
        return Commodity.objects.update(commodity_id,validated_data)
    # @staticmethod
    # def deleteCommodity(commodity_id):
    #     return Commodity.objects.update(commodity_id,{'if_delete':'True'})
    @staticmethod
    def updateMyCommodityApplicationDetail(application_id,validated_data):
        return Commodity.objects.update(application_id,validated_data)
    @staticmethod
    def getMyCommodityApplicationDetail(application_id):
        return Commodity.objects.get(application_id)
    @staticmethod
    def listCommodities(query_criteria):
        if query_criteria ==None:
            return Commodity.objects.filter(if_delete=False)
        else:
            query_criteria.update({'if_delete':'False'})
            return Commodity.objects.filter(**query_criteria)
    @staticmethod
    def listBrowseHistory(user):
        return BrowserHisory.objects.filter(user=user,if_delete=False)
