
from constants import CHOICES
from bot import get_bot_choice
from game import check_winner
from display import (
    show_welcome,
    show_choices,
    show_round_result,
    show_final_result,
    show_invalid_input,
)
from scoreboard import create_scoreboard, update_score


def get_player_choice():
    
    choice = input("\nYour move: ").strip().lower()
    if choice == "quit":
        return None
    return choice


def main():
    show_welcome()
    scores = create_scoreboard()

    while True:
        show_choices()
        player_choice = get_player_choice()

        
        if player_choice is None:
            break

        
        if player_choice not in CHOICES:
            show_invalid_input()
            continue

        
        bot_choice = get_bot_choice()

        
        result = check_winner(player_choice, bot_choice)

        
        update_score(scores, result)

       
        show_round_result(player_choice, bot_choice, result, scores)

        
        again = input("\n  Play another round? (y / n): ").strip().lower()
        if again != "y":
            break

    show_final_result(scores)


if __name__ == "__main__":
    main()
