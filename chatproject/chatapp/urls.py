from django.urls import path
from . import views
from knox import views as knox_views
# from .views import LoginAPI
from .views import RegisterAPI
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register('user',views.CreateUser,basename='CreateUser')
router.register('message',views.CreateMessage,basename='CreateMessage')
router.register('groupdetails',views.CreateGroup,basename='createGroup')
router.register('groupchat',views.GroupChat,basename='groupchat')

urlpatterns = [
    # path('create/', views.MessageCreate.as_view(), name='create'),
    path('user/<int:pk>/', views.UserDetails.as_view(), name='user'),
    path('msg/<int:pk>/', views.MessageDetails.as_view(), name='msg'),
    path('grp/<int:pk>/', views.GroupDetails.as_view(), name='grp'),
    # path('grpchat/<int:pk>', views.GroupChatDetails.as_view(), name='groupdet'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'),
]+router.urls






# path('api/login/', LoginAPI.as_view(), name='login'),
# path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
# path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')