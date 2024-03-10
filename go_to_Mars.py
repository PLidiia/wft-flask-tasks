from flask import Flask
from flask import render_template

app = Flask('__main__')


@app.route('/answer')
@app.route("/auto_answer")
def content():
    dictionary = {
        'surname': 'Wathy',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал побывать на Марсе!',
        'ready': 'True',
        'title': 'Анкета'
    }
    return render_template('auto_answer.html', values=dictionary, title=dictionary['title'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
