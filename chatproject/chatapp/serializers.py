from rest_framework import serializers,validators
from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','email']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance



    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)





class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    group_name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())


    class Meta:
        model = GroupDetails
        fields = ['id','group_name','members','date']

        def create(self, validated_data):
            return GroupDetails.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.group_name = validated_data.get('group_name', instance.group_name)
            instance.members = validated_data.get('members', instance.members)
            instance.save()
            return instance


    def validate(self, attrs):
        if GroupDetails.objects.filter(members=attrs['members']).exists():
            raise serializers.ValidationError(' User already in group')
        return super().validate(attrs)
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.ListField(child=serializers.CharField())
    groupmembers = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = GroupName
        fields = ['id', 'name','groupmembers']

        def create(self, validated_data):
            return GroupName.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.groupmembers = validated_data.get('groupmembers', instance.groupmembers)
            instance.save()
            return instance

    def validate(self, attrs):
        if GroupName.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError('group already exists')
        return super().validate(attrs)


# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='group_name', queryset=GroupDetails.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sender = validated_data.get('sender', instance.sender)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance

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


