from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os
from utils import money_sum


app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)

def init_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS money (
            id INT AUTO_INCREMENT PRIMARY KEY,
            amount INTEGER,
            message TEXT,
            type INTEGER          
        );
        ''')
        mysql.connection.commit()  
        cur.close()


@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT amount, message, type from money')
    datas = cur.fetchall()
    cur.close()
    data,earns,exps = money_sum(datas)
    return render_template("index.html", data = data, earns=earns, exps=exps)

@app.route("/submit", methods=["POST"])
def submit():
    amount = request.form.get('amount')
    type = request.form.get('type')
    msg = request.form.get('message')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO money (amount, message, type) VALUES (%s,%s,%s)',[amount, msg, type]) 
    mysql.connection.commit()  
    cur.close()  
    return redirect('/')
	
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000,debug=True)