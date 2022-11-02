from rest_framework import serializers
from .models import UserProfile,Message,GroupChat
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
#
# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):

    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    group_members = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = GroupChat
        fields = ['id','group_members','join_date']

