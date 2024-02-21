import unittest
from app import app


class TestFormPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_when_load_page_should_not_show_info_box(self):
        response = self.app.get('/form')
        self.assertNotIn(b"Estos son los datos recopilados:", response.data)

    def test_form_submission(self):
        form_data = {
            'username': 'test_user',
            'email_username': 'test_email_username',
            'email_server': 'test_email_server',
            'description': 'test_description'
        }
        response = self.app.post('/form', data=form_data, follow_redirects=True)

        self.assertIn(b"Estos son los datos recopilados:", response.data)
        self.assertIn(b"Usuario: test_user", response.data)
        self.assertIn(b"Email: test_email_username@test_email_server", response.data)
        self.assertIn(b"Descripci\xc3\xb3n: test_description", response.data)
