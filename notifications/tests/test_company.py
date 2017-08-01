from django.test import TestCase
from django.urls import reverse

from notifications.tests.base import factories


class CompanyTest(TestCase):

    def test_company_list(self):
        group = factories.CompaniesGroupFactory(code='f-gases-eu')
        company = factories.CompanyFactory(group=group)
        user = factories.UserFactory(is_staff=True)
        self.client.force_login(user)
        resp = self.client.get(reverse('notifications:companies'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['groups']), 1)
        self.assertEqual(resp.context['items'][0], company)