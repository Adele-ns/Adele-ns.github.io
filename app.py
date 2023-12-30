from flask import Flask, render_template
from flask import request, jsonify
from flask import Flask
from models import db, Language
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    # Logique du jeu ici
    return render_template('game.html')


@app.route('/api/start_game', methods=['POST'])
def start_game():
    # Logique pour commencer une nouvelle partie
    # Retourner les informations initiales au format JSON
    return jsonify({
        'question_number': 1,
        'total_questions': 5,
        'audio_url': 'url_de_laudio',
        'language_options': ['francais', 'anglais', 'espagnol'],  # Exemple de langues
        'correct_language': 'francais'  # Exemple de réponse correcte
    })

@app.route('/api/check_answer', methods=['POST'])
def check_answer():
    # Logique pour vérifier la réponse de l'utilisateur
    # Retourner les informations sur la réponse au format JSON
    return jsonify({
        'is_correct': True,
        'correct_language': 'francais'
    })



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Remplacez par l'URI de votre base de données
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)