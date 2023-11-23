"""
SQLite 是一个 C 库，它提供了一个轻量级的基于磁盘的数据库，不需要单独的服务器进程，并允许使用 SQL 查询语言的非标准变体访问数据库。
一些应用程序可以使用 SQLite 进行内部数据存储。
还可以使用 SQLite 构建应用程序原型，然后将代码移植到更大的数据库，例如 PostgreSQL 或 Oracle。

"""
import sqlite3

from liubin import utils

# 调用在当前工作目录中sqlite3.connect()创建与数据库的连接tutorial.db，如果不存在则隐式创建
with sqlite3.connect(utils.get_data_dir() / "tutorial.db") as con:
    # 创建一个游标对象，该对象可以用来执行SQL语句
    cur = con.cursor()
    # 使用游标对象的execute()方法执行SQL语句
    cur.execute("SELECT SQLITE_VERSION()")
    # 使用游标对象的fetchone()方法获取查询结果
    data = cur.fetchone()
    # 打印查询结果
    print(f"SQLite version: {data}")

    # 创建数据表
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT)"
    )
    # 插入数据
    cur.execute("INSERT INTO users VALUES(1, 'John', '123456789')")
    cur.execute("INSERT INTO users VALUES(2, 'Adam', '987654321')")
    # 查询数据
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    print(data)
    # 更新数据
    cur.execute("UPDATE users SET phone = '123' WHERE id = 1")
    # 删除数据
    cur.execute("DELETE FROM users WHERE id = 2")
    # 查询数据
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    print(data)
