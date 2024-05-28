from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Questions et réponses pour le QCM
questions = [
    {
        "question": "Quel mot-clé est utilisé pour créer une fonction en Python?",
        "choices": ["function", "def", "func", "define"],
        "answer": "def"
    },
    {
        "question": "Comment créer une liste en Python?",
        "choices": ["list = {}", "list = []", "list = ()", "list = <>"],
        "answer": "list = []"
    },
    {
        "question": "Quel opérateur est utilisé pour l'exponentiation en Python?",
        "choices": ["^", "**", "%", "//"],
        "answer": "**"
    },
    {
        "question": "Comment créer une boucle infinie en Python?",
        "choices": ["while (1)", "while True", "while (true)", "for ( ; ; )"],
        "answer": "while True"
    },
    {
        "question": "Comment accéder à des éléments d'une liste en Python?",
        "choices": ["list(1)", "list[1]", "list{1}", "list<1>"],
        "answer": "list[1]"
    },

    
    {
        'question': 'Quelle est la sortie de ce code : print(2 ** 3) ?',
        'choices': ['6', '8', '9', '16'],
        'answer': '8'
    },
    {
        'question': 'Quelle est la sortie de ce code : print(3 == 3.0) ?',
        'choices': ['False', 'True', 'None', 'Erreur'],
        'answer': 'False'
    },
    {
        'question': 'Quelle est la sortie de ce code : print("python".islower()) ?',
        'choices': ['True', 'False', 'None', 'Erreur'],
        'answer': 'True'
    },
    {
        'question': 'Comment déclarer une variable x avec la valeur 10 en Python ?',
        'choices': ['int x = 10;', 'var x = 10;', 'x := 10;', 'x = 10;'],
        'answer': 'x = 10;'
    },
    {
        'question': 'Comment créer un commentaire sur une ligne en Python ?',
        'choices': ['/* Commentaire */', '// Commentaire', '# Commentaire', '– Commentaire'],
        'answer': '# Commentaire'
    }

]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('qcm', name=name))
    return render_template('index.html')

@app.route('/qcm/<name>', methods=['GET', 'POST'])
def qcm(name):
    if request.method == 'POST':
        score = 0
        for i, question in enumerate(questions):
            selected_answer = request.form.get(f'question-{i}')
            if selected_answer == question['answer']:
                score += 1
        return redirect(url_for('result', name=name, score=score))
    return render_template('qcm.html', name=name, questions=questions, enumerate=enumerate)

@app.route('/result/<name>/<int:score>')
def result(name, score):
    if score >= 8:
        message = "Excellent travail! 😜"
    elif score >= 5:
        message = "Bon travail, mais vous pouvez faire mieux! 😁"
    else:
        message = "Continuez à pratiquer, vous allez y arriver! 😉"

    return render_template('result.html', name=name, score=score, message=message)

if __name__ == '__main__':
    app.run(debug=True)