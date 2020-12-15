import unittest
from main import start


class testing(unittest.TestCase):
    def setUp(self) -> None:
        self.start = start()

    def test_is_inside(self):
        self.assertEqual(self.start)