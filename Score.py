import Utils


def data_reconstruction(data, difficulty, player):
    players_score = {}
    for score in data:
        name = score.split(' = ')[0][0].upper() + score.split(' = ')[0][1:].lower()
        points = score.split(' = ')[1]
        players_score[name] = int(points)

    if player[0].upper() + player[1:].lower() in list(players_score.keys()):
        players_score[(player[0].upper() + player[1:].lower())] += int(difficulty)*3 + 5
    else:
        players_score[(player[0].upper() + player[1:].lower())] = int(difficulty) * 3 + 5
    return [f'{key} = {players_score[key]}\n' for key in players_score]


def add_score(difficulty, player):
    try:
        with open(Utils.SCORES_FILE_NAME, 'r+') as file:
            scores = file.read().splitlines()
            new_scores = data_reconstruction(scores, difficulty, player)
            file.seek(0)
            file.writelines(new_scores)

    except FileNotFoundError:
        with open(Utils.SCORES_FILE_NAME, 'w') as file:
            file.write(f'{player[0].upper()+player[1:].lower()} = {int(difficulty)*3 + 5}')
