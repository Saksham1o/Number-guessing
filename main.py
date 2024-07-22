import random

def show_score(attempts_list):
    """Displays the current best score."""
    if not attempts_list:
        print('There is currently no best score, it\'s yours for the taking!')
    else:
        print(f'The current best score is {min(attempts_list)} attempts')


def start_game():
    """Starts the number guessing game."""
    attempts_list = []

    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(f'Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        return

    while True:
        attempts = 0
        rand_num = random.randint(1, 10)
        show_score(attempts_list)

        while True:
            try:
                guess = int(input('Pick a number between 1 and 10: '))
                if guess < 1 or guess > 10:
                    raise ValueError('Please guess a number within the given range')

                attempts += 1

                if guess == rand_num:
                    attempts_list.append(attempts)
                    print('Nice! You got it!')
                    print(f'It took you {attempts} attempts')
                    break
                else:
                    if guess > rand_num:
                        print('It\'s lower')
                    elif guess < rand_num:
                        print('It\'s higher')

            except ValueError as err:
                print('Oh no!, that is not a valid value. Try again...')
                print(err)

        wanna_play = input('Would you like to play again? (Enter Yes/No): ')
        if wanna_play.lower() != 'yes':
            print('That\'s cool, have a good one!')
            break


if __name__ == '__main__':
    start_game()