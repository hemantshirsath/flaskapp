from flask import Flask, request, render_template, jsonify
# import mysql.connector 
import MySQLdb as sql_db


app = Flask(__name__)

db = sql_db.connect(
    host='localhost',
    user='root',
    password='student12345',
    database='test'
)


@app.route('/', methods=['GET'])
def get_word():
    cursor = db.cursor()
    cursor.execute('SELECT WORD from words LIMIT 1')
    word = cursor.fetchone()[0]
    cursor.close()
    data = {
        'Test': word
    }
    return jsonify(data)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        new_word = request.form['new_word']
        cursor = db.cursor()
        cursor.execute('UPDATE words SET WORD = %s ', (new_word,))
        db.commit()
        cursor.close()

    cursor = db.cursor()
    cursor.execute('SELECT WORD FROM words LIMIT 1')
    word = cursor.fetchone()[0]
    cursor.close()
    return render_template('admin.html', word=word)


app.run()
