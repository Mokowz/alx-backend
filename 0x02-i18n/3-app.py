#!/usr/bin/env python3
"""Get locale module"""
import babel
from flask import Flask, render_template ,request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Get language code from config"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
   """Home function"""
   return render_template('2-index.html')


if __name__ == '__main__':
   app.run(debug=True)
