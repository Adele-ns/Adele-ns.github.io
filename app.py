from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/game', methods=['GET', 'POST'])
def game():
    # Logique du jeu ici
    return render_template('game.html')


from flask import request, jsonify

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