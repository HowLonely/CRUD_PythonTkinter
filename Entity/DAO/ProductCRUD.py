from Entity.DTO.Connection import Connection

host = 'localhost'
port = 3307
user = 'root'
password = ''
db = 'sistemacrud'


def insert(prod):
    try:
        con = Connection(host, port, user, password, db)
        query = "INSERT INTO `productos` VALUES (NULL, '{}', '{}', '{}', '{}', '{}');"\
            .format(prod.name, prod.price, prod.date, prod.category, prod.id_user)
        con.ex_query(query)
        con.commit()

        con.disconnect()

    except Exception as e:
        print(e)


def modify(product):
    try:
        con = Connection(host, port, user, password, db)
        query = "UPDATE `productos` SET `nombre` = '{}', `precio` = '{}', `fecha_ingreso` = '{}', `id_categoria` = '{}' " \
                "WHERE `productos`.`id_producto` = {} AND `productos`.`id_usuario` = {};"\
            .format(product.name, product.price, product.date, product.category, product.id_prod, product.id_user)

        #print(product.name, product.price, product.date, product.category, product.id_prod, product.id_user)

        con.ex_query(query)
        con.commit()

        con.disconnect()

    except Exception as e:
        print(e)


def delete(id):
    try:
        con = Connection(host, port, user, password, db)
        query = 'DELETE FROM productos WHERE id_producto={}'.format(id)
        con.ex_query(query)
        con.commit()

        con.disconnect()

    except Exception as e:
        print(e)


def show_all():
    try:
        con = Connection(host, port, user, password, db)
        query = 'select * from productos'

        cursor = con.ex_query(query)
        data = cursor.fetchall()
        con.disconnect()
        return data

    except Exception as e:
        con.rollback()
        print(e)


def show_one(id):
    try:
        con = Connection(host, port, user, password, db)
        query = 'select * from productos where id_producto={}'.format(id)
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
        query = 'select * from productos'
        cursor = con.ex_query(query)
        data = cursor.fetchmany(size=quantity)
        con.disconnect()
        return data
    except Exception as e:
        con.rollback()
        print(e)

def show_category():
    try:
        con = Connection(host, port, user, password, db)
        query = 'select * from categorias'

        cursor = con.ex_query(query)
        data = cursor.fetchall()
        con.disconnect()
        return data

    except Exception as e:
        con.rollback()
        print(e)

def show_one_categ(id):
    try:
        con = Connection(host, port, user, password, db)
        query = 'select * from categorias where id_categoria={}'.format(id)
        cursor = con.ex_query(query)
        data = cursor.fetchone()
        con.disconnect()
        return data
    except Exception as e:
        con.rollback()
        print(e)

def show_categ_by_name(categ):
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from categorias where nombre='{}';".format(categ)
        cursor = con.ex_query(query)
        data = cursor.fetchone()
        con.disconnect()
        return data
    except Exception as e:
        con.rollback()
        print(e)