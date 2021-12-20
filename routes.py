import sys
import flask
import requests
from flask import Flask

BACKEND_URL = open('.backendurl').read()
URL = sys.argv[1]
app = Flask('Magoole - Mes recherches, Mes données, Mes droits')


def requestBackend(route, params: dict = {}):
    try:
        response = requests.get(BACKEND_URL + route, params=params).json()
        return response
    except:
        return {'code': 500, 'message': 'Something went wrong with the Magoole Brain'}


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/search')
def search():
    searched = flask.request.args.get('q')
    jsonBackendResponse = requestBackend('/search', params={'q': searched})
    if jsonBackendResponse['code'] != 200:
        return flask.render_template('error.html', error=jsonBackendResponse['message'], code=jsonBackendResponse['code'])
    results = jsonBackendResponse['results']
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
    print(f'BACKEND_URL: {BACKEND_URL}')
    app.run('0.0.0.0', port=15000, debug=True)
