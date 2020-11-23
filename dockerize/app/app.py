from typing import List, Dict
from flask import Flask
import mysql.connector as mc
import json

app = Flask(__name__)


def count(uid):
    con=None
    try:
        #con=mc.connect(host='localhost',database='visual_minds',user='root',password='root')

        con=mc.connect(host='db',port='3306',database='visual_minds',user='root',password='root')
        s='select count(userid) from mysql where userid=%s'
        userid=[uid]
        cursor=con.cursor()
        cursor.execute(s,userid)
        data=cursor.fetchall()
        for cnt in data:
            return (cnt[0])
    except mc.DatabaseError as de:
        print('Operation failed due to ',de)
    finally:
        if con:
            con.close()

    
@app.route('/')
def index1():
    return 'hello'

@app.route('/getvalue/<int:id1>')
def index(id1):
    temp = count(id1)
    return 'The total number of advertisements are %d' % temp


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)