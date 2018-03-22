import sqlite3


class Connect_database:
    def __init__(self):
        try:
            self.con = sqlite3.connect("change_seat.db")
            self.cur = self.con.cursor()
            print("connect successfully!")
            self.cur.execute('drop table seat')
            self.con.commit()
            self.create_table()
            print("init table successfully!")
        except:
            print('connect error!')

    def create_table(self):
        try:
            self.create_sql = 'CREATE table seat (id int primary key not null,student char(10));'
            self.cur.execute(self.create_sql)
            self.con.commit()
            print("create table successfully")
        except:
            print("create table error!")

    def insert_data(self, id, name):
        try:
            self.insert_sql = 'insert into seat VALUES (?,?)'
            self.cur.execute(self.insert_sql, (id, name))
            self.con.commit()
            print("insert to table successfully")
        except:
            print("create table failed!")

    def delete_db(self):
        try:
            self.cur.execute('drop table seat')
            self.con.commit()
            print("delete db finished!")
        except:
            print("delete fail!")

    def create_db(self):
        self.insert_data(1, "Abbot")
        self.insert_data(2, "Doris")
        self.insert_data(3, "Emersion")
        self.insert_data(4, "Green")
        self.insert_data(5, "Jeams")

    def handle_db(self):
        sql = 'select * from seat s1 WHERE s1.id%2=0'
    def close_db(self):
        self.con.close()


if __name__ == '__main__':
    C = Connect_database()
    C.create_db()
