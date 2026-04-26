
from constants import CHOICE_EMOJIS, RESULT_WIN, RESULT_LOSE, RESULT_DRAW

def show_welcome():
    print("=" * 40)
    print("   🎮 ROCK PAPER SCISSORS GAME 🎮")
    print("=" * 40)
    print("Type 'quit' anytime to exit.\n")

def show_choices():
    print("\nYour choices:  🪨 rock  |  📄 paper  |  ✂️  scissors")

def show_round_result(player_choice, bot_choice, result, scores):
    p_emoji = CHOICE_EMOJIS[player_choice]
    b_emoji = CHOICE_EMOJIS[bot_choice]

    print(f"\n  You   → {p_emoji}  {player_choice.upper()}")
    print(f"  Bot   → {b_emoji}  {bot_choice.upper()}")
    print("-" * 30)

    if result == RESULT_WIN:
        print("  ✅ You WIN this round!")
    elif result == RESULT_LOSE:
        print("  ❌ You LOSE this round!")
    else:
        print("  🤝 It's a DRAW!")

    print(f"\n  Score → You: {scores['player']}  |  Bot: {scores['bot']}  |  Draws: {scores['draws']}")

def show_final_result(scores):
    print("\n" + "=" * 40)
    print("         🏁 GAME OVER")
    print("=" * 40)
    print(f"  Your wins  : {scores['player']}")
    print(f"  Bot wins   : {scores['bot']}")
    print(f"  Draws      : {scores['draws']}")
    print("-" * 40)

    if scores["player"] > scores["bot"]:
        print("  🏆 Overall Winner: YOU! Great game!")
    elif scores["bot"] > scores["player"]:
        print("  🤖 Overall Winner: BOT! Better luck next time.")
    else:
        print("  🤝 It's an overall DRAW!")
    print("=" * 40)

def show_invalid_input():
    print("  ⚠️  Invalid choice! Please type rock, paper, or scissors.")
