import pymysql


class Connection:
    def __init__(self, host, port,user, password, db):
        self.db = pymysql.connect(
            host=host,
            port = port,
            user=user,
            password=password,
            db=db
        )
        self.cursor = self.db.cursor()

    def ex_query(self, query):
        self.cursor.execute(query)
        return self.cursor

    def disconnect(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
