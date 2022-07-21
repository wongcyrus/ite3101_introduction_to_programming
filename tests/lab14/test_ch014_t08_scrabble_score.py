import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t08_scrabble_score_ans import scrabble_score
        else:
            from lab.lab14.ch014_t08_scrabble_score import scrabble_score
        self.assertEqual(15, scrabble_score("HeyYou"))
        self.assertEqual(10, scrabble_score("reverse"))
        self.assertEqual(7, scrabble_score("abc"))
        self.assertEqual(20, scrabble_score("uiuhjk"))
        self.assertEqual(0, scrabble_score(""))


if __name__ == '__main__':
    unittest.main()
