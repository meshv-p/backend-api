from django.http.response import HttpResponse
from Noteapp.models import Notes
from django.contrib.auth.models import User , Group
from rest_framework import viewsets , status , permissions
from api.serializers import  NoteSerializer , UserSerializer , GroupSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated , IsAdminUser, BasePermission
# from rest_framework.authentication import BasicAuthentication

# class WritebyAdminOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if request.method == 'GET':
#             return True
#         if request.method == 'POST' or request.method == 'PUT':
#             if user.is_superuser:
#                 return True
#         return False
    # return super().has_permission(request, view)

# Create your views here.
#  views.py
class getNotes(ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated,WritebyAdminOnlyPermission]
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer



'''
class Notes(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self,request):
        todo=Notes.objects.all()
        serializer=NoteSerializer(todo,many=True)
        return Response(serializer.data)
    def post(self,request):
        Notes.objects.create(
            title=request.POST.get('title'),
            text=request.POST.get('text'))
        return HttpResponse(status=201)
    def put(self, request,id, format=None):
        device = self.get_object(id)
        serializer = NoteSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
'''
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

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]