import sqlite3 as s

# una funcion que me crea la base de datos

def creardb():
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
    );''',

        '''CREATE TABLE IF NOT EXISTS habitacion (
        codHab int primary key,
        piso number(10) not null,
        camaMatr number(10) not null,
        camaInd number(10) not null
    );''',
        '''CREATE TABLE IF NOT EXISTS historial (
        codHistorial int primary key,
        codReserva int not null,
        codEmpleado int not null,
        descr varchar(255),
        foreign key (codReserva) references reserva(codReserva),
        foreign key (codEmpleado) references empleado(codEmpleado)
    );''',

        '''CREATE TABLE IF NOT EXISTS resHab(
        codReshab int primary key,
        codHab int not null,
        codReserva int not null,
        camaMatr number(10) not null,
        camaInd number(10) not null,
        costoHab decimal(10,2) not null,
        fechaIngreso date not null,
        fechaEgreso date not null

        foreign key (codHab) references habitacion(codHab),
        foreign key (codReserva) references reserva(codReserva)
    );''',

        '''CREATE TABLE IF NOT EXISTS resCoch(
        codRescoch int primary key,
        codReserva int not null,
        codCochera int not null,
        foreign key (codCochera) references cochera(codCochera),
        foreign key (codReserva) references reserva(codReserva)
    );''',

        '''CREATE TABLE IF NOT EXISTS reserva (
        codReserva int primary key,
        codReshab int not null,
        codCliente int not null,
        codEmpleado int not null,
        codRescoch int,
        cantidad int not null,
        fechaReserva date not null,
        descr varchar(255),
        foreign key (codReshab) references habitacion(codReshab),
        foreign key (codCliente) references cliente(codCliente),
        foreign key (codEmpleado) references empleado(codEmpleado),
        foreign key (codRescoch) references cochera(codRescoch)
    );'''
    ]

    # me conecto a la base de datos
    con = s.connect("GestionHotel.db")

    # creo el cursor
    c = con.cursor()

    # ejecuto para hacer las tablas
    for query in tablas:
        c.execute(query)

    # realizo los cambios
    con.commit()
