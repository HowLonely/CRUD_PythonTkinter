from Entity.DTO.Connection import Connection

host = 'localhost'
port = 3307
user = 'root'
password = ''
db = 'sistemacrud'


def insert(u):
    try:
        con = Connection(host, port, user, password, db)
        query = "INSERT INTO usuarios values (NULL, '{}', '{}', '{}')".format(u.username, u.email, u.password)
        con.ex_query(query)
        con.commit()

        con.disconnect()

    except Exception as e:
        print(e)


def modify(user):
    try:
        con = Connection(host, port, user, password, db)
        query = ''

        con.ex_query(query)
        con.commit()

        con.disconnect()

    except Exception as e:
        print(e)


def delete(id):
    try:
        con = Connection(host, port, user, password, db)
        query = "DELETE FROM usuarios WHERE id_usuario={}".format(id)
        con.ex_query(query)
        con.commit()

        con.disconnect()

    except Exception as e:
        print(e)


def show_all():
    try:
        con = Connection(host, port, user, password, db)
        query = 'SELECT * FROM usuarios'

        cursor = con.ex_query(query)
        data = cursor.fetchall()
        con.disconnect()
        return data

    except Exception as e:
        con.rollback()
        print(e)


def show_one(username):
    try:
        con = Connection(host, port, user, password, db)
        query = "SELECT * FROM `usuarios` WHERE usuario='{}';".format(username)
        cursor = con.ex_query(query)
        data = cursor.fetchone()
        con.disconnect()
        return data
    except Exception as e:
        con.rollback()
        print(e)

def search_index(id):
    try:
        con = Connection(host, port, user, password, db)
        query = "SELECT * FROM `usuarios` WHERE id_usuario={};".format(id)
        cursor = con.ex_query(query)
        data = cursor.fetchone()
        con.disconnect()
        return data
    except Exception as e:
        con.rollback()
        print(e)


def show_many(quantity):
    try:
        con = Connection(host, port, user, password, db)
        query = 'select * from usuarios'
        cursor = con.ex_query(query)
        data = cursor.fetchmany(size=quantity)
        con.disconnect()
        return data
    except Exception as e:
        con.rollback()
        print(e)
