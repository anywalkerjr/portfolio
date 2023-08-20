# Импорт
from flask import Flask, render_template, request, redirect
# Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Создание db
db = SQLAlchemy(app)

# Запуск страницы с контентом
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')
        return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)
    else:
        return render_template('index.html')

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)

@app.route('/feedback', methods=['POST'])
def add_feedback():
    email = request.form['email']
    text = request.form['text']

    feedback = Feedback(email=email, text=text)
    db.session.add(feedback)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)