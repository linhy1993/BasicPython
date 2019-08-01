import pymysql


class Database():
    def __init__(self, truncate=False):
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test')
        self.cursor = self.db.cursor()
        if truncate:
            self.truncate_table()

    def close_db(self):
        self.db.close()

    def _execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print(sql)
            self.db.rollback()

    def insert_movie(self, name, stars, release_time, score):
        sql = "INSERT INTO movies(name, stars, release_time, score) " \
              "VALUES ('%s', '%s', '%s', '%s')" % (name, stars, release_time, score)
        self._execute(sql=sql)

    def truncate_table(self):
        sql = "TRUNCATE table movies;"
        self._execute(sql=sql)

    def search_name(self, name):
        sql = "SELECT * FROM movies WHERE name=('%s');" % (name)
        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        name, stars, release_time, score = results[0], results[1], results[2], results[3]
        return name, stars, release_time

