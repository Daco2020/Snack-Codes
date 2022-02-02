import pymysql
from config import DATABASE


class SnackDelete():
    def select_all():
        db_class = Connector()
        sql = "SELECT id, name FROM snack_delete WHERE is_del = 0"
        rows = db_class.execute_all(sql)
        return rows

    def delete_physics(id):
        db_class = Connector()
        sql = "DELETE FROM snack_delete WHERE id = (%s)"
        db_class.execute(sql, id)
        db_class.commit()

    def delete_logical(id):
        db_class = Connector()
        sql = "UPDATE snack_delete SET is_del = 1 WHERE id = (%s)"
        db_class.execute(sql, id)
        db_class.commit()


class Connector():
    def __init__(self):
        self.db = pymysql.connect(**DATABASE)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    # 단일 인서트
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    # 벌크 인서트(추가)
    def execute_many(self, query, args={}):
        self.cursor.executemany(query, args)

    # 한번에 한 row
    def execute_one(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    # 모든 row
    def execute_all(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
