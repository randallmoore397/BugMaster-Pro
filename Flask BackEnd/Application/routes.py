from app import app, db

@app.route("/")
def login():
    return "Login Page"