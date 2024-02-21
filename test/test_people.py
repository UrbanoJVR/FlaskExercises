import unittest
from app import app, people


class TestPeople(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_when_boss_is_python_should_show_all_employees(self):
        response = self.app.get('/people/python')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'HI PYTHON. SECRET NAMES OF YOUR TEAM', response.data)

        for name in people:
            self.assertIn(name.upper().encode(), response.data)

    def test_when_boss_is_conda_should_show_first_employee_only(self):
        response = self.app.get('/people/conda')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'HI CONDA. SECRET NAMES OF YOUR TEAM', response.data)
        self.assertIn(people[0].upper().encode(), response.data)

        for name in people[1:]:
            self.assertNotIn(name.upper().encode(), response.data)

    def test_whe_unknown_boss_should_not_show_employees(self):
        response = self.app.get('/people/unknown')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'YOU HAVE NO TEAM', response.data)

        for name in people:
            self.assertNotIn(name.upper().encode(), response.data)
