import unittest
from pymorse import to_english


class TestToEnglish(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(
            'HELLO WORLD',
            to_english('.... . .-.. .-.. ---   .-- --- .-. .-.. -..'),
            'Simple String Test Failed'
        )
        self.assertEqual(
            'Hello World',
            to_english('.... . .-.. .-.. ---   .-- --- .-. .-.. -..', title=True),
            'Simple String Test With Title Failed'
        )


if __name__ == '__main__':
    unittest.main()
