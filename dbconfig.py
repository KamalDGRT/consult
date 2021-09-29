from  db.db import Database

db = Database(
    host='localhost',
    user='root',
    password='Test@12345',
    database='consult',
    autocommit=True
)

print(db.config)
