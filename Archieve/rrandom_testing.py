from poker.utils import rank_hand


# hand1 = ["2H", "2D", "4C", "4D", "4S"]  # One Pair of 4D 6S 9H QH QC
# hand2 = ["9S", "9D", "3C", "3S", "3D"]  # One Pair of Eights 3D 6D 7H QD QS

def compare_hands(first_hand, second_hand):
    rank1 = rank_hand(first_hand)
    rank2 = rank_hand(second_hand)
    print(rank1, rank2)
    if rank1 > rank2:
        return "Player 1 wins!"
    elif rank2 > rank1:
        return "Player 2 wins!"
    else:
        return "It's a tie!"


hands = [
    (["2H", "2D", "4C", "4D", "4S"], ["4C", "4D", "4S", "9S", "9D"]),  # Full House
    (["5H", "5C", "6S", "7S", "KD"], ["2C", "3S", "5S", "5D", "TD"]),  # Pair vs Pair
    (["2D", "9C", "AS", "AH", "AC"], ["3D", "6D", "7D", "TD", "QD"]),  # Three of a Kind vs Flush
    (["4H", "4S", "4D", "8C", "8H"], ["3H", "3S", "3D", "KC", "KH"]),  # Full House vs Full House
    (["TD", "TH", "TC", "TS", "2D"], ["9D", "9H", "9C", "9S", "JD"]),  # Royal Flush vs Four of a Kind
    (["2H", "3D", "5S", "9C", "KD"], ["2C", "3H", "4S", "8C", "AH"]),  # High Card vs High Card
    (["4H", "4D", "QD", "QC", "5C"], ["4C", "4S", "QH", "QS", "5D"]),  # Two Pair vs Two Pair
    (["AS", "KS", "QS", "JS", "TS"], ["2H", "2D", "2S", "3C", "3D"]),  # Royal Flush vs Full House
    (["AH", "KH", "QH", "JH", "TH"], ["2D", "3H", "4C", "5D", "6S"]),  # Straight Flush vs Straight
    (["3H", "4H", "5H", "6H", "7H"], ["7S", "3S", "4S", "5S", "6S"]),  # Straight Flush vs Straight Flush
]

for i, (hand1, hand2) in enumerate(hands, 1):
    result = compare_hands(hand1, hand2)
    print(f"Hand {i}:")
    print(f"  Player 1: {hand1}")
    print(f"  Player 2: {hand2}")
    print(f"  Result: {result}\n")
