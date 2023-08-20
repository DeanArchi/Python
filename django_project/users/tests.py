from django.test import TestCase
from django.urls import reverse

from users.models import User


class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='test_user',
            password='test_pass',
            first_name='test_name',
            last_name='test_last_name',
            age=22
        )

    def test_user_info(self):
        self.assertEqual(self.user.first_name, 'test_name')
        self.assertEqual(self.user.last_name, 'test_last_name')
        self.assertEqual(self.user.age, 22)


class TestUserViewSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='test',
            password='tEsT1234555',
            first_name='qwe',
            last_name='dsa',
            age=22
        )

    def test_user_create_view(self):
        url = reverse('users:user-create')
        data = {
            'username': 'new_user',
            'password1': 'newPASSword123',
            'password2': 'newPASSword123',
            'first_name': 'New',
            'last_name': 'User',
            'age': 30,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        new_user = User.objects.get(username='new_user')

        self.assertEqual(new_user.first_name, data.get('first_name'))
        self.assertEqual(new_user.last_name, data.get('last_name'))
        self.assertEqual(new_user.age, data.get('age'))

    def test_user_detail_view(self):
        response = self.client.get(f'users/{self.user.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'qwe')

    def test_user_delete_view(self):
        response = self.client.get(f'users/{self.user.pk}/delete/')
        self.assertEqual(response.status_code, 302)
