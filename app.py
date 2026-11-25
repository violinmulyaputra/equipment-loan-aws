# Setup
import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

# Database
def connect():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database="loanapp",
        ssl={"ca": "global-bundle.pem"},
        cursorclass=pymysql.cursors.DictCursor,
    )

# Routes
@app.get("/health")
def health():
    with connect() as db, db.cursor() as cur:
        cur.execute("SELECT * FROM equipment")
        return jsonify(status="ok", data=cur.fetchall())

# Run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
