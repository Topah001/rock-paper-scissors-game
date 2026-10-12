"""Play Rock-Paper-Scissors and keep score for the current session."""

import random

CHOICES = ("rock", "paper", "scissors")
_BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def round_outcome(player: str, computer: str) -> str:
    """Return 'win', 'loss', or 'tie' for a valid pair of moves."""
    player = player.strip().lower()
    computer = computer.strip().lower()
    if player not in CHOICES or computer not in CHOICES:
        raise ValueError("moves must be rock, paper, or scissors")
    if player == computer:
        return "tie"
    return "win" if _BEATS[player] == computer else "loss"


def play_round(player: str, computer: str | None = None) -> tuple[str, str]:
    """Return the computer's move and outcome; computer can be supplied in tests."""
    player = player.strip().lower()
    if player not in CHOICES:
        raise ValueError("move must be rock, paper, or scissors")
    computer = random.choice(CHOICES) if computer is None else computer.strip().lower()
    return computer, round_outcome(player, computer)


def main() -> None:
    scores = {"wins": 0, "losses": 0, "ties": 0}
    print("Rock-Paper-Scissors")
    while True:
        player = input("Choose rock, paper, or scissors (or q to quit): ").strip().lower()
        if player in ("q", "quit"):
            break
        if player not in CHOICES:
            print("Please enter rock, paper, scissors, or q.")
            continue
        computer, outcome = play_round(player)
        scores[{"win": "wins", "loss": "losses", "tie": "ties"}[outcome]] += 1
        print(f"You: {player} | Computer: {computer}")
        print({"win": "You win!", "loss": "Computer wins!", "tie": "It's a tie!"}[outcome])
        print(f"Session score — Wins: {scores['wins']}  "
              f"Losses: {scores['losses']}  Ties: {scores['ties']}\n")

    print(f"Final session score — Wins: {scores['wins']}  "
          f"Losses: {scores['losses']}  Ties: {scores['ties']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
