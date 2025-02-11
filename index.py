from flask import Flask, render_template
import perguntas  # Importa o arquivo perguntas.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', categories=perguntas.quiz_data.keys())

@app.route('/quiz/<category>')
def quiz(category):
    if category in perguntas.quiz_data:
        questions = perguntas.quiz_data[category]
        return render_template('quiz.html', category=category, quiz=questions)
    else:
        return "Categoria não encontrada.", 404

if __name__ == '__main__':
    app.run(debug=True)