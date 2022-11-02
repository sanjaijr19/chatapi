from django.contrib.auth.models import User
from .models import Message,UserProfile,GroupChat
from .serializers import MessageSerializer, UserSerializer,GroupSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from .pagination import Page
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# from chatapp.permissions import IsOwnerOrReadOnly
from knox.models import AuthToken


#Create user,messages,Group
class CreateUser(viewsets.ModelViewSet,APIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Page


class CreateMessage(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Page

class GroupMessage(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = GroupChat.objects.all()
    serializer_class = GroupSerializer



#update and delete the user, messages,Group
class Details(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsOwnerOrReadOnly]


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class GroupDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = GroupChat.objects.all()
    serializer_class = GroupSerializer


#View all members in group
class GroupMembers(APIView):
    def get(self,request):
        user=GroupChat.objects.all()
        serializer=GroupSerializer(user,many=True)
        return Response(serializer.data)