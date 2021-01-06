from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .service import UserService
from rest_framework import status
# Create your views here.
# class UserViewSet (ModelViewSet):
class UserList(APIView):
    #根据查询条件获取数据，没有返回查询条件就获取全部数据
    def get(self,request):
        serializer = UserSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        query_criteria = serializer.data
        query_set = UserService.getUserList(query_criteria=query_criteria)
        serializer = UserSerializer(query_set,many=True)
        return Response(serializer.data)    

class UserDetail(APIView):
    #获取一条数据
    def get(self,request):   
        serializer = UserSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        user = UserService.getUserDetail(pk=serializer.data.user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)  
    #删除一条数据(也可以不要)
    def delete(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.updateUserDetail(serializer.data.user_id,{'if_delete':'False'})
        return Response({'msg':'删除成功!'})
    
    #新增一条数据
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.insertUserInfo(validated_data=serializer.data)
        return Response(serializer.data)
    #修改一条数据
    def put(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.updateUserDetail(serializer.data.user_id,serializer.data)
        return Response(serializer.data)

class Login(APIView):
    def post(self,request):
        query_criteria = {'user_name':request.data.get('user_name'),'password':request.data.get('password')}
        user = UserService.getUserList(query_criteria).first()
        if not user:
            return Response(data={'msg':'用户名或者密码错误!'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = UserSerializer(user)
            user = UserService.getUserDetail(serializer.data.user_name)
            if user.account_state=='DISABLE':
                return Response(data={'msg':'账号已禁用'},status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(data={'msg':'登录成功!'})
