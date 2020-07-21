import unittest
import random_game

class TestGame(unittest.TestCase):
    def test_correct_guess(self):
        answer = 5
        guess = 5
        result = random_game.run_guess(guess, answer)
        self.assertTrue(result)
    
    def test_wrong_guess(self):
        result = random_game.run_guess(3, 5)
        self.assertFalse(result)

    def test_out_of_bounds_guess(self):
        result = random_game.run_guess(11,5)
        self.assertFalse(result)
    
    def test_wrong_type(self):
        result = random_game.run_guess("3",5)
        self.assertIsInstance(result,ValueError)

if __name__ == '__main__':
    unittest.main()