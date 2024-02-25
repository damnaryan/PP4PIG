import random

max_score = 50

def dice_roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        # 'input' by default stores a in string datatype, so when storing a number it needs to typecasted to int.
        if 2 <= players <= 4:
            break
        else: 
            print("The total number of players can be between 2 to 4.")
    else: 
        print("Enter a valid number.")

scoreboard = [0 for _ in range(players)]
# This is called list comprehension. Here the list comprises of 0's equal to the number of players.
# 'for' is a loop statement that loops 0 for times equal to the number of players.

score = 0
while max(scoreboard) < max_score :
    for plr_index in range(players):
        plr_index += 1
        print(f"\nPlayer {plr_index} is now playing.\n")
        while True:
            cmd = input("Do you want to roll the dice (Y/N): ").lower()
            if cmd == 'y':
                roll = dice_roll()
                if roll == 1:
                    scoreboard[plr_index] = 0
                    print(f"\nYou got 1! Your score is back to {scoreboard[plr_index]}")
                    break
                else:
                    score += roll
                    print(f"\nYou got {roll}! \n{roll} was added to your score. \nYour new score is {score}\n")
            elif cmd == 'n':
                quit()
            else:
                print("Enter a valid choice.")
        scoreboard[plr_index] = score
        print(f"Your final score is {scoreboard[plr_index]}.")

            

    

