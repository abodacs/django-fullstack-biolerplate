from django.urls import reverse

from apps.users.tests.factories import EnvoyFactory
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CaseFactory


class CategoryTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.envoy_1 = EnvoyFactory(username="envoy")

    def test_list_cases(self):
        url = reverse("cases-list")
        CaseFactory.create_batch(2, envoy=self.envoy_1)

        # No authenticated
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.envoy_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
