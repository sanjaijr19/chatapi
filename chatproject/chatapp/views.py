from django.contrib.auth.models import User
from .models import Message,GroupDetails,GroupName
from .serializers import MessageSerializer, UserSerializer,RegisterSerializer,GroupnameSerializer,GroupSerializer
from rest_framework.response import Response
from rest_framework import generics,permissions,mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from .pagination import Page,Pages
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from .permissions import IsPostOwner
from knox.models import AuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters     
# class MessageCreate(mixins.CreateModelMixin,generics.GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#Create user,messages,Group
class CreateUser(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pages
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['username','email']
    search_fields = ['username','email']
    ordering_fields = ['username','email']


class CreateMessage(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pages
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['sender','receiver','message']
    search_fields = ['sender','receiver','message']
    ordering_fields = ['sender','receiver','message']



# class GroupMessage(viewsets.ModelViewSet):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#     queryset = GroupMembers.objects.all()
#     serializer_class = GroupSerializer
#     pagination_class = Pages

class GroupChat(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = GroupDetails.objects.all()
    serializer_class = GroupnameSerializer
    pagination_class = Pages
class CreateGroup(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = GroupName.objects.all()
    serializer_class = GroupSerializer
    pagination_class = Pages
# class Groupname(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#     def get(self,request):
#         user=Group_Name.objects.all()
#         serializer=GroupnameSerializer(user,many=True)
#         return Response(serializer.data)



#update and delete the user, messages,Group
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsOwnerOrReadOnly]

class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GroupDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = GroupDetails.objects.all()
    serializer_class = GroupnameSerializer

# class GroupChatDetails(generics.RetrieveUpdateDestroyAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#     queryset = GroupMembers.objects.all()
#     serializer_class = GroupSerializer


#View all members in group
# class GroupMembers(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#     def get(self,request):
#         queryset = GroupMembers.objects.all()
#         serializer=GroupSerializer(queryset,many=True)
#         return Response(serializer.data)


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



# Login User
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

