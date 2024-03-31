import sqlite3 as s

# una funcion que me crea la base de datos


def creardb():
    tablas = [
        '''CREATE TABLE IF NOT EXISTS login(
        codLog varchar(30) primary key,
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
        codLog varchar(30) not null,
        foreign key (codLog) references login(codLog)
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS cochera (
        codCochera INTEGER PRIMARY KEY AUTOINCREMENT,
        piso number(10) not null
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS habitacion (
        codHab INTEGER PRIMARY KEY AUTOINCREMENT,
        piso number(10) not null,
        camaMatr number(10) not null,
        camaInd number(10) not null,
        costo number(30) not null
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
        codReserva INTEGER PRIMARY KEY AUTOINCREMENT,
        codCliente int not null,
        codEmpleado int not null,
        fechaReserva date not null,
        descr varchar(255),
        foreign key (codCliente) references cliente(dni_cli),
        foreign key (codEmpleado) references empleado(dni_emp)
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS historial (
        codHistorial INTEGER PRIMARY KEY AUTOINCREMENT,
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
        sql = "INSERT INTO login (codLog, password, nivel) VALUES ('0','0',5)"
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
        if str(usuario) == str(result[i][0]) and str(contraseña) == str(result[i][1]):
            return True ,result[i][2]
    print(result)
    con.close()

#..........................menu 0.................................
def Reservar(dni_cli,dni_emp,fecha,desc):
    val = 0
    con = s.connect("GestionHotel.db")
    cur = con.cursor()
    cur.execute("SELECT dni_cli from cliente")
    z = cur.fetchall()

    for i in range(len(z)):
        if int(dni_cli) == z[i][0]:
            val = 1
    if val == 1:
        cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(dni_cli,dni_emp,fecha,desc))
        con.commit()
        con.close()
        return 1
    else:
        return 2


def Consulta(ing,eng):
    val = 0
    con = s.connect("GestionHotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM habitacion WHERE codHab NOT IN (SELECT codHab FROM resHab where fechaIngreso between ("+ing+" and "+eng+") and fechaEgreso not between "+ing+" and "+eng+")")
    z = cur.fetchall()
    print(z)
    con.close()
    
#..................................................................



def Cli_add(a,b,c,d):
    con = s.connect("GestionHotel.db")
    cur = con.cursor()
    cur.execute("INSERT INTO cliente (dni_cli, nombre, email, descr) VALUES (?,?,?,?)",(a,b,c,d))
    con.commit()
    con.close()
    return True





def crear_hab(piso,camamatr,camaind,costo):
    con = s.connect("GestionHotel.db")
    cur = con.cursor()
    cur.execute("INSERT INTO habitacion (piso,camaMatr,camaInd,costo) VALUES (?,?,?,?)",(piso,camamatr,camaind,costo))
    con.commit()
    con.close()
    return True

def crear_coch(piso):
    con = s.connect("GestionHotel.db")
    cur = con.cursor()
    cur.execute("INSERT INTO cochera (piso) VALUES (?)",(piso))
    con.commit()
    con.close()
    return True




#..........................Menu 4.......................
def reg_emp(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):
    i = 0
    con = s.connect("GestionHotel.db")
    cur = con.cursor()

    cur.execute("SELECT codLog FROM login")
    var = cur.fetchall()
    for i in range(len(var)):
        if var[i][0] == usuario:
            i = 1
    print(i)
    if i == 0:
        cur.execute("INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)",(usuario,contraseña,nivel))
        con.commit()
        cur.execute("INSERT INTO empleado (dni_emp,nombre,email,telefono,puesto,codLog) VALUES (?,?,?,?,?,?)",(dni_emp,nombre_emp,email,telefono,puesto,usuario))
        con.commit()
        con.close()
        return True
    else:
        con.close()
        return False
    
    

def otra():  
    con = s.connect("GestionHotel.db")
    cur = con.cursor() 
    #cur.execute("INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)",(usuario,contraseña,nivel))
    con.commit()
   # cur.execute("INSERT INTO empleado (dni_emp,nombre,email,telefono,puesto,usuario) VALUES (?,?,?,?,?,?)",(dni_emp,nombre_emp,email,telefono,puesto,usuario))
    con.commit()
    
    return True