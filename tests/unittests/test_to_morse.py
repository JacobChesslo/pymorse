import unittest
from pymorse import to_morse


class TestToMorse(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(
            '.... . .-.. .-.. ---    .-- --- .-. .-.. -..',
            to_morse('HELLO WORLD'),
            'Simple String Test Failed'
        )
        self.assertEqual(
            '.... . .-.. .-.. ---    .-- --- .-. .-.. -..',
            to_morse('Hello World'),
            'Simple String Test With Title Failed'
        )


if __name__ == '__main__':
    unittest.main()
