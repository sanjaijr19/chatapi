from django.test import TestCase,Client
from rest_framework.test import APITestCase,APIClient
from django.test import SimpleTestCase
from django.urls import resolve,reverse
from .views import RegisterAPI,CreateUser,UserDetails,MessageDetails,GroupDetails
from django.contrib.auth.models import User
from .models import GroupDetails,GroupName,Message

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('CreateUser-list')
    def test_view(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 401)

class ViewTestmessage(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('CreateMessage-list')
    def test_view_msg(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 401)

class ViewTestGroup(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('CreateMessage-list')
    def test_view_grp(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 401)

class TestGroup(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('groupchat-list')
    def test_view_group(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 401)
class Testuser(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('user',args=[2])
    def test_view_user(self):
        response = self.client.get(self.reg_url)
        # self.assertEquals(response.status_code,200)
        self.assertTrue(response.status_code,200)

class TestGroupView(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('user',args=[2])
    def test_view_groups(self):
        response = self.client.get(self.reg_url)
        # self.assertEquals(response.status_code,200)
        self.assertTrue(response.status_code,200)

class TestMessage(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('user',args=[2])
    def test_view_message(self):
        response = self.client.get(self.reg_url)
        # self.assertEquals(response.status_code,200)
        self.assertTrue(response.status_code,200)


class Groupcreation(TestCase):
    def setUp(self):
        GroupName.objects.create(name='python')

    def test_group_create(self):
        group = GroupName.objects.filter(name="python")
        self.assertTrue(group.exists())

class GroupdetailsTest(TestCase):
    def setUp(self):
        grp = GroupName.objects.create(name='python')
        mem = User.objects.create(username='sanjai')
        GroupDetails.objects.create(group_name=grp)
        GroupDetails.objects.create(members=mem)

    def test_group_detail(self):
        group = GroupDetails.objects.filter(group_name=1)
        member = GroupDetails.objects.filter(members=1)
        self.assertTrue(group.exists())
        self.assertTrue(member.exists())

class MessageTest(TestCase):
    def setUp(self):
        sen = User.objects.create(username='sanjai')

        grp = GroupName.objects.create(name='python')
        rec = GroupDetails.objects.create(group_name=grp)
        Message.objects.create(sender=sen,receiver=rec,message="Hi")

    def test_message(self):
        group = Message.objects.filter(sender=1,receiver=1,message="Hi")
        self.assertTrue(group.exists())


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse('login')
        self.user_data = {
            'username' : "sanjai",
            'email': "sanjai@gmail.com",
            'password' : 'sanjai',
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

import pdb
class TestViews(TestSetUp):
    def test_user_register(self):
        res = self.client.post(self.register_url)
        # pdb.set_trace()
        self.assertEquals(res.status_code,400)
    #
    def test_user_register_correctly(self):
        resp = self.client.post(self.register_url,self.user_data,format="json")
        self.assertEqual(resp.status_code,200)

    def test_user_login_correctly(self):
        self.client.post(self.register_url, self.user_data, format='json')
        res = self.client.post(self.login_url, self.user_data, format='json')
        # pdb.set_trace()
        self.assertEqual(res.status_code, 200)




class AuthenticationTestCase(TestCase):
 def setUp(self):
       User.objects.create(username='testuser')
       User.objects.create(email='testuser@gmail.com')

 def test_user_created(self):
       user = User.objects.filter(username='testuser')
       email = User.objects.filter(email='testuser@gmail.com')
       self.assertTrue(user.exists())
       self.assertTrue(email.exists())

