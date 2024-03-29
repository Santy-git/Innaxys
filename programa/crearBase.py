import sqlite3 as s

# una funcion que me crea la base de datos


def creardb():
    tablas = [
        '''CREATE TABLE IF NOT EXISTS login(
        codLog int primary key,
        password varchar(30) not null,
        nivel varchar(20) not null
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS empleado (
        dni_emp int primary key,
        nombre varchar(100) not null,
        email varchar(100) not null,
        telefono varchar(20) not null,
        puesto varchar(100) not null,
        codLog int not null,
        foreign key (codLog) references login(codLog)
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS cochera (
        codCochera int primary key,
        estado varchar(50) not null
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS habitacion (
        codHab int primary key,
        piso number(10) not null,
        camaMatr number(10) not null,
        camaInd number(10) not null,
        costo number(30) not null,
        estado varchar(50) not null
    );''',
#_____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS cliente (
        dni_cli int primary key,
        nombre varchar(100) not null,
        email varchar(100),
        descr varchar(255)
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS reserva (
        codReserva int primary key,
        codCliente int not null,
        codEmpleado int not null,
        cant_hab int not null,
        cant_cochera int not null,
        fechaReserva date not null,
        descr varchar(255),
        foreign key (codCliente) references cliente(dni_cli),
        foreign key (codEmpleado) references empleado(dni_emp)
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS historial (
        codHistorial int primary key,
        codReserva int not null,
        codEmpleado int not null,
        descr varchar(255),
        foreign key (codReserva) references reserva(codReserva),
        foreign key (codEmpleado) references empleado(dni_emp)
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS resHab(
        codReshab int primary key,
        codHab int not null,
        codReserva int not null,
        camaMatr number(10) not null,
        camaInd number(10) not null,
        costoHab decimal(10,2) not null,
        fechaIngreso date not null,
        fechaEgreso date not null,
        foreign key (codHab) references habitacion(codHab),
        foreign key (codReserva) references reserva(codReserva)
    );''',
#_____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS resCoch(
        codRescoch int primary key,
        codReserva int not null,
        codCochera int not null,
        fechaIngreso date not null,
        fechaEgreso date not null,
        foreign key (codCochera) references cochera(codCochera),
        foreign key (codReserva) references reserva(codReserva)
    );'''
    ]
#_____________________________________________________________________


    # me conecto a la base de datos
    con = s.connect("GestionHotel.db")

    # creo el cursor
    cur = con.cursor()

    # ejecuto para hacer las tablas
    for query in tablas:
        cur.execute(query)

    # realizo los cambios
    con.commit()
    try:
        sql = "INSERT INTO login (codLog, password, nivel) VALUES (0,'innaxys',5)"
        con.execute(sql)
        con.commit()
    except s.IntegrityError:
        pass
        
    con.close()

def login(usuario, contraseña):
    con = s.connect("GestionHotel.db")

    # creo el cursor
    cur = con.cursor()

    cur.execute("SELECT * FROM login")
    result=cur.fetchall()

    for i in range(len(result)):
        print(result[i][0])
        print(result[i][1])
        if str(usuario) == str(result[i][0]) and str(contraseña) == str(result[i][1]):
            return True ,result[i][2]
    print(result)
    con.close()

