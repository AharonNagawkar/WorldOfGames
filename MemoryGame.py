from random import randint
from time import sleep
from os import system


def generate_sequence(num_range):
    return [randint(1, 101) for _ in range(int(num_range))]


def get_list_from_user(num_range):
    print(f"Please enter your {num_range} guesses")
    return [int(input("Insert your guess and hit return\n")) for _ in range(int(num_range))]


def is_it_equal(cpu_list, user_list):
    return cpu_list == user_list


def play(difficulty_level):
    random_list = generate_sequence(difficulty_level)
    print(random_list)
    sleep(0.7)
    system('clear')
    user_guess = get_list_from_user(difficulty_level)
    return is_it_equal(random_list, user_guess)
