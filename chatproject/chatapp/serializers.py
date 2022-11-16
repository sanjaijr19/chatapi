from rest_framework import serializers,validators
from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','password']

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance


    # def validate(self, attrs):
    #     if User.objects.filter(email=attrs['email']).exists():
    #         raise serializers.ValidationError('email already exists')
    #     return super().validate(attrs)


class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    # group_name = serializers.SlugRelatedField(slug_field='name', queryset=GroupName.objects.all())
    # members = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # members = UserSerializer()
    members = serializers.ListField(child=serializers.CharField())
    group_name = serializers.CharField(required=False)
    # group_name = serializers.ListField(child=serializers.CharField())


    class Meta:
        model = GroupDetails
        fields = ['id','group_name','members','date']

    def create(self, validated_data):
        # print(validated_data["group_name"])
        # print(validated_data["members"])
        group_name,created = GroupName.objects.get_or_create(name=validated_data["group_name"])
        print(group_name.id)
        for user in validated_data["members"]:
            user = User.objects.get(username=user)
            print(user.id)

            if user:
                GroupDetails.objects.create(group_name=group_name,members=user)
            else:
                raise serializers.ValidationError("user does not exist")

            return validated_data


    # def update(self, instance, validated_data):
    #     instance.group_name = validated_data.get('group_name', instance.group_name)
    #     instance.members = validated_data.get('members', instance.members)
    #     instance.save()
    #     return instance
    #
    # def validate(self, attrs):
    #     if GroupDetails.objects.filter(members=attrs['members']).exists():
    #         raise serializers.ValidationError('user already in group')
    #     return super().validate(attrs)
    def validate(self, attrs):
        member=GroupDetails.objects.filter(members_id=attrs['members'])
        group=GroupDetails.objects.filter(group_name_id=attrs['group_name_id'])
        if (member and group).exists():
            raise serializers.ValidationError('user already in group')
        return super().validate(attrs)
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.ListField(child=serializers.CharField())
    # groupmembers = GroupnameSerializer(many=True,read_only=True)

    class Meta:
        model = GroupName
        fields = ['id', 'name']


    # def create(self, validated_data):
        # groups_data = validated_data.pop("groupmembers")
        # group_name = GroupName.objects.create(**validated_data)
        # for group_data in groups_data:
        #     GroupDetails.objects.create(group_name=group_name,groupmember= group_data)
        # return group_name


        # def create(self, validated_data):
        #     return GroupName.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.groupmembers = validated_data.get('groupmembers', instance.groupmembers)
        #     instance.save()
        #     return instance

    # def validate(self, attrs):
    #     if GroupName.objects.filter(name=attrs['name']).exists():
    #         raise serializers.ValidationError('group already exists')
    #     return super().validate(attrs)


# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    # sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    # receiver = serializers.SlugRelatedField(many=False, slug_field='name', queryset=GroupName.objects.all())
    # receiver = serializers.ListField(child=serializers.CharField())
    sender = serializers.ListField(child=serializers.CharField())
    #
    receiver = serializers.CharField(required=False)
    message = serializers.CharField(required=False)
    # sender = serializers.StringRelatedField()
    # receiver = serializers.StringRelatedField()


    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
    # def create(self, validated_data):
    #     return Message.objects.create(**validated_data)

    def create(self, validated_data):
        receiver = GroupDetails.objects.get(group_name_id=validated_data["receiver"])
        # print(receiver.id)
        message = Message.objects.create(message=validated_data["message"])
        # print(message.id)
        for user in validated_data["sender"]:
            user = GroupDetails.objects.get(members_id=user)
            # print(user.id)
            if user:
                Message.objects.create(sender=user,receiver=receiver,message=message)
            else:
                raise serializers.ValidationError("user not in this group")
            return validated_data

    # def validators(self,**kwargs):
        # members = GroupDetails.objects.filter(members_id=members_id)
        # print(members.id)
        # group = GroupDetails.objects.filter(group_name_id=group_name_id)
        # print(group.id)
        # if members.id not in group.id:
        #     raise serializers.ValidationError("not")




    # def validate(self, attrs):
    #     group = GroupDetails.objects.filter(group_name_id = attrs["group_name_id"])
    #     users = User.objects.filter(id =attrs["id"])
    #     print(group)
    #     print(users)

        # if users not in group:
        #     raise serializers.ValidationError("not")
        # return super().validate(attrs)

    # def update(self, instance, validated_data):
    #     instance.sender = validated_data.get('sender', instance.sender)
    #     instance.receiver = validated_data.get('receiver', instance.receiver)
    #     instance.message = validated_data.get('message', instance.message)
    #     instance.save()
    #     return instance
    #
    # def validate(self, attrs):
    #     if GroupDetails.objects.filter(members=attrs['sender']).exists():
    #         return super().validate(attrs)
    #     else:
    #         raise serializers.ValidationError(' User not in group')
    #     return super().validate(attrs)


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






