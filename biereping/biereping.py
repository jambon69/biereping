#!/usr/bin/env python

from flask import Flask, request, abort, render_template, redirect, url_for
import sys

app = Flask(__name__)


@app.route('/create_event', methods=['GET'])
def create_event():
        return render_template('create_event.html', params={'name':'michel', 'age':20})


@app.route('/event', methods=['POST'])
def add_event():
        args = request.form.to_dict()
        print args
        return render_template('index.html')

@app.route('/', methods=['GET'])
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
            
