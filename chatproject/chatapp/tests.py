from django.test import TestCase,Client
from django.test import SimpleTestCase
from django.urls import resolve,reverse
from .views import RegisterAPI,CreateUser,UserDetails,MessageDetails,GroupDetails
from django.contrib.auth.models import User
from .models import GroupDetails,GroupName
# Create your tests here.
# class URLTestcase(TestCase):
#     def test(self):
#         client = Client()
#         User.objects.create_user(username="sanjai",password="sanjai",email="sanjai@gmail.com")
#         response = client.get(reverse('register'))
#         self.assertEquals(response.status_code,200)
class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('CreateUser-list')
    def test_view(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 200)

class ViewTestmessage(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('CreateMessage-list')
    def test_view_msg(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 200)

class ViewTestGroup(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('CreateMessage-list')
    def test_view_grp(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 200)

class TestGroup(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('groupchat-list')
    def test_view_group(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 200)
class Testuser(TestCase):
    def setUp(self):
        self.client = Client()
        self.reg_url = reverse('grp',args=[1])
    def test_view_user(self):
        response = self.client.get(self.reg_url)
        self.assertEquals(response.status_code, 200)


# class TestUrls(SimpleTestCase):
#     def test_url(self):
#         url = reverse("register")
#         self.assertEquals(resolve(url).func.view_class, RegisterAPI)
# #
#     def test_urls(self):
#         url = reverse("userdetails",args=[1])
#         self.assertEquals(resolve(url).func.view_class,UserDetails)
#
#     def test_url_message(self):
#         url = reverse("msg", args=[1])
#         self.assertEquals(resolve(url).func.view_class, MessageDetails)
#
#     def test_url_group(self):
#         url = reverse("grp", args=[1])
#         self.assertEquals(resolve(url).func.view_class, GroupDetails)

    # def test_url_group(self):
    #     url = reverse("user")
    #     self.assertEquals(resolve(url).func.view_class, CreateUser)

#
# class TestModels(TestCase):
#     def setUp(self):
#         self.create = GroupName.objects.create(
#             name = "project"
#         )
#
#     def testmodels(self):
#         self.assertEquals(self.create,'project')