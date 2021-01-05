from .models import User

class UserService():
    @staticmethod
    def insertUserInfo(validated_data):
        User.objects.create(validated_data=validated_data)

    @staticmethod
    def getUserDetail(pk):
        return User.objects.get(pk=pk)

    @staticmethod
    def getUserList(query_criteria=None):
        if query_criteria ==None:
            return User.objects.all()
        else:
            query_criteria.update({'if_delete':'False'})
            return User.objects.filter(**query_criteria)

    @staticmethod        
    def updateUserDetail(pk,validated_data):
        return User.objects.update(pk=pk,validated_data=validated_data)