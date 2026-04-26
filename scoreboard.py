
def create_scoreboard():
  
    return {"player": 0, "bot": 0, "draws": 0}

def update_score(scores, result):

    if result == "win":
        scores["player"] += 1
    elif result == "lose":
        scores["bot"] += 1
    else:
        scores["draws"] += 1
