from flask import Flask
from flask import render_template

app = Flask('__main__')


@app.route('/<title>')
@app.route('/index/<title>')
def content(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
