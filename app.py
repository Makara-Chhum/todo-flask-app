# app.py
from flask import Flask, request, render_template, redirect
import mysql.connector
import os
app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': os.environ["MYSQL_HOST"],
    'port': 3306,
    'user': os.environ["MYSQL_USER"],
    'password': os.environ["MYSQL_PASSWORD"],
    'database': os.environ["MYSQL_DATABASE"]
}
print(db_config)
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create the 'todos' table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INT AUTO_INCREMENT PRIMARY KEY, task TEXT)")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Root of the website"""
    if request.method == 'POST':
        task = request.form['task']
        cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
        conn.commit()

    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()

    return render_template('index.html', todos=todos)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    print(task)
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    conn.commit() 
    return redirect("/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
