import unittest


def product_function(a, b):
    result = a * b
    return result


class TestForFunction(unittest.TestCase):
    def test_product_function1(self):
        self.assertEqual(product_function(2, 3), 6)

    def test_product_function2(self):
        self.assertIs(product_function(2, 3), 5)

    def test_product_function3(self):
        self.assertTrue(product_function(2, 3) == 5,'not true')


#a=TestForFunction()
if __name__ == '__main__':

    unittest.main()