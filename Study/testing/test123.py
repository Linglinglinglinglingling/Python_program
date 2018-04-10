import unittest


def add_number(a, b):
    return a + b


class TestForSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_number(1, 2), 3)


if __name__ == '__main__':
    t=TestForSum()