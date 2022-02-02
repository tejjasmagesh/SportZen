#app.py
from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='mag26751!',database='hello')


cursor=con.cursor()
 
app = Flask(__name__)
      
app.secret_key = "caircocoders-ednalan"
      
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mag26751!'
app.config['MYSQL_DB'] = 'hello'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
      
@app.route('/')
def main(): 
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM creds")
    contacts = cur.fetchall()   
    return render_template('test.html', contacts=contacts)
     
@app.route('/delete', methods=['GET', 'POST'])
def delete():   
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST': 
        for getid in request.form.getlist('mycheckbox'):
            print(getid)
            cur.execute('DELETE FROM creds WHERE  username= "{}"'.format(getid))
            mysql.connection.commit()
        flash('Successfully Deleted!')
    return redirect('/')
         
if __name__ == '__main__':
    app.run(debug=True)

