import json
from database import Database
from database import Note

def extract_route(request):
    filename=''
    x = request.split()
    if len(x)>0:
        filename = x[1][1:]
    return filename

def read_file(archive):
    with open(archive, 'rb') as file:
        return file.read()

def load_data(): 
    db = Database('banco')
    notes = db.get_all()
    return notes

def load_template(archive):
    with open('templates/' + archive, 'r', encoding='utf-8') as file: 
        return file.read()

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}'
    if len(headers):
        response+= f'\n{headers}'

    response+= f'\n\n{body}'
    return response.encode()

def add(params):
    db = Database("banco")
    db.add(Note(id, params['title'], params['content']))

def delete(params):
    db = Database("banco")
    db.delete(params['id'])

def update(params):
    db = Database("banco")
    db.update(Note(title=params['titulo'], content=params['detalhes'], id=params['id']))
