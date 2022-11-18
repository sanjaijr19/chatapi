from django.contrib.auth.models import User
from .models import Message,GroupDetails,GroupName
from .serializers import MessageSerializer, UserSerializer,RegisterSerializer,GroupnameSerializer,GroupSerializer,GroupViewSerializer
from rest_framework.response import Response
from rest_framework import generics,permissions,mixins
from rest_framework.views import APIView
from .pagination import Page,Pages
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from .permissions import IsPostOwner
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.renderers import JSONRenderer


#Create user,messages,Group
class CreateUser(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    # renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pages


class CreateMessage(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pages


class GroupChat(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GroupDetails.objects.all()
    serializer_class = GroupnameSerializer
    pagination_class = Pages
class CreateGroup(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GroupName.objects.all()
    serializer_class = GroupSerializer
    pagination_class = Pages

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GroupDetails.objects.all()
    serializer_class = GroupViewSerializer

#update and delete the user, messages,Group
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsPostOwner]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class GroupNameDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GroupName.objects.all()
    serializer_class = GroupSerializer
class GroupDetails(generics.RetrieveUpdateDestroyAPIView,generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GroupDetails.objects.all()
    serializer_class = GroupViewSerializer

#Register the New User
class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })

