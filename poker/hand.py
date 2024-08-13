from poker.utils import rank_hand
from typing import List, Tuple


class Hand:
    """
    Represents a poker hand and provides methods to compare its rank with other hands.
    """

    def __init__(self, cards: List[str]) -> None:
        """
        Initialize a Hand instance with a list of cards and calculate its rank.

        Args:
            cards (List[str]): A list of 5 cards representing the player's hand.
        """
        self.cards: List[str] = cards
        self.rank: Tuple[int, List[int]] = rank_hand(cards)  # Rank of the hand, derived from the cards

    def __lt__(self, other: 'Hand') -> bool:
        """
        Compare this hand with another hand to determine if this hand has a lower rank.

        Args:
            other (Hand): Another Hand instance to compare against.

        Returns:
            bool: True if this hand's rank is lower than the other hand's rank, False otherwise.
        """
        return self.rank < other.rank

    def __eq__(self, other: 'Hand') -> bool:
        """
        Compare this hand with another hand to determine if they have equal rank.

        Args:
            other (Hand): Another Hand instance to compare against.

        Returns:
            bool: True if this hand's rank is equal to the other hand's rank, False otherwise.
        """
        return self.rank == other.rank
