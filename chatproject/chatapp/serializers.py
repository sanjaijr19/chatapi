from rest_framework import serializers,validators
from .models import Message,GroupMembers,Group_Name
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
        group_members = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
        class Meta:
            model = GroupMembers
            fields = ['id', 'group_members', 'join_date']


# class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
#     name = serializers.SlugRelatedField(many=True, slug_field='group_members', queryset=GroupMembers.objects.all())
#     class Meta:
#         model = Group_Name
#         fields = ['id','group_name','name','date']

# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):

    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='group_name', queryset=Group_Name.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
