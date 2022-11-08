from rest_framework import serializers,validators
from .models import Message,GroupDetails
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','email']



# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#         group_members = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
#         class Meta:
#             model = GroupMembers
#             fields = ['id', 'group_members', 'join_date']


class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.SlugRelatedField(many=True, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = GroupDetails
        fields = ['group_name','members','date']

# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='group_name', queryset=GroupDetails.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']

    # def update(self,instance,validated_data):
    #     instance.sender = validated_data.get('sender',instance.sender)
    #     instance.receiver = validated_data.get('receiver',instance.receiver)
    #     instance.message = validated_data.get('message',instance.message)
    #     instance.save()
    #     return instance

    # def validate_sender(self,sender):
    #     if sender not in GroupDetails.objects.filter(members=members).exists():
    #         raise serializers.ValidationError("not in the group")
    #     return sender
    # def validate(self, attrs):
    #     if sender not in GroupDetails.objects.filter(sender=attrs['members']).exists():
    #         raise serializers.ValidationError('sender not in the group')
    #     return super().validate(attrs)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    # def validate_email(self,email):
    #     if email == User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError("email already exist")
    #     return email

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)

