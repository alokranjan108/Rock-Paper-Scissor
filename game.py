
from constants import WIN_CONDITIONS, RESULT_WIN, RESULT_LOSE, RESULT_DRAW

def check_winner(player_choice, bot_choice):
   
    if player_choice == bot_choice:
        return RESULT_DRAW

    if WIN_CONDITIONS[player_choice] == bot_choice:
        return RESULT_WIN

    return RESULT_LOSE
