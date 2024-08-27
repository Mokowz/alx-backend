#!/usr/bin/env python3
"""App module"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Default route function"""
    return render_template('0-index.html')
