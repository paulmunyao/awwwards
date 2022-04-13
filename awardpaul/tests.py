from django.test import TestCase
from .models import Project, Profile, Rate,User

# Create your tests here.

class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.project = Project.objects.create(title='test', description='test', link='test', user=self.user)

    def test_project_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEqual(expected_object_name, 'test')

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.profile = Profile.objects.create(user=self.user, bio='test', contact='test')

    def test_profile_content(self):
        profile = Profile.objects.get(id=1)
        expected_object_name = f'{profile.user}'
        self.assertEqual(expected_object_name, 'test')   

class RateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.project = Project.objects.create(title='test', description='test', link='test', user=self.user)
        self.rate = Rate.objects.create(user=self.user, project=self.project, design=1, usability=1, content=1)

    def test_rate_content(self):
        rate = Rate.objects.get(id=1)
        expected_object_name = f'{rate.user}'
        self.assertEqual(expected_object_name, 'test')    
        


