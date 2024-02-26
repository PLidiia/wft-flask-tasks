from flask import Flask
from flask import render_template

app = Flask('__main__')


@app.route('/list_prof/<type>')
def content(type):
    return render_template('index.html', type=type,
                           list_of_prof=['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                                         'инженер по терраформированию',
                                         'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                                         'инженер жизнеобеспечения',
                                         'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов'])


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)
