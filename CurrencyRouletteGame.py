import requests
from random import randint


def get_money_interval(difficulty, dollars):
    url = 'https://api.exchangerate.host/convert?from=USD&to=ILS'
    response = requests.get(url)
    currency_rate = float(response.json()['result'])
    low_margin = dollars * currency_rate - (5 - difficulty)
    high_margin = dollars * currency_rate + (5 - difficulty)
    return round(low_margin, 2), round(high_margin, 2)


def get_guess_from_user(dollar_currency):
    return float(input(f"How much do you think {dollar_currency}$ are in NIS?:\n"))


def play(difficulty_level):
    amount_in_dollars = randint(1, 100)
    money_range = get_money_interval(int(difficulty_level), amount_in_dollars)
    user_guess = get_guess_from_user(amount_in_dollars)
    bottom_margin = money_range[0]
    top_margin = money_range[1]

    if bottom_margin <= user_guess <= top_margin:
        return True
    else:
        return False
