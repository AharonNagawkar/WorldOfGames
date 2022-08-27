from flask import Flask
import Utils

error_html_reply = \
    f'''<html>
	<head>
		<title>Scores Game</title>
	</head>
	<body>
		<h1>
			<div id="score" style="color:red">{Utils.BAD_RETURN_CODE} - File not found</div>
		</h1>
	</body>
</html>'''


def success_html_reply(players_scores):
    return \
        f'''<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is: 
                {players_scores}
            </h1>
        </body>
    </html>'''


app = Flask("WoG Scores")


@app.route('/')
def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME, 'r') as file:
            scores = file.read().splitlines()
            index = 1
            html_scores = ''
            for score in scores:
                html_scores += f'<div id="player{index}">{score}</div>'
                index += 1
            return success_html_reply(html_scores)

    except FileNotFoundError:
        return error_html_reply


app.run(host="0.0.0.0", port=5001, debug=False)

# scores = f'<div id="player1">15</div>'
# print(success_html_reply(scores))
# print(error_html_reply)

