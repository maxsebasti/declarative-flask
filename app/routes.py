from flask import Flask, request
from app import app
from app.database import db_session
from app.models import User

@app.route('/')
def index():
    if request.method == 'GET':
        users = User.query.all()
        results = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email
            } for user in users]

        return {"count": len(results), "users": results}
    else:
        return '<p>Hello World</p>'
