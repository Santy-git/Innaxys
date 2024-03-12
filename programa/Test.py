import sqlite3 as s

tablas = [
    '''CREATE TABLE IF NOT EXISTS hotel (
        nombre varchar(50) not null,
        hab number(10) not null,
        pisos number(10) not null,
        capac number(10) not null
    );''',

    '''CREATE TABLE IF NOT EXISTS cochera (
        codCochera int primary key,
        estado varchar(50) not null
    );''',

    '''CREATE TABLE IF NOT EXISTS login(
        codLog int primary key,
        nivel varchar(20) not null
    );''',

    '''CREATE TABLE IF NOT EXISTS empleado (
        codEmpleado int primary key,
        nombre varchar(100) not null,
        dni varchar(20) not null,
        email varchar(100) not null,
        telefono varchar(20) not null,
        puesto varchar(100) not null,
        codLog int not null,
        foreign key (codLog) references login(codLog)
    );''',

    '''CREATE TABLE IF NOT EXISTS cliente (
        codCliente int primary key,
        nombre varchar(100) not null,
        dni varchar(20) not null,
        email varchar(100),
        descr varchar(255)
    );''']

# me conecto a la base de datos
con = s.connect("GestionHotel.db")

# creo el cursor
c = con.cursor()

# ejecuto para hacer las tablas
for query in tablas:
    c.execute(query)

# realizo los cambios
con.commit()
