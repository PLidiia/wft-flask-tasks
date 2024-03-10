from flask import Flask
from flask import render_template

app = Flask('__main__')


@app.route('/distribution')
def content():
    names = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('design_cabins.html', values=names, title='По каютам!')


if __name__ == '__main__':
    app.run(port=5015, host='127.0.0.1', debug=True)
