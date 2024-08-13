import pytest
from poker.game import Game

def test_player2_wins():
    # Given poker hands
    player1_cards = ["5H", "5C", "6S", "7S", "KD"]  # Pair of Fives
    player2_cards = ["2C", "3S", "8S", "8D", "TD"]  # Pair of Eights

    # When the game is played
    game = Game(player1_cards, player2_cards)
    result = game.get_winner()
    print(result)
    # Then assert that Player 2 wins
    assert result == "Player 2 wins!", f"Expected 'Player 2 wins!', but got '{result}'"

if __name__ == "__main__":
    pytest.main()
