from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user/',views.CreateUser,basename='CreateUser')
router.register('message',views.CreateMessage,basename='CreateMessage')
router.register('group',views.GroupMessage,basename='GroupMessage')

urlpatterns = [
    path('cr/<int:pk>/', views.Details.as_view(), name='detail'),
    path('msg/<int:pk>', views.MessageDetails.as_view(), name='Messagedetails'),
    path('grp/<int:pk>', views.GroupDetails.as_view(), name='groupdetails'),
    path('grpview/', views.GroupMembers.as_view(), name='groupmembers'),
]+router.urls