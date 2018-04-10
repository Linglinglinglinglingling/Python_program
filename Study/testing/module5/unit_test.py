import unittest
import calculate_gpa


class TestForgpa(unittest.TestCase):
    def test_valid(self):
       self.assertEqual(calculate_gpa.calculate_GPA(['A','B','C','D','F']),2)

    def test_invalid_int(self):
       self.assertEqual(calculate_gpa.calculate_GPA([1,'B']),-2)

    #boundary test
    def test_invalid_str(self):
       self.assertEqual(calculate_gpa.calculate_GPA(['A','A','A','A']),4)

    def test_boundary(self):
        self.assertEqual(calculate_gpa.calculate_GPA(['F','F','F','F']),0)



test=TestForgpa()