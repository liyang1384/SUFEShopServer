from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .service import UserService
from rest_framework import status
from utils import delete_null
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import delete_null
# Create your views here.
# class UserViewSet (ModelViewSet):
class UserList(APIView):
    #根据查询条件获取数据，没有返回查询条件就获取全部数据
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request):
        serializer = UserSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        query_criteria = serializer.data
        delete_null(query_criteria)
        # query_criteria = None
        query_set = UserService.getUserList(query_criteria=query_criteria)
        serializer = UserSerializer(query_set,many=True)
        return Response(serializer.data)  
        # return Response(query_criteria)  
class UserDetail(APIView):
    #获取一条数据
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request):   
        serializer = UserSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # user_id = serializer.data.get('user_id')
        user = UserService.getUserDetail(pk=serializer.data.get('user_id'))
        serializer = UserSerializer(user)
        return Response(serializer.data)  
        # return Response(user_id)  
    #删除一条数据(也可以不要)
    @csrf_exempt
    def delete(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.updateUserDetail(serializer.data.get('user_id'),{'if_delete':'True'})
        return Response({'msg':'删除成功!'})
        # return Response(serializer.data.get('user_id'))
    
    #新增一条数据
    @csrf_exempt
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = delete_null(serializer.data)
        UserService.insertUserInfo(validated_data=validated_data)
        return Response(serializer.data)
    #修改一条数据
    @csrf_exempt
    def put(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = delete_null(serializer.data)
        UserService.updateUserDetail(serializer.data.get('user_id'),validated_data)
        return Response(serializer.data)

class Login(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self,request):
        query_criteria = {'user_name':request.data.get('user_name'),'password':request.data.get('password')}
        user = UserService.getUserList(query_criteria).first()
        if not user:
            return Response(data={'msg':'用户名或者密码错误!'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = UserSerializer(user)
            if user.account_state=='DISABLE':
                return Response(data={'msg':'账号已禁用'},status=status.HTTP_403_FORBIDDEN)
            else: 
                return Response(data=serializer.data)
    def get(self,request):
        serializer = UserSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        code = UserService.getUserDetail(serializer.data.get('user_id')).get('password')
        if code == serializer.data.get('password'):
            return Response(data={'flag':'True'})
        else:
            return Response(data={'flag':'False'})