import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password=None,
    db='proyecto',
)



def queryDatos(user, contra):
    db.ping()
    sql = "SELECT * FROM clientes WHERE correo='"+str(user)+"'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:

        email=row[6]
        contrasenia=row[7]

        print(email)
        print(contrasenia)
        if email == user and contrasenia == contra:
            return True
        else:
            return False


def perfiluser(user):
    db.ping()
    dato=0
    sql = "SELECT * FROM clientes WHERE correo='"+str(user)+"'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        dato = row[1]
    return dato

def nombreuser(user):
    db.ping()
    sql = "SELECT * FROM clientes WHERE correo='" + str(user) + "'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        nombre = row[2]+" "+row[3]
    return nombre

def ciuser(user):
    db.ping()
    sql = "SELECT * FROM clientes WHERE correo='" + str(user) + "'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        ci = row[0]
    return ci

def listaproductosg():
    db.ping()
    sql = "SELECT * FROM productos "
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data
