import sqlite3
from dataclasses import dataclass

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database:
    def __init__ (self, name_bd):
        # corpo do construtor
        self.conn = sqlite3.connect(f'{name_bd}.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')

    def add(self,note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista_note = []

        for linha in cursor:
            identificador = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(identificador, title, content)
            lista_note.append(note)
        return lista_note

    def update(self, entry):
        self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}")
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
            
        


