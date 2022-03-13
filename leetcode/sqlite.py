import sqlite3
def getall():
    # print('>>>>>>....')
    conn = sqlite3.connect("problem.db")
    cur = conn.cursor()
    cur.execute("SELECT rowid, * FROM problems")
    a = cur.fetchall()
    conn.commit()
    conn.close()
    return a

def getuser(username):
    conn = sqlite3.connect("problem.db")
    cur = conn.cursor()
    cur.execute(f"SELECT rowid,*  FROM  admins   WHERE username = '{username}' ")
    userdata = cur.fetchone()
    conn.commit()
    conn.close()
    return userdata

def createuser(data):
    conn = sqlite3.connect("problem.db")
    cur = conn.cursor()
    cur.execute(f"insert into admins values {data}")
    conn.commit()
    conn.close()

def problem():
    print(">>>>>>>>>")
    conn = sqlite3.connect("problem.db")
    cur = conn.cursor()
    # cur.execute("CREATE table problems (Status VARCHAR ,Title VARCHAR,Solution VARCHAR(255 ),Acceptance int ,Difficulty VARCHAR )")
    cur.execute("SELECT * from problems ")
    c = cur.fetchall()
    conn.commit()
    conn.close()
    return c

def addproblem(data):
    conn = sqlite3.connect("problem.db")
    cur = conn.cursor()
    cur.execute(f"insert into problems values {data}")
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("problem.db")
    # print(">...",id)
    cur = conn.cursor()
    cur.execute(f"DELETE   FROM  problems   WHERE rowid LIKE {id} ")
    # deletedata = cur.fetchone()
    conn.commit()
    conn.close()
    # return deletedata


# conn = sqlite3.connect("problem.db")
# cur = conn.cursor()
# # cur.execute("CREATE table problems (Status VARCHAR ,Title VARCHAR,Solution VARCHAR(255 ),Acceptance int ,Difficulty VARCHAR , adminid INT  NOT NULL)")
# # cur.execute("CREATE table admins (firstname  VARCHAR,lastname VARCHAR, email VARCHAR , contact INT , username VARCHAR ,password VARCHAR    )")
# conn.commit()
# conn.close()
