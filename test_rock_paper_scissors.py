import unittest
from unittest.mock import patch

from rock_paper_scissors import CHOICES, play_round, round_outcome


class RockPaperScissorsTests(unittest.TestCase):
    def test_all_outcomes(self):
        self.assertEqual(round_outcome("rock", "scissors"), "win")
        self.assertEqual(round_outcome("paper", "scissors"), "loss")
        self.assertEqual(round_outcome("Scissors", "SCISSORS"), "tie")

    def test_rejects_invalid_moves(self):
        with self.assertRaises(ValueError):
            round_outcome("lizard", "rock")
        with self.assertRaises(ValueError):
            play_round("rock", "lizard")

    def test_play_round_uses_random_choice(self):
        with patch("rock_paper_scissors.random.choice", return_value="scissors") as choose:
            computer, result = play_round("rock")
        choose.assert_called_once_with(CHOICES)
        self.assertEqual((computer, result), ("scissors", "win"))


if __name__ == "__main__":
    unittest.main()
