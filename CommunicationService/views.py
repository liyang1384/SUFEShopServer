from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from CommunicationService.service import CommunicationService
from CommunicationService.serializer import MessageSerializer

# Create your views here.
class MessageDetail(APIView):
    def get(self, request, receive_user):
        instance = CommunicationService.getMessage(receive_user=receive_user)
        serializer = MessageSerializer(instance)
        return Response(serializer.data)
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommunicationService.insertMessage(validated_data=serializer.data)
        return Response(serializer.data)


class MessageList(APIView):
    def post(self,request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommunicationService.insertMessage(validated_data=serializer.data)
        return Response(serializer.data) 


