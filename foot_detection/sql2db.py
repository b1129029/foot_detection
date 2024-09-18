import os
import sqlite3 as sql3

def create_db(file) :
    sql = 'sql\\'+file+'.sql'
    db = 'db\\'+file+'.db'
    try :
        os.remove(db)
    except :
        pass
    conn = sql3.connect(db)
    cursor = conn.cursor()

    with open(sql, 'r', encoding="utf-8") as f:
        sql_command = f.read()

    command = sql_command.split(';')

    for com in command:
        com = com.strip()
        if com:
            cursor.execute(str(com))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    file = "edema_measure"
    create_db(file)