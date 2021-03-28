import sys
import io
import unittest
from unittest.mock import patch

from game import snowman

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class TestSnowman(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_success_message_if_all_letters_guessed(self, mock_stdout):
        # Arrange
        input_letters = [
            'n',
            'a',
            'm',
            'w',
            'o',
            'n',
            's',
        ]

        # Act
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

          snowman('snowman')

        # Assert
        assert "you win" in mock_stdout.getvalue().lower()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_success_message_with_3_wrong_guesses_and_the_rest_right(self, mock_stdout):
        # Arrange
        input_letters = [
            's',
            'n',
            'b',
            'o',
            'w',
            'm',
            'a',
            'q',
            'v',
            'n',
        ]

        # Act
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

          snowman('snowman')

        # Assert
        assert "you win" in mock_stdout.getvalue().lower()  
        assert "sorry, you lose!  the word was snowman" not in mock_stdout.getvalue().lower()



    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_failure_message_with_7_straight_wrong_guesses(self, mock_stdout):
        # Arrange
        input_letters = [
            'b',
            'c',
            'p',
            'z',
            'q',
            'v',
            'x',
        ]

        # Act
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

          snowman('snowman')

        # Assert
        assert "you win" not in mock_stdout.getvalue().lower()  
        assert "sorry, you lose!  the word was snowman" in mock_stdout.getvalue().lower()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_failure_message_with_7_wrong_guesses_and_two_right(self, mock_stdout):
        # Arrange
        input_letters = [
            's',
            'b',
            'c',
            'p',
            'n',
            'z',
            'q',
            'v',
            'x',
        ]

        # Act
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

          snowman('snowman')

        # Assert
        assert "you win" not in mock_stdout.getvalue().lower()  
        assert "sorry, you lose!  the word was snowman" in mock_stdout.getvalue().lower()


    # Invalid letter please enter a single character.
if __name__ == '__main__':
    unittest.main()