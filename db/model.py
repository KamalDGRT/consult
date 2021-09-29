from .dbconfig import db

class Model:
    def __init__(self):
        self._db = db
        self._table = ''
    
    def select(self, fields='*', where = None):
        return db.select(self._table, fields, where)

    def insert(self, info):
        return db.insert(self._table, info)
