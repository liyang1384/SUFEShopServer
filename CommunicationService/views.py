from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from CommunicationService.service import CommunicationService
from CommunicationService.serializer import MessageSerializer
from rest_framework import status
from utils import delete_null
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
class MessageDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        serializer = MessageSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        instance = CommunicationService.getMessage(receive_user=serializer.data.get('receive_user'))
        serializer = MessageSerializer(instance)

        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommunicationService.insertMessage(validated_data=serializer.data)
        return Response(serializer.data)


class MessageList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self,request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommunicationService.insertMessage(validated_data=serializer.data)
        return Response(serializer.data) 


