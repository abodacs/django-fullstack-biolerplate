from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CaseFactory, ConfirmationFactory, EnvoyFactory, PatchFactory, ProjectFactory


class PatchTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.envoy_1 = EnvoyFactory(username="envoy")
        cls.envoy_2 = EnvoyFactory(username="envoy_2")
        cls.project = ProjectFactory(envoys=[cls.envoy_1, cls.envoy_2])
        cls.case = CaseFactory(envoy=cls.envoy_1)

    def test_list_envoy_patches(self):
        url = reverse("patches-my-patches")
        PatchFactory.create_batch(1, project=self.project)

        # No authenticated
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.envoy_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def create_patch(self):
        patch = PatchFactory(project=self.project)
        ConfirmationFactory(patch=patch, case=self.case, envoy=self.envoy_1)
        ConfirmationFactory(patch=patch, case=self.case, envoy=self.envoy_2)
        return patch

    def test_list_envoy_confirmations(self):
        url = reverse("confirmations-my-confirmations")
        self.create_patch()
        # No authenticated
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.envoy_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def change_deliver_status(self, reverse_url="confirmations-confirm"):

        patch = self.create_patch()
        instance = ConfirmationFactory(patch=patch, case=self.case, envoy=self.envoy_1)
        url = reverse("confirmations-confirm", kwargs={"pk": instance.id,})
        # No authenticated
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.envoy_1)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        instance = ConfirmationFactory(patch=patch, case=self.case, envoy=self.envoy_2)
        url = reverse("confirmations-confirm", kwargs={"pk": instance.id,})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_confirm_case(self):
        self.change_deliver_status()

    def test_cancel_case(self):
        self.change_deliver_status(reverse_url="confirmations-cancel")
