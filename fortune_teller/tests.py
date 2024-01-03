from django.test import TestCase
from .forms import RegisterForm
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Fortune
from .forms import FortuneForm

class RegisterFormTest(TestCase):

    def test_valid_register_form(self):
        data = {'username': 'newuser', 'email': 'user@example.com', 'password1': 'dfgjkldfsg345', 'password2': 'dfgjkldfsg345'}
        form = RegisterForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_register_form(self):
        data = {'username': 'newuser', 'email': 'user@example.com', 'password1': 'dfgjkldfsg345', 'password2': 'different'}
        form = RegisterForm(data)
        self.assertFalse(form.is_valid())



class FortuneModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser', password='12345')
        Fortune.objects.create(title='Test Fortune', text='A test fortune', zodiac_sign='Aries', sex='M', user=user)

    def test_fortune_creation(self):
        fortune = Fortune.objects.get(id=1)
        self.assertEqual(fortune.title, 'Test Fortune')
        self.assertEqual(fortune.text, 'A test fortune')
        self.assertEqual(fortune.zodiac_sign, 'Aries')
        self.assertEqual(fortune.sex, 'M')
        self.assertEqual(fortune.user.username, 'testuser')



class FortuneFormTest(TestCase):

    def test_valid_form(self):
        user = User.objects.create(username='testuser', password='12345')
        data = {'title': 'Test Title', 'text': 'Some text', 'zodiac_sign': 'Aries', 'sex': 'M', 'user': user}
        form = FortuneForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = FortuneForm(data={})
        self.assertFalse(form.is_valid())
