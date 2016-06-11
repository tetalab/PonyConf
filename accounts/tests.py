from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import PonyConfSpeaker, PonyConfUser


ROOT_URL = 'accounts'


class AccountTests(TestCase):
    def setUp(self):
        for guy in 'ab':
            User.objects.create_user(guy, email='%s@example.org' % guy, password=guy)

    # MODELS

    def test_create_ponyconfuser(self):
        self.assertEqual(PonyConfUser.objects.count(), 2)

    # VIEWS

    def test_password(self):
        self.client.login(username='a', password='a')
        self.assertEqual(self.client.get(reverse('password')).status_code, 200)

    def test_profile(self):
        # User b wants to update its username, email and biography
        user = User.objects.get(username='b')
        self.assertEqual(user.email, 'b@example.org')
        self.assertEqual(user.ponyconfuser.biography, '')

        self.client.login(username='b', password='b')

        # He tries with an invalid address
        r = self.client.post(reverse('profile'), {'email': 'bnewdomain.com', 'username': 'z', 'biography': 'tester'})
        self.assertEqual(User.objects.filter(username='z').count(), 0)

        r = self.client.post(reverse('profile'), {'email': 'b@newdomain.com', 'username': 'z', 'biography': 'tester'})

        user = User.objects.get(username='z')
        self.assertEqual(user.email, 'b@newdomain.com')
        self.assertEqual(user.ponyconfuser.biography, 'tester')
