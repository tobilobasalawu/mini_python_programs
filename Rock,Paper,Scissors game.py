import random

com_points = 0
user_points = 0

def play():
    global user_points, com_points
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, or 'done' to quit: \n")
        
        if user == 'done':
            print("Game over. Total scores - You:", user_points, "Computer:", com_points)
            if user_points > com_points:
                print('You Won')
            else:
                print('Computer Won')
            break 
        
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            com_points += 5
            user_points += 5
            print("It's a tie")
            print("Your points =", user_points, "Computer Points = ", com_points)
        elif is_win(user, computer):
            user_points += 10
            print('You won!')
            print("Your points =", user_points, "Computer Points = ", com_points)
        else:
            com_points += 10
            print('You lost!')
            print("Computer points =", com_points, "User Points = ", user_points)

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

play()
