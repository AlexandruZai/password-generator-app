# Treasure Island Game

print("Welcome to the Treasure Island.\n"
      "Your mission is to find the treasure.")

move = input("Please make a move in order to advance. Type 'L' for left or 'R' for right -> ")
if move == 'L':
    print('You can move forward')
    second_move = input("You've come to a lake. There is an island in the middle of the lake\n"
                        "Swim or wait for the boat? Type 'swim' or 'wait' ").lower()
    if second_move == 'wait':
        print("Your boat has arrived.")
        choose_door = input("Please choose a door. Type 'red', 'yellow' or 'blue' -> ").lower()
        if choose_door == 'red':
            print("Burned by fire.\nGame Over")
        elif choose_door == 'yellow':
            print("You win! You have found the treasure!")
        elif choose_door == 'blue':
            print('Eaten by beasts.\nGame Over.')
        else:
            print("Game Over")
    elif second_move == 'swim':
        print("Attacked by trout.\nGame Over.")
    else:
        print("Attacked by trout.\nGame Over.")

elif move == 'R':
    print("Fall into a hole.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
