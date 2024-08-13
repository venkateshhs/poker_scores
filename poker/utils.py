from collections import Counter
from typing import List, Tuple


def rank_hand(cards: List[str]) -> Tuple[int, List[int]]:
    """
    Determine the rank of a poker hand.

    Args:
        cards (List[str]): A list of 5 cards in the format ['2H', '3D', '5S', '9C', 'KD'].

    Returns:
        Tuple[int, List[int]]: A tuple containing the rank category and a list of values that determines the hand's rank.

    The rank categories are:
        9: Straight Flush
        8: Four of a Kind
        7: Full House
        6: Flush
        5: Straight
        4: Three of a Kind
        3: Two Pair
        2: One Pair
        1: High Card
    """
    # Map card values to their corresponding integers.
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Convert the hand's card ranks into integers and sort in descending order.
    ranks = sorted([values[card[0]] for card in cards], reverse=True)

    # Extract the suits of the cards.
    suits = [card[1] for card in cards]

    # Count the frequency of each rank in the hand.
    rank_count = Counter(ranks)
    # Sort the rank frequencies in descending order.
    rank_freq = sorted(rank_count.values(), reverse=True)
    # Get the unique ranks sorted in descending order.
    unique_ranks = sorted(rank_count.keys(), reverse=True)

    # Check if all cards have the same suit.
    is_flush = len(set(suits)) == 1
    # Check if the ranks form a straight (consecutive values).
    is_straight = len(unique_ranks) == 5 and (unique_ranks[0] - unique_ranks[-1] == 4)
    # Special case: Check for Ace-low straight (A, 2, 3, 4, 5).
    is_ace_low_straight = ranks == [14, 5, 4, 3, 2]

    # Straight Flush
    if is_straight and is_flush:
        # Return rank 9 with the sorted ranks (special case for Ace-low straight).
        return 9, ranks if not is_ace_low_straight else [5, 4, 3, 2, 1]

    # Four of a Kind
    elif rank_freq == [4, 1]:
        # Return rank 8 with the rank of the quads first, followed by the kicker.
        quads_rank = [rank for rank, count in rank_count.items() if count == 4]
        kicker_rank = [rank for rank, count in rank_count.items() if count == 1]
        return 8, quads_rank + kicker_rank

    # Full House
    elif rank_freq == [3, 2]:
        # Return rank 7 with the rank of the trips first, followed by the pair.
        trips_rank = [rank for rank, count in rank_count.items() if count == 3]
        pair_rank = [rank for rank, count in rank_count.items() if count == 2]
        return 7, trips_rank + pair_rank

    # Flush
    elif is_flush:
        # Return rank 6 with the sorted ranks.
        return 6, ranks

    # Straight
    elif is_straight:
        # Return rank 5 with the sorted ranks (special case for Ace-low straight).
        return 5, ranks if not is_ace_low_straight else [5, 4, 3, 2, 1]

    # Three of a Kind
    elif rank_freq == [3, 1, 1]:
        # Return rank 4 with the rank of the trips first, followed by the kickers.
        return 4, unique_ranks

    # Two Pair
    elif rank_freq == [2, 2, 1]:
        # Return rank 3 with the ranks of the pairs first, followed by the kicker.
        pairs = sorted([rank for rank, count in rank_count.items() if count == 2], reverse=True)
        kicker = [rank for rank, count in rank_count.items() if count == 1]
        return 3, pairs + kicker

    # One Pair
    elif rank_freq == [2, 1, 1, 1]:
        # Return rank 2 with the rank of the pair first, followed by the kickers.
        pair_rank = [rank for rank, count in rank_count.items() if count == 2]
        kicker_ranks = sorted([rank for rank, count in rank_count.items() if count == 1], reverse=True)
        return 2, pair_rank + kicker_ranks

    # High Card
    else:
        # Return rank 1 with the sorted ranks.
        return 1, ranks
