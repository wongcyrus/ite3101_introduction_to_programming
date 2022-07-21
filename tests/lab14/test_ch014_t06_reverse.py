import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t06_reverse_ans import reverse
        else:
            from lab.lab14.ch014_t06_reverse import reverse
        self.assertEqual("esrever", reverse("reverse"))
        self.assertEqual("cba", reverse("abc"))
        self.assertEqual("4321", reverse("1234"))
        self.assertEqual("", reverse(""))


if __name__ == '__main__':
    unittest.main()
