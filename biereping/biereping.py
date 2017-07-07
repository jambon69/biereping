#!/usr/bin/env python

from functools import wraps
from flask import Flask, request, abort, render_template, redirect, url_for, session, flash, g
from flask_sqlalchemy import SQLAlchemy
import sys
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biereping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/create_event', methods=['GET'])
def create_event():
    return render_template('create_event.html', params={'name': 'michel', 'age': 20})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        args = request.form.to_dict()
        print args
        # TODO: real database lookup
        user = User.query.filter_by(username=args['username']).first()
        print user.password
        if user is None or args['password'] != user.password:
            flash('wrong username / password')
        else:
            session['logged_in'] = True
            session['pseudo'] = args['username']
        return render_template('index.html')
    return render_template('login.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['pseudo'] = ''
    return render_template('index.html')


@app.route('/event', methods=['POST'])
def add_event():
    args = request.form.to_dict()
    print args
    return render_template('index.html')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=8000)
