from inner_module_def_datastruct import AUTHOR, AGE, WEIXIN_URL, CSDN_URL
import sqlite3

def practice_sqlite():
    # 连接数据库
    conn = sqlite3.connect(AUTHOR)

    # 获取游标
    c = conn.cursor()

    # 创建表格
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER,
                  address TEXT);''')

    # 插入数据
    # c.execute(f"INSERT INTO users (name, age, address) VALUES ('{AUTHOR}', '{AGE}', '{WEIXIN_URL}')")

    # 更新数据
    # c.execute("UPDATE users SET age=?,name=?,address=? WHERE id=2", (22, 'Cramer', CSDN_URL))

    # 删除数据
    c.execute("DELETE FROM users WHERE name=?", ('SteveRocket',))

    # 查询数据
    c.execute("SELECT * FROM users")
    result = c.fetchall()
    print(result)

    # 提交更改
    conn.commit()

    # 关闭连接
    conn.close()


class BooKManager:
    def __init__(self):
        # 连接数据库
        self.conn = sqlite3.connect(AUTHOR)

        # 获取游标
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS category
              (id int primary key, sort int, name text)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS book
              (id int primary key, 
               sort int, 
               name text, 
               price real, 
               category int,
               FOREIGN KEY (category) REFERENCES category(id))''')

        self.conn.commit()
        self.conn.close()

    def insert_data(self):
        self.c.execute("INSERT INTO category VALUES (1, 1, 'fpga')")
        self.c.execute("INSERT INTO category VALUES (?, ?, ?)", (2, 2, 'python'))

        books = [(1, 1, '基于FPGA的数字图像处理原理及应用', 53.12, 1),
                 (2, 3, 'Python技术手册(第2版)', 47.5, 2),
                 (3, 2, 'Python设计模式第2版', 63.6, 2),
                 ]

        self.c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)

        self.conn.commit()
        self.conn.close()

    def select_data(self):
        self.c.execute('SELECT sort,name,price FROM book ORDER BY sort')
        print(self.c.fetchone())  # 返回第一条数据：(1, '基于FPGA的数字图像处理原理及应用', 53.12)
        print(self.c.fetchone())  # 返回第二条数据：(2, 'Python设计模式第2版', 63.6)

        print(self.c.fetchall())  # 返回所有数据：[(1, '基于FPGA的数字图像处理原理及应用', 53.12), (2, 'Python设计模式第2版', 63.6), (3, 'Python技术手册(第2版)', 47.5)]

        print(self.c.fetchmany(2))  # 返回指定条数数据：[(1, '基于FPGA的数字图像处理原理及应用', 53.12), (2, 'Python设计模式第2版', 63.6)]


        self.c.execute('SELECT * FROM book WHERE book.category=2')
        print(self.c.fetchall())

        for row in self.c.execute('SELECT name, price FROM book ORDER BY sort'):
            print(row)

    def update_delete_data(self):
        # 更新id为1的书籍价格为88.88
        self.c.execute('UPDATE book SET price=? WHERE id=?', (88.88, 1))
        # 删除id为2的书籍数据
        self.c.execute('DELETE FROM book WHERE id=2')

        self.conn.commit()
        self.conn.close()

        # self.c.execute('DROP TABLE book')  # 直接删除整张表

if __name__ == '__main__':
    bm = BooKManager()
    # bm.insert_data()
    # bm.select_data()
    bm.update_delete_data()