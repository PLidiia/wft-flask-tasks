from flask import Flask
from flask import render_template


app = Flask('__main__')


@app.route('/training/<prof>')
def content(prof):
    return render_template('design.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
