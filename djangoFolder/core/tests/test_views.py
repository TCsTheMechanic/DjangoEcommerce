
# "emula um cliente"
from django.test import TestCase, Client
# biblioteca importada para podermos utilizar o nome das urls definidas no
# arquivo urls.py
from django.core.urlresolvers import reverse

class indexViewTestCase(TestCase):

    # sempre executa no inicio dos testes
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

        # sempre executa no final dos testes
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')
