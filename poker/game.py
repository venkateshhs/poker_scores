from poker.hand import Hand
from poker.logger import get_logger

# Initialize a logger instance for the Game class
logger = get_logger(__name__)


class Game:
    """
    Game class to manage poker games between two players, including
    tracking the number of wins for each player and ties.
    """
    player1_wins: int = 0  # Tracks Player 1's wins across games
    player2_wins: int = 0  # Tracks Player 2's wins across games
    tie: int = 0  # Tracks the number of tie games

    def __init__(self, player1_cards: list[str], player2_cards: list[str]) -> None:
        """
        Initialize a Game instance with hands for Player 1 and Player 2.

        Args:
            player1_cards (list[str]): List of 5 cards representing Player 1's hand.
            player2_cards (list[str]): List of 5 cards representing Player 2's hand.
        """
        self.player1: Hand = Hand(player1_cards)
        self.player2: Hand = Hand(player2_cards)

    def get_winner(self) -> str:
        """
        Determines the winner of the game by comparing the hands of Player 1 and Player 2.

        Returns:
            str: "1" if Player 1 wins, "2" if Player 2 wins, or "tie!" if the game is a tie.
        """
        # Log the rank of each player's hand for debugging purposes
        logger.debug(f"Player 1 Rank: {self.player1.rank}, Player 2 Rank: {self.player2.rank}")

        # Compare hands and update win counters
        if self.player1 > self.player2:
            Game.player1_wins += 1
            return "1"
        elif self.player2 > self.player1:
            Game.player2_wins += 1
            return "2"
        else:
            Game.tie += 1
            return "tie!"

    @classmethod
    def get_player1_wins(cls) -> int:
        """
        Returns the total number of wins for Player 1.

        Returns:
            int: Number of games won by Player 1.
        """
        return cls.player1_wins

    @classmethod
    def get_player2_wins(cls) -> int:
        """
        Returns the total number of wins for Player 2.

        Returns:
            int: Number of games won by Player 2.
        """
        return cls.player2_wins

    @classmethod
    def get_tie(cls) -> int:
        """
        Returns the total number of tie games.

        Returns:
            int: Number of tie games.
        """
        return cls.tie
