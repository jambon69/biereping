#!/usr/bin/env python

from flask import Flask, request, abort, render_template, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
            
