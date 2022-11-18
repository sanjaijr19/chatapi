from rest_framework import serializers,validators
from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User


class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.ListField(write_only=True)
    group_name = serializers.CharField(required=False)

    class Meta:
        model = GroupDetails
        fields = ['id','group_name','members','date']

    def create(self, validated_data):
        # print(validated_data["group_name"])
        # print(validated_data["members"])
        group_name,created = GroupName.objects.get_or_create(name=validated_data["group_name"])

        for user in validated_data["members"]:
            user = User.objects.get(id=user)
            #print(user.id)
            if user:
                GroupDetails.objects.create(group_name=group_name,members=user)
                print(group_name.id)
            else:
                raise serializers.ValidationError("user does not exist")

            return validated_data



class GroupViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupDetails
        fields = ['id', 'group_name', 'members', 'date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="CreateUser")
    members = GroupnameSerializer(many=True,read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','password','members']

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


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GroupName
        fields = ['id', 'name']

    def create(self, validated_data):
        return GroupName.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


    def validate(self, attrs):
        if GroupName.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError('group already exists')
        return super().validate(attrs)


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
    def create(self, validated_data):
        return Message.objects.create(**validated_data)




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)






