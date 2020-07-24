import unittest
from random_walk import Randomwalk

class UserTestCase(unittest.TestCase):
    """Tests for user rights"""
    def setUp(self):
        self.rw = Randomwalk(50_000)

    def test_user_rights_input(self):
        rw = self.rw.fill_walk()
        self.assertEqual(self.rw.num_points, len(self.rw.x_values))
        self.assertEqual(self.rw.num_points, len(self.rw.y_values))
    

if __name__ == '__main__':
    unittest.main()
