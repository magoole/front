import sys
import flask
from flask import Flask

BACKEND_URL = open('.backendurl').read()
URL = sys.argv[1]
app = Flask('Magoole - Mes recherches, Mes données, Mes droits')


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/search')
def search():
    searched = flask.request.args.get('q')
    results = []
    return flask.render_template('search.html', search=searched, results=results)


@app.route('/ref')
def referencement():
    return flask.render_template('ref.html')


@app.route('/favicon.ico')
def fav():
    return flask.send_file('static/assets/logo_small_icon_only_inverted_blue.png')


def serverURL():
    return URL


app.jinja_env.globals.update(url=serverURL)


if __name__ == '__main__':
    print(f'URL: {URL}')
    app.run('0.0.0.0', port=15000, debug=True)
