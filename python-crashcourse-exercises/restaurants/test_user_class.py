import unittest
from user_rights import User

class UserTestCase(unittest.TestCase):
    """Tests for user rights"""

    def test_user_rights_input(self):
        test_user = User(first_name="Jan", last_name="Kowalski")
        name_test_user = test_user.describe_user()
        self.assertEqual(name_test_user, 'Jan Kowalski')


if __name__ == '__main__':
    unittest.main()
