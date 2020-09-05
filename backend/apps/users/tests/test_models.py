from django.db.models.signals import post_save
from django.test import TestCase

import factory

from .factories import UserFactory


class TestUser(TestCase):
    @factory.django.mute_signals(post_save)
    def test__user_str_representation_to_be_user_name(self):
        user = UserFactory(username="my_user_name")
        self.assertEqual(str(user), user.username)
