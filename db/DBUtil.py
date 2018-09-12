import sqlite3


class sqlite:

    def __init__(self, datafile):
        self.conn = sqlite3.connect(datafile)

    def createConnection(datafile):
        conn = sqlite3.connect(datafile)

    def insert(self, sql, params):
        cursor = self.conn.cursor()
        print("Execute SQL :: {}".format(sql))

        sql = sql.format(*params)
        print("Execute SQL :: {}".format(sql))
        ret = ''
        try:
            ret = cursor.execute(sql)
            self.conn.commit()
        except Exception as ex:
            print("Exception : {}".format(ex))
            self.conn.rollback()

        return ret

    def select(self, sql, params):
        cursor = self.conn.cursor()

        sql = sql.format(*params)

        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as ex:
            print("Exception : {}".format(ex))