import CurrencyRouletteGame
import GuessGame
import MemoryGame
import Score


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game(name):
    games = ['Memory Game', 'Guess Game', 'Currency Roulette']

    selection = input('''
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
    \n''')

    while selection not in ['1', '2', '3']:
        selection = input('Wrong selection choose again:'
                          ' 1-Memory Game.'
                          ' 2-Guess Game.'
                          ' 3-Currency Roulette. \n')
    print(f"Your game is {games[int(selection)-1]}\n")

    difficulty = input("Please choose game difficulty from 1 to 5:\n")
    while difficulty not in ['1', '2', '3', '4', '5']:
        difficulty = input("Wrong input, select a number between 1-5\n")
    print(f"Your difficulty level is {difficulty}")

    if selection == '1':
        result = MemoryGame.play(difficulty)
    elif selection == '2':
        result = GuessGame.play(difficulty)
    else:
        result = CurrencyRouletteGame.play(difficulty)

    if result:
        Score.add_score(difficulty, name)
