import pytest
from poker.hand import Hand

def test_hand_ranking():
    hand = Hand(["5H", "5C", "6S", "7S", "KD"])
    assert hand.rank == [13, 7, 6, 5, 5]
