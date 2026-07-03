import random
# -1 stands for Snake, 0 stands for Water and 1 stands for Gun
s='''Snake Water Gun
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors"
where player uses hand gestures to represent a snake, water or a gun. The gun
beats the snake, the water beats the gun, and the snake beats the water'''
print(s)
def Game(player,computer):
    if player == 'Snake':
        if computer == -1:
            print("I choose Snake\nIt's a Draw")
        elif computer == 0:
            print("I choose Water\nYou Win")
        else:
            print("I choose Gun\nYou Loose")
    elif player == 'Water':
        if computer == -1:
            print("I choose Snake\nYou Loose")
        elif computer == 0:
            print("I choose Water\nIt's a Draw")
        else:
            print("I choose Gun\nYou Win")
    elif player == 'Gun':
        if computer == -1:
            print("I choose Snake\nYou Win")
        elif computer == 0:
            print("I choose Water\nYou Loose")
        else:
            print("I choose Gun\nIt's a Draw")
a = True
while a:
    print("\nNow please choose between Snake, Water and Gun")
    player = input()
    computer = random.randint(-1, 1)
    Game(player, computer)
    print("Do you want to play Snake Water Gun Game again??")
    answer = input()
    if answer == 'Yes':
        a = True
    else:
        a = False