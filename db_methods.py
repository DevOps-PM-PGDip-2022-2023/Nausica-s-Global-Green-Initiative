
import psycopg2

# change connection info
conn = psycopg2.connect(
    host="green-giants",
    database="GreenGiants",
    user="dbadmin",
    password="12345678ab")


def register_user(username=None, password=None):
    cur = conn.cursor()
    insert_stmt = (
        "INSERT INTO users (email, password, role) "
        "VALUES (%s, %s, %s)"
    )
    data = (username, password, "user")
    cur.execute(insert_stmt, data)


def patch_user(username=None, password=None, newuser=None, newpass=None):
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE email = %s"
    adr = (username, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        register_user(username, password)
    else:
        sql = "UPDATE users SET email = %s WHERE email = %s"
        val = (newuser, username)
        cur.execute(sql, val)


def remove_user(username=None, password=None):
    cur = conn.cursor()
    sql = "DELETE FROM users WHERE name = %s"
    adr = (username, )
    cur.execute(sql, val)


# todo: add,remove,update grants method

def add_grant(name=None, ammount=None):
    cur = conn.cursor()
    insert_stmt = (
        "INSERT INTO grants (name, ammount) "
        "VALUES (%s, %s)"
    )
    data = (name, ammount)
    cur.execute(insert_stmt, data)


def patch_grant(name=None, ammount=None, newname=None, newammount=None):
    cur = conn.cursor()
    sql = "SELECT * FROM grants WHERE name = %s"
    adr = (username, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        register_user(username, password)
    else:
        sql = "UPDATE grants SET name = %s WHERE name = %s"
        val = (newuser, username)
        cur.execute(sql, val)


def remove_grant(name=None, ammount=None):
    cur = conn.cursor()
    sql = "DELETE FROM grants WHERE name = %s"
    adr = (username, )
    cur.execute(sql, val)


def getall_grants():
    cur = conn.cursor()
    sql = "SELECT * FROM grants"
    cur.execute(sql)
    return cur.fetchall()
