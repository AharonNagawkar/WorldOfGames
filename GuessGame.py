from random import randint


def generate_number(num_limit):
    return randint(1, int(num_limit))


def get_guess_from_user(num_limit):
    selection = input(f"Guess a number from 1 to {num_limit}\n")
    while selection not in [str(num) for num in range(1, num_limit+1)]:
        selection = input(f"Please select a number between 1 and {num_limit} only.\n")
    return selection


def compare_results(secret, user):
    return secret == int(user)


def play(difficulty_level):
    secret_number = generate_number(difficulty_level)
    user_numer = get_guess_from_user(difficulty_level)
    return compare_results(secret_number, user_numer)
