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
        # sql1 = 'create table seat1 (id int PRIMARY KEY NOT NULL ,student NOT NULL)'
        # self.cur.execute(sql1)
        # self.con.commit()
        # sql2 = 'insert into seat1 SELECT * FROM seat'
        # self.cur.execute(sql2)
        # self.con.commit()
        sql3 = '''update seat set student = CASE id 
              WHEN id%2=0 THEN (SELECT student FROM seat1 WHERE seat1.id=seat.id-1) 
              WHEN id%2=1 THEN (SELECT student FROM seat1 WHERE seat1.id=seat.id+1) 
              END 
              '''
        self.cur.execute(sql3)
        self.con.commit()
        sql4 = 'select student from seat1 s1 where s1.id%2=0'
        self.cur.execute(sql4)

        print(self.cur.fetchall())
    def close_db(self):
        self.con.close()


if __name__ == '__main__':
    C = Connect_database()
    C.create_db()
    C.handle_db()
'''
    fail to solve,find answer from web:
    
    SELECT
    s.id,
    s.student
FROM
    (
        SELECT
            id - 1 AS id,
            student
        FROM
            seat
        WHERE
            (id % 2 = 0)
        UNION
            SELECT
                (CASE WHEN (cnt%2=1) AND id=cnt THEN id ELSE id + 1 END) AS id,
                student
            FROM
                seat,
                (select count(*) as cnt from seat) as seatcnt
            WHERE
                (id % 2 = 1)
    ) s
GROUP BY
    s.id ASC
    
well,wrong at first
ps: I still don't know reason why this is right answer
'''