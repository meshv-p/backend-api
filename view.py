from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from Noteapp.models import Notes
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import  NoteSerializer , UserSerializer
from rest_framework.response import Response


#  views.py

class Notes(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

class List(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# class UserLoggedin(viewsets.ModelViewSet):
#     # user = 
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
@api_view(['GET'])
def getdata():
    return Response({"message":"hey"})

# @api_view(['GET'])
# def UserLoggedin(request):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
 

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]