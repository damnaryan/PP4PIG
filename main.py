import random

MAX_SCORE = 50

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("How many players are playing the game? (2-4): ")
    if players.isdigit():
        players = int(players)
        # 'input' by default stores a in string datatype, so when storing a number it needs to typecasted to int.
        if 2 <= players <= 4:
            break
        else: print("Only 2 to 4 players can play this game.")
    else: print("Enter a valid number.")

scoreboard = [0 for _ in range(players)]
# This is called list comprehension. Here the list comprises of 0's equal to the number of players.
# 'for' is a loop statement that loops 0 for times equal to the number of players.
player_idx = 0
player_num = 0

def result():
    win_score = max(scoreboard)
    print(f"Player {scoreboard.index(win_score) + 1} won the game!\n")
    quit()

while max(scoreboard) < MAX_SCORE:
    for player_idx in range(players):
        player_num = player_idx + 1
        print(f"\nPlayer {player_num} is now playing.\n")
        while max(scoreboard) < MAX_SCORE:
            cmd = input("Do you want to roll the dice?(Y/N): ").lower()
            if cmd == 'y':
                score = roll()
                if score == 0:
                    scoreboard[player_idx] = 0
                    print("Your score is back to 0")
                    break
                else: 
                    scoreboard[player_idx] += score
                    print(f"\n{score} was added to your score.\nYour new total is {scoreboard[player_idx]}\n")
            elif cmd == 'n': break
            else: print("\nEnter a valid response (Y/N).\n")
        print(f"\nSCOREBOARD: {scoreboard}\n")
        if scoreboard[player_idx] >= MAX_SCORE:
                result()