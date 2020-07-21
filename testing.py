import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_add5(self):
        test_param = 10
        result = main.add5(test_param)
        self.assertEqual(result, 15)

    def test_add5_2(self):
        test_param = "hello"
        result = main.add5(test_param)
        self.assertIsInstance(result, ValueError)

    def tearDown(self):
        print('cleaning up')
    
if __name__ == "__main__":
    unittest.main()