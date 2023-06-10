from flask import Flask, Response, render_template
from lichess.format import PYCHESS
from dotenv import load_dotenv
import lichess.api
import chess.svg
import chess
import os

load_dotenv()

def generate_card():
    username = os.getenv("username")
    game_objs = lichess.api.user_games(username, max=1, format=PYCHESS)
    board = next(game_objs)
    return chess.svg.board(board.end().board(), size=350)

app = Flask(__name__)

@app.route("/")
def handle_all():
    svg = generate_card()
    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"

    return resp

if __name__ == "__main__":
    app.run(debug=True)