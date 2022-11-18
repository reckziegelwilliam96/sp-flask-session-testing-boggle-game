from flask import Flask, request, render_template, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456789"
app.debug = True
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def index():
    """Show Homepage with Start Button"""
    return render_template("index.html")

@app.route('/home')
def display_game():
    """Show Game Board"""
    board = boggle_game.make_board()

    session["board"]=board
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)

    return render_template("home.html", board=board, highscore=highscore, plays=plays)

@app.route('/check-word')
def add_word_guess():
    """Get word guess from form, 
    check to see if its a valid word 
    from boggle functionality."""
    word = request.args['word']
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route('/post-score', methods=["POST"])
def post_score():
    """Add score to seciton under board and compare to high score
    if greater than high score, activate brokeRecord and switch to new highscore"""
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)

    session['plays'] = plays + 1
    session['highscore'] = max(score, highscore)
    return jsonify(brokeRecord=score > highscore)