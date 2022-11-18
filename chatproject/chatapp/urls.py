from django.urls import path
from . import views
from knox import views as knox_views
# from .views import LoginAPI
from .views import RegisterAPI
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router =routers.DefaultRouter()
router.register(r'createuser',views.CreateUser,basename='CreateUser')
router.register('message',views.CreateMessage,basename='CreateMessage')
router.register('groupName',views.CreateGroup,basename='createGroup')
router.register('groupchat',views.GroupChat,basename='groupchat')
router.register('groupview',views.GroupViewSet,basename='groupview')

urlpatterns = [
    # path('create/', views.MessageCreate.as_view(), name='create'),
    path('user/<int:pk>', views.UserDetails.as_view(), name='user'),
    path('msg/<int:pk>/', views.MessageDetails.as_view(), name='msg'),
    path('grp/<int:pk>/', views.GroupDetails.as_view(), name='grp'),
    path('grpname/<int:pk>/', views.GroupNameDetails.as_view(), name='grpname'),
    # path('grpchat/<int:pk>', views.GroupChatDetails.as_view(), name='groupdet'),
    # path('grpview/', views.GroupView.as_view(), name='GroupView'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'),
]+router.urls






# path('api/login/', LoginAPI.as_view(), name='login'),
# path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
# path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')