from django.test import TestCase
from .models import Project, Profile, Rate

# Create your tests here.

class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title='test', description='test', link='test', image='test')

    def test_project_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEqual(expected_object_name, 'test')

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(user='test', bio='test', contact='test', image='test')

    def test_profile_content(self):
        profile = Profile.objects.get(id=1)
        expected_object_name = f'{profile.user}'
        self.assertEqual(expected_object_name, 'test')   

class RateTestCase(TestCase):
    def setUp(self):
        Rate.objects.create(user='test', project='test', design='test', usability='test', content='test')

    def test_rate_content(self):
        rate = Rate.objects.get(id=1)
        expected_object_name = f'{rate.user}'
        self.assertEqual(expected_object_name, 'test')    
        


