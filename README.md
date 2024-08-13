# Poker Hand Evaluation

This project implements a poker hand evaluation system, which determines the winner between two players based on the hands they have. The system ranks hands according to standard poker rules and compares them to determine the winner.

## Project Structure

### 1. `poker/`
This directory contains the core logic and utilities for the poker hand evaluation.

- **`__init__.py`**: This file makes the directory a package, allowing you to import modules from it.
  
- **`game.py`**:
  - Contains the `Game` class which is responsible for processing the poker hands of two players and determining the winner.
  - The `Game` class keeps track of the number of wins for each player and any ties.
  - Key methods include:
    - `__init__(self, player1_cards: List[str], player2_cards: List[str])`: Initializes the game with two players' hands.
    - `get_winner(self) -> str`: Compares the hands of the two players and returns the winner ("1" for Player 1, "2" for Player 2, or "tie").
    - `get_player1_wins(cls) -> int`: Returns the total number of wins for Player 1.
    - `get_player2_wins(cls) -> int`: Returns the total number of wins for Player 2.
    - `get_tie(cls) -> int`: Returns the total number of ties.
  
- **`hand.py`**:
  - Contains the `Hand` class, which represents a poker hand.
  - The `Hand` class is used to rank a player's hand using the `rank_hand` function from the `utils.py` file.
  - Key methods include:
    - `__init__(self, cards: List[str])`: Initializes a hand with a list of cards and ranks them using `rank_hand`.
    - `__lt__(self, other: 'Hand') -> bool`: Compares two hands to determine which is lesser (used for ranking).
    - `__eq__(self, other: 'Hand') -> bool`: Checks if two hands are equal in rank.

- **`logger.py`**:
  - Contains a utility function to initialize and configure logging.
  - The `get_logger(name: str) -> logging.Logger` function:
    - Configures logging to save logs to a file with the format `poker_logs_{date_time_of_execution}.log` in the `logs/` directory.
    - The logs capture the details of the game, such as which player won each hand.

- **`utils.py`**:
  - Contains the `rank_hand` function, which is the core logic for ranking poker hands.
  - The `rank_hand(cards: List[str]) -> Tuple[int, List[int]]` function:
    - Analyzes a poker hand to determine its rank based on standard poker rules.
    - Returns a tuple with a numeric rank (e.g., 9 for a Straight Flush) and a list of sorted ranks to compare hands of the same type.

### 2. `run_poker.py`
- This script is the main entry point to run the poker hand evaluation.
- It reads poker hands from a file (e.g., `poker.txt`), processes them, and determines the winner for each hand.
- The results can be logged to a file based on the command-line argument provided (player 1, player 2, or ties).

### 3. `poker.txt`
- This file contains the hands dealt to each player in the game.
- Each line represents a separate game, with the first five cards belonging to Player 1 and the next five to Player 2.

### 4. `tests/`
- This directory contains unit tests to validate the correctness of the poker hand evaluation logic.
- **`test_game.py`**: Tests the functionality of the `Game` class.
- **`test_hand.py`**: Tests the functionality of the `Hand` class and `rank_hand` function.

## Getting Started

### Prerequisites
- Python 3.x
- Install dependencies from `requirements.txt` using `pip install -r requirements.txt`.

### Running the Poker Game
To run the poker hand evaluation:

```bash
python run_poker.py
