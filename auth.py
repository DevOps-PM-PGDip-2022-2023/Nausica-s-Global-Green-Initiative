import psycopg2

def search(username = None, password = None):
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE email = %s"
    adr = (username, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        return True
    else:
        return False

def getrole(username = None, password = None):
    cur = conn.cursor()
    sql = "SELECT role FROM users WHERE email = %s"
    adr = (username, )
    cur.execute(sql, adr)
    resp = cur.fetchall()
    if len(resp)>1:
        return "user"
    else:
        return str(resp[0])

