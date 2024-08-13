import argparse
from poker.game import Game
from poker.logger import get_logger


def main() -> None:
    """
    Main function that reads poker hands from a file, processes them,
    and logs the results based on the command-line argument.

    The function logs how many hands Player 1, Player 2, or ties won,
    with Player 1 being the default if no argument is provided.
    """
    # Get logger instance from logging.py
    logger = get_logger(__name__)

    # Log the start of the program
    logger.info("Poker game started.")

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Determine the winner in Poker hands.")
    parser.add_argument(
        "player",
        type=int,
        choices=[1, 2, 3],
        nargs='?',  # Indicates that there can be 0 or more arguments in CLI
        default=1,
        help="Enter 1 for Player 1 wins (default), 2 for Player 2 wins, 3 for ties."
    )
    args = parser.parse_args()
    logger.debug(f"Finding total winning hands for player: {args.player}")

    # Read hands from poker.txt
    try:
        with open('poker.txt', 'r') as file:
            hands = file.readlines()
        logger.info(f"Successfully read {len(hands)} hands from poker.txt")
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return

    # Process each hand
    for index, hand in enumerate(hands, start=1):
        cards = hand.strip().split()
        player1_cards = cards[:5]  # First 5 cards are for Player 1
        player2_cards = cards[5:]  # Next 5 cards are for Player 2

        game = Game(player1_cards, player2_cards)
        winner = game.get_winner()
        logger.debug(
            f"Hand {index}: Player 1 cards: {player1_cards}, Player 2 cards: {player2_cards}. Winner: Player {winner}")

    # Log results based on command-line argument
    if args.player == 1:
        logger.info(f"Player 1 won {Game.player1_wins} hands.")
    elif args.player == 2:
        logger.info(f"Player 2 won {Game.player2_wins} hands.")
    elif args.player == 3:
        logger.info(f"There were {Game.tie} tie hands.")

    # Log the end of the program
    logger.info("Poker game finished.")


if __name__ == "__main__":
    main()
