
import psycopg2

#change connection info
try:
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="Abcd1234")
except:
    pass


def register_user(username = None, password = None):
    cur = conn.cursor()
    insert_stmt = (
    "INSERT INTO users (email, password, role) "
    "VALUES (%s, %s, %s)"
    )
    data = (username, password, "user")
    cur.execute(insert_stmt, data)


def patch_user(username = None, password = None, newuser = None, newpass = None):
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE email = %s"
    adr = (username, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        register_user(username,password)
    else:
        sql = "UPDATE users SET email = %s WHERE email = %s"
        val = (newuser, username)
        cur.execute(sql, val)

def remove_user(username = None, password = None):
    cur = conn.cursor()
    sql = "DELETE FROM users WHERE name = %s"
    adr = (username, )
    cur.execute(sql, adr)


#todo: add,remove,update grants method 

def add_grant(name = None, ammount = None):
    cur = conn.cursor()
    insert_stmt = (
    "INSERT INTO grants (name, ammount) "
    "VALUES (%s, %s)"
    )
    data = (name, ammount)
    cur.execute(insert_stmt, data)
    

def patch_grant(name = None, ammount = None, newname = None, newammount = None):
    cur = conn.cursor()
    sql = "SELECT * FROM grants WHERE name = %s"
    adr = (name, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        add_grant(name,ammount)
    else:
        sql = "UPDATE grants SET name = %s WHERE name = %s"
        val = (name, newname)
        cur.execute(sql, val)

def remove_grant(name = None, ammount = None):
    cur = conn.cursor()
    sql = "DELETE FROM grants WHERE name = %s"
    adr = (name, )
    cur.execute(sql, adr)


def getall_grants():
    cur = conn.cursor()
    sql = "SELECT * FROM grants"
    cur.execute(sql)
    return cur.fetchall()
