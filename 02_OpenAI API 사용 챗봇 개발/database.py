# SQLite3 DB 읽고 쓰기 기능 구현 모듈
# Date: 2025-02-12  Author:GBH

import sqlite3

# DB 초기화
def init_db():
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')

    conn.commit() 
    conn.close() 

# 저장하기
def save_conversation(question,answer):
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO conversations (question, answer) VALUES (?, ?)
    ''', (question, answer))
    conn.commit() 
    conn.close()  

# 불러오기
def get_conversation():
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute('SELECT * FROM conversations')
    conversations = c.fetchall()
    conn.close()
    return conversations  

# 삭제하기
def delete_conversation(id_key=None,question=None):
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    
    if id_key :
        c.execute('''
            DELETE FROM conversations WHERE id = ?
            ''', (id_key,))
        conn.commit() 
    elif question:
        c.execute('''
            DELETE FROM conversations WHERE question = ?
            ''', (question,))
        conn.commit() 
    
    conn.close()   

if __name__ == '__main__':
    init_db()
    save_conversation('Hello','Hello! How can I assist you today?')
    # delete_conversation(id_key=1)
    # delete_conversation(question='Hello')    
    print(get_conversation())
