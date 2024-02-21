import unittest
from app import app, new_people


class TestNewPeople(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_when_boss_is_python_should_show_all_public_employees(self):
        response = self.app.get('/new_people/python')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You are the boss. You should know everyone's name. Keep them safe, and let no one else "
                      b"know.", response.data)

        for name in new_people:
            self.assertIn(name.upper().encode(), response.data)

    def test_when_boss_is_conda_should_show_first_public_employee_only(self):
        response = self.app.get('/new_people/conda')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You're not in charge here. Access is restricted to first name only.", response.data)
        self.assertIn(new_people[0].upper().encode(), response.data)

        for name in new_people[1:]:
            self.assertNotIn(name.upper().encode(), response.data)

    def test_whe_unknown_boss_should_not_show_public_employees(self):
        response = self.app.get('/new_people/unknown')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'YOU HAVE NO TEAM', response.data)

        for name in new_people:
            self.assertNotIn(name.upper().encode(), response.data)
