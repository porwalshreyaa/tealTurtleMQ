import sqlite3


def create_client_list():
    con = sqlite3.connect("client_list.db")
    try:
        cur = con.cursor()
        cur.execute("CREATE TABLE client_session(username,password,role)")
        con.commit()
    except:
        print("oops-list!")
    finally:
        con.close()

def add_client(username,password, role):
    con = sqlite3.connect("client_list.db")
    try:
        cur = con.cursor()
        data = [(username, password,role)]
        cur.executemany(f"INSERT INTO client_session VALUES (?,?,?)", data)
        con.commit()
    except:
        print("oops-client!")
    finally:
        con.close()