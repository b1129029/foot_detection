import sqlite3

def view_patient_info():
    conn = sqlite3.connect('db\edema_measure.db')
    cursor = conn.cursor()
    query = '''
    SELECT * FROM `病患資料`
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def view_edema_info(patient_id):
    conn = sqlite3.connect('db\edema_measure.db')
    cursor = conn.cursor()
    query = '''
    SELECT `測量編號`, `測量時間`, `腳圍` FROM `水腫程度`
    WHERE `病患_ID` = ?
    '''
    cursor.execute(query, (patient_id,))
    results = cursor.fetchall()
    conn.close()
    print(query)
    return results

def search_line(search):
    conn = sqlite3.connect('db\edema_measure.db')
    cursor = conn.cursor()
    query = '''
    SELECT * FROM `病患資料` WHERE `等級` LIKE ?
    OR `病患_ID` LIKE ?
    OR `名字` LIKE ?
    OR `性別` LIKE ?
    OR `身高` LIKE ?
    OR `病患_LineID` LIKE ?
    '''
    search_param = f"%{search}%"
    cursor.execute(query, (search_param, search_param, search_param, search_param, search_param, search_param))
    results = cursor.fetchall()
    conn.close()
    return results