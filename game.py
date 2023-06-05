import random

# print('Welcome to my first game, name as Paper Scissor Rock')
# print('User have to select paper, scissor or rock')

while True:
    possible_action = ['PAPER', 'ROCK', 'SCISSOR']
    user_action = input('Enter your choice(paper, scissor or rock)')

    computer_action = random.choice(possible_action)

    print('Your choice is', user_action)
    print('The computer choice is', computer_action)

    if (user_action == computer_action):

        print('Its tie')
    elif (user_action == 'Paper'):
        if (computer_action == 'Scissor'):
            print('Scissor wins !! You loose')
        else:
            print('Paper Wins !! You won')
    elif (user_action == 'Rock'):
        if (computer_action == 'Paper'):
            print('Paper wins !! You loose')
        else:
            print('Rock wins !! You won')
    elif (user_action == 'Scissor'):
        if (computer_action == 'Rock'):
            print('Rock wins !! you loose')
        else:
            print('Scissor Wins !! You won')

        play_again = input('Play again ? (y/n):')
        if play_again.lower() != 'y':
            break
