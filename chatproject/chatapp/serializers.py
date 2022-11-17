from rest_framework import serializers,validators
from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User


class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    # group_name = serializers.SlugRelatedField(slug_field='name', queryset=GroupName.objects.all())
    # members = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # members = UserSerializer()
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
            print(user.id)
            # if user.exists():
            #     raise serializers.ValidationError("user does not exist")
            if user:
                GroupDetails.objects.create(group_name=group_name,members=user)
                print(group_name.id)
                # print(user.id)
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
    # def validate(self, attrs):
    #     member=GroupDetails.objects.filter(members_id=attrs['members_id']).exist()
    #     group=GroupDetails.objects.filter(group_name_id=attrs['group_name_id'])
    #     if member in group:
    #         raise serializers.ValidationError('user already in group')
    #     return super().validate(attrs)

    # def validators(self):
    #     member = GroupDetails.objects.filter(members=members).exists()
    #     group = GroupDetails.objects.filter(group_name=group_name)
    #     if member in group:
    #         raise serializers.ValidationError('user already in group')
        # return super().validate(attrs)





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
class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    # print(sender)
    # receiver = serializers.SlugRelatedField(many=, slug_field='username', queryset=User.objects.all())
    # sender = serializers.CharField(required=False)
    # receiver = serializers.PrimaryKeyRelatedField(many=False,queryset=GroupDetails.objects.all())
    # message = serializers.CharField(required=False)
    # print(receiver)


    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
    def create(self, validated_data):
        return Message.objects.create(**validated_data)






    # def create(self, validated_data):
    #     receiver = GroupDetails.objects.get(group_name_id=validated_data["receiver"])
    #     # print(receiver.id)
    #     message = Message.objects.create(message=validated_data["message"])
    #     # senders = GroupDetails.objects.filter(members_id=validated_data["members_id"])
    #     # print(message.id)
    #     for user in validated_data["sender"]:
    #         user = GroupDetails.objects.get(members_id=user)
    #         if user:
    #             Message.objects.create(sender=user, receiver=receiver, message=message)
    #         else:
    #             raise serializers.ValidationError("user not in this group")
    #         return validated_data

    # def validators(self,**kwargs):
    #     members = GroupDetails.objects.filter(members_id=members_id)
    #     print(members.id)
    #     group = GroupDetails.objects.filter(group_name_id=group_name_id)
    #     print(group.id)
    #     if members.id not in group.id:
    #         raise serializers.ValidationError("not")

    # def validators(self):
    #     members = GroupDetails.objects.filter(group_name_id=group_name_id)
    #     print(members)
    #     group = Message.objects.filter(sender_id=sender_id)
    #     print(group)
    #     if members != group:
    #         raise serializers.ValidationError("not")

    # def validated_data(self):
    #     members = GroupDetails.objects.filter(group_name_id=group_name_id)
    #     print(members)
    #     sender = Message.objects.filter(sender_id=sender_id)
    #     print(sender)
    #     if members != sender:
    #         raise serializers.ValidationError("user not in this group")

    # def validate(self, attrs):
    #     # if Message.objects.filter(receiver=attrs['receiver']) == Message.objects.filter(sender=attrs['sender']):
    #     msg = GroupDetails.objects.filter(receiver=attrs['receiver'])
    #     grp = Message.objects.filter(sender=attrs['sender'])
    #     if msg != grp:
    #         raise serializers.ValidationError('email already exists')
    #     return super().validate(attrs)


    # def validators(self):
    #     # msg = GroupDetails.objects.filter(receiver=['receiver'])
        # print(msg)
        # grp = Message.objects.filter(sender=['sender'])
        # if msg != grp:
        #     raise serializers.ValidationError('user already exists')


    # def validate(self, attrs):
    #     group = GroupDetails.objects.filter(group_name_id = attrs["group_name_id"])
    #     users = User.objects.filter(id =attrs["id"])
    #     print(group)
    #     print(users)
    #
    #     if users not in group:
    #         raise serializers.ValidationError("not")
    #     return super().validate(attrs)

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
        fields = ('url', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)






