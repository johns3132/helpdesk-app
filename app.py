from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# 🔧 Ścieżka do bazy (ważne na Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "tickets.db")


def get_db():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            problem TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        problem = request.form["problem"]

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (name, problem, status) VALUES (?, ?, ?)",
            (name, problem, "OPEN")
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("index.html")


@app.route("/admin")
def admin():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    conn.close()

    return render_template("admin.html", tickets=tickets)


@app.route("/close/<int:id>")
def close_ticket(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET status='CLOSED' WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/admin")


init_db()


if __name__ == "__main__":
    app.run(debug=True)
