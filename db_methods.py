
import psycopg2

# change connection info
conn = psycopg2.connect(
    host="green-giants.cluster-cvyu518jf2zy.eu-west-1.rds.amazonaws.com",
    database="GreenGiants",
    user="dbadmin",
    password="12345678ab")


def check_db():
    cur = conn.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    data = cur.fetchall()
    if not "user" in data:
        try:
            cur.execute("CREATE TABLE users (email varchar PRIMARY KEY, password varchar, role varchar);")
        except:
            print("I can't create the table")
    if not "grant" in data:
        try:
            cur.execute("CREATE TABLE grants (name varchar PRIMARY KEY, ammount integer);")
        except:
            print("I can't create the table")
    seed_db()



def seed_db():
    cur = conn.cursor()
    query_user= """ INSERT INTO users (email, password, role) VALUES (%s,%s,%s)"""
    query_grant= """ INSERT INTO grants (name, ammount, site) VALUES (%s,%s,%s)"""
    user_data= [
        {
        "email":"admin@test.com",
        "password":"admin",
        "role":"admin"
        },
        {
        "email":"aidan@test.com",
        "password":"admin",
        "role":"admin"
        },
        {
        "email":"anuradha@test.com",
        "password":"admin",
        "role":"admin"
        },
        {
        "email":"rotimi@test.com",
        "password":"admin",
        "role":"admin"
        },
        {
        "email":"samantha@test.com",
        "password":"admin",
        "role":"admin"
        },
        {
        "email":"dean@test.com",
        "password":"admin",
        "role":"admin"
        }
        ]
    grant_data= [
        {
        "name":"Help to Buy Scheme",
        "ammount":30000,
        "site":"https://www.citizensinformation.ie/en/housing/owning_a_home/help_with_buying_a_home/help_to_buy_incentive.html"
        },
        {
        "name":"Future Growth Loan Scheme",
        "ammount":80000000,
        "site":"https://enterprise.gov.ie/en/What-We-Do/Supports-for-SMEs/Access-to-Finance/Future-Growth-Loan-Scheme/"
        }
        ]
    for i in user_data:
        record = (i['email'], i['password'], i['role'])
        cur.execute(query_user, record)
    for i in grant_data:
        record = (i['name'],i['ammount'],i['site'])
        cur.execute(query_grant, record)

check_db()

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
        val = (newuser, newpass)
        cur.execute(sql, val)


def remove_user(username=None):
    cur = conn.cursor()
    sql = "DELETE FROM users WHERE name = %s"
    adr = (username, )
    cur.execute(sql, adr)


# todo: add,remove,update grants method

def add_grant(name=None, ammount=None, site=None):
    cur = conn.cursor()
    insert_stmt = (
        "INSERT INTO grants (name, ammount, site) "
        "VALUES (%s, %s, %s)"
    )
    data = (name, ammount, site)
    cur.execute(insert_stmt, data)


def patch_grant(name=None, ammount=None, newname=None, newammount=None, newsite=None):
    cur = conn.cursor()
    sql = "SELECT * FROM grants WHERE name = %s"
    adr = (name, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        register_user(newname, newammount, newsite)
    else:
        sql = "UPDATE grants SET name = %s WHERE name = %s"
        val = (name, ammount)
        cur.execute(sql, val)


def remove_grant(name=None):
    cur = conn.cursor()
    sql = "DELETE FROM grants WHERE name = %s"
    adr = (name, )
    cur.execute(sql, adr)


def getall_grants():
    cur = conn.cursor()
    sql = "SELECT * FROM grants"
    cur.execute(sql)
    return cur.fetchall()

def search(username = None, password = None):
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE email = %s"
    adr = (username, )
    cur.execute(sql, adr)
    if len(cur.fetchall()) == 0:
        return True
    else:
        return False

def getrole(username = None):
    cur = conn.cursor()
    sql = "SELECT role FROM users WHERE email = %s"
    adr = (username, )
    cur.execute(sql, adr)
    resp = cur.fetchall()
    if len(resp)>1:
        return "user"
    else:
        return str(resp[0])
    
def data_load():

    pass