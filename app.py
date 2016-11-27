import server
from flask import Flask, render_template

app = Flask(__name__)

db = server.get_db()

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/create_account")
def create_account():
    return render_template('create_account.html')

@app.route("/soundboard")
def soundboard():
    return render_template('soundboard.html')

if __name__ == "__main__":
    app.run()