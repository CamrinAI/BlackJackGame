# Blackjack (Terminal Game)

A simple command-line Blackjack game written in Python. The player draws cards to reach 21 without going over, while the dealer draws to 17 or higher.

## How to Run

1. Create a virtual environment (optional but recommended).
2. Install dependency: `pip install art`.
3. Run: `python main.py`.

## Project Functionality

- `deal_card()` returns a random card value (Ace starts as 11 and if the user is over 21 it will change to 1).
- `calculate_score()` totals a hand and handles blackjack (score 0) plus Ace reduction when busting.
- `play_game()` manages the game loop, user input, dealer logic, and win/lose/tie results.
- The bottom loop prompts to replay the game until the user exits.
