import random

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return 'You win!'

    return 'You lost!'

# Start the game
print(play())
