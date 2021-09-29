import mysql.connector as mysql


class Database:
    config = None
    connection = None
    cursor = None

    def __init__(self, **kwargs):
        self.config = kwargs
        self.config["autocommit"] = kwargs.get("autocommit", False)
        self.connect()
    
    def connect(self):
        self.connection = mysql.connect(
            host=self.config['host'],
            db=self.config['database'],
            user=self.config['user'],
            passwd=self.config['password']
        )
        self.connection.autocommit = self.config['autocommit']
        self.cursor = self.connection.cursor()
    
    def query(self, sqlQuery, params=None):
        self.cursor.execute(sqlQuery, params)
        return self.cursor
    
    def insert(self, table, info):
        columns = [key for key in info.keys()]
        values = [info[column] for column in columns]
        sqlQuery = 'INSERT INTO ' + table + ' '
        sqlQuery += str(columns).replace("'", "")
        sqlQuery += ' VALUES ' + str(values) + ";"
        sqlQuery = sqlQuery.replace('[', '(').replace(']', ')')
        return self.query(sqlQuery)

    def select(self, table=None, fields=None, where=None):
        sqlQuery =  "SELECT %s FROM `%s`" % (",".join(fields), table)
        if where and len(where) > 0:
            sqlQuery += " WHERE %s " % where[0]
        params = None
        if where and len(where)>1:
            params = where[1]
        return self.query(sqlQuery, params)
    
    def getAll(self, table=None, fields='*', where=None):
        cursor = self.select(table, fields, where)
        result = cursor.fetchall()
        rows = None
        if result:
            columns = [column[0] for column in cursor.description]
            rows = [dict(zip(columns, row)) for row in result]
        return rows
