#!/usr/bin/env python

from functools import wraps
from flask import Flask, request, abort, render_template, redirect, url_for, session, flash, g
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import sys
import os

MAPS_APIKEY = open("maps_apikey").read()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'bieredb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bieredb'


mongo = PyMongo(app)


@app.route('/event/<eventId>', methods=["GET"])
def show_event(eventId):
    events = mongo.db.events
    event = events.find_one({'_id': ObjectId(eventId)})
    return render_template('event.html', event=event)


@app.route('/events', methods=["GET"])
def show_events():
    events = mongo.db.events
    htmlEvent = []
    for event in events.find():
        print event
        htmlEvent.append(event)
    return render_template('events.html', events=htmlEvent)
        

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == "GET":
        return render_template('create_event.html', dom={'apikey': MAPS_APIKEY})
    args = request.form.to_dict()
    print args
    events = mongo.db.events
    event_id = events.insert({'event_name': args['event_name'], 'event_place': args['event_place']})
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        args = request.form.to_dict()
        users = mongo.db.users
        user = users.find_one({'username': args['username'], 'password': args['password']})
        print user
        if user is None:
            flash('wrong username / password')
        else:
            session['logged_in'] = True
            session['pseudo'] = args['username']
        return render_template('index.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    args = request.form.to_dict()
    users = mongo.db.users
    user_id = users.insert({'username': args['username'], 'password': args['password']})
    return render_template('index.html')


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
