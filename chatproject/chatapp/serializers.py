from rest_framework import serializers,validators
from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','email']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupName
        fields = ['id', 'name']

    # def create(self, validated_data):
    #     group = GroupName.objects.create_user(validated_data['name'])
    #     return group



    def validate(self, attrs):
        if GroupName.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError('group already exists')
        return super().validate(attrs)


class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    group_name = serializers.SlugRelatedField(many=False, slug_field='name', queryset=GroupName.objects.all())
    class Meta:
        model = GroupDetails
        fields = ['group_name','members','date']

    # def create(self):
    #     groups = GroupDetails.objects.create()
    #     return groups



    def validate(self, attrs):
        if GroupDetails.objects.filter(members=attrs['members']).exists():
            raise serializers.ValidationError(' User already in group')
        return super().validate(attrs)


# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='name', queryset=GroupName.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


    def validate(self, attrs):
        if GroupDetails.objects.filter(members=attrs['sender']).exists():
            return super().validate(attrs)
        else:
            raise serializers.ValidationError(' User not in group')
        return super().validate(attrs)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)


