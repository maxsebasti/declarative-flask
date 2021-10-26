from flask import Flask, request

app = Flask(__name__)

from app import routes

from app.database import db_session

@app.teardown_appcontext
def shutdown_session(exception = None):
    db_session.remove()
