from django.urls import path
from . import views
from knox import views as knox_views
from .views import LoginAPI
from .views import RegisterAPI
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register('user/',views.CreateUser,basename='CreateUser')
router.register('message',views.CreateMessage,basename='CreateMessage')
router.register('group',views.GroupMessage,basename='GroupMessage')
# router.register('groupname',views.Groupname,basename='Groupname')

urlpatterns = [
    path('cr/<int:pk>/', views.Details.as_view(), name='detail'),
    path('msg/<int:pk>', views.MessageDetails.as_view(), name='Messagedetails'),
    path('grp/<int:pk>', views.GroupDetails.as_view(), name='groupdetails'),
    # path('grpview/', views.GroupMembers.as_view(), name='groupmembers'),
    # path('grpname/', views.Groupname.as_view(), name='groupname'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('gettoken/',TokenObtainPairView.as_view(),name='tokenobtain'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='tokenrefresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='tokenverify'),
]+router.urls