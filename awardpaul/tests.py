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
        


