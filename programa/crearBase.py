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
        foreign key (codCliente) references cliente(dni_cli) ,
        foreign key (codEmpleado) references empleado(dni_emp) 
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS historial (
        codHistorial INTEGER PRIMARY KEY AUTOINCREMENT,
        codReserva int not null,
        codEmpleado int not null,
        descr varchar(255),
        foreign key (codReserva) references reserva(codReserva) ,
        foreign key (codEmpleado) references empleado(dni_emp) 
    );''',
#_____________________________________________________________________
    '''CREATE TABLE IF NOT EXISTS resHab(
        codReshab INTEGER PRIMARY KEY AUTOINCREMENT,
        codHab int not null,
        codReserva int not null,
        camaMatr number(10) not null,
        camaInd number(10) not null,
        costoHab decimal(10,2) not null,
        fechaIngreso date not null,
        fechaEgreso date not null,
        foreign key (codHab) references habitacion(codHab) ,
        foreign key (codReserva) references reserva(codReserva) 
    );''',
#_____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS resCoch(
        codRescoch INTEGER PRIMARY KEY AUTOINCREMENT,
        codReserva int not null,
        codCochera int not null,
        fechaIngreso date not null,
        fechaEgreso date not null,
        foreign key (codCochera) references cochera(codCochera) ,
        foreign key (codReserva) references reserva(codReserva) 
    );'''
    ]
#_____________________________________________________________________


    # me conecto a la base de datos
    con = s.connect("GestionHotel.sqlite3")

    # creo el cursor
    cur = con.cursor()

    # ejecuto para hacer las tablas
    for query in tablas:
        cur.execute(query)

    con.commit()




    try:
        sql = "INSERT INTO login (codLog, password, nivel) VALUES ('0','0',8)"
        con.execute(sql)
        con.commit()
    except s.IntegrityError:
        pass
        
    con.close()

def login(usuario, contraseña):
    #cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?",(id))
    print("la que te trajo",usuario,contraseña)
    con = s.connect("GestionHotel.sqlite3")
    # creo el cursor
    cur = con.cursor()
    cur.execute("SELECT * FROM login WHERE codLog = '"+usuario+"'")
    result=cur.fetchall()

    cur.execute("SELECT puesto FROM empleado where codLog = '"+usuario+"'")
    result2 = cur.fetchall()

    return result,result2
#..........................menu 0.................................
def Reservar(dni_cli,dni_emp,fecha,desc):
    val = 0
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT dni_cli from cliente")
    z = cur.fetchall()

    for i in range(len(z)):
        if int(dni_cli) == z[i][0]:
            val = 1
    if val == 1:
        return 1
    else:
        return 2


def Consulta(ing,eng,num):
    if num == 0:
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM habitacion WHERE codHab not in (SELECT codHab FROM resHab) or codHab in (SELECT codHab FROM resHab WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
        z = cur.fetchall()
        con.close()
        return z
    else:
        print(num,"numero")
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM habitacion WHERE codHab in (SELECT codHab FROM resHab WHERE codReserva = "+num+") or codHab not in (SELECT codHab FROM resHab) or codHab in (SELECT codHab FROM resHab WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
        z = cur.fetchall()
        print(z,"z")
        con.close()
        return z


def completar(cli,emp,fecha,desc,hres,ing,eng):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(cli,emp,fecha,desc))
    con.commit() 
    cur.execute("SELECT codReserva FROM reserva where codCliente = '"+cli+"' AND codEmpleado = '"+emp+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resHab (codHab,codReserva,camaMatr,camaInd,costoHab,fechaIngreso,fechaEgreso) VALUES (?,?,?,?,?,?,?)",(hres[i][0],info[-1][0],hres[i][2],hres[i][3],hres[i][4],ing,eng))
        con.commit()
    con.close()

def completar_cochera_actualizar(cli,emp,fecha,desc,hres,ing,eng,num):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    print("por aca",num)
    cur.execute("DELETE FROM resCoch where codReserva = '"+str(num)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(num)+"'")
    con.commit()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(cli,emp,fecha,desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '"+cli+"' AND codEmpleado = '"+emp+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resCoch (codReserva,codCochera,fechaIngreso,fechaEgreso) VALUES (?,?,?,?)",(info[-1][0],hres[i][0],ing,eng))
        con.commit()
    con.close()  

def completar_actualizar(cli,emp,fecha,desc,hres,ing,eng,num):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    print(num)
    cur.execute("DELETE FROM resHab where codReserva = '"+str(num)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(num)+"'")
    con.commit()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(cli,emp,fecha,desc))
    con.commit() 
    cur.execute("SELECT codReserva FROM reserva where codCliente = '"+cli+"' AND codEmpleado = '"+emp+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resHab (codHab,codReserva,camaMatr,camaInd,costoHab,fechaIngreso,fechaEgreso) VALUES (?,?,?,?,?,?,?)",(hres[i][0],info[-1][0],hres[i][2],hres[i][3],hres[i][4],ing,eng))
        con.commit()
    con.close()    
#eliminar reservas

def consulta_eliminar(dni):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * from reserva where codCliente = '"+str(dni)+"'")
    cons = cur.fetchall()
    return cons 

def consulta_tipo(cod):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codReshab from resHab where codReserva = '"+str(cod)+"'")
    cons = cur.fetchall()
    return cons 

def eliminar_reserva(numero):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    print(numero)
    cur.execute("DELETE FROM resHab where codReserva = '"+str(numero)+"'")
    cur.execute("DELETE FROM resCoch where codReserva = '"+str(numero)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(numero)+"'")
    con.commit()
    con.close()

#..........................menu 1..............................
def ReservarCoch(dni_cli,dni_emp,fecha,desc):
    val = 0
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT dni_cli from cliente")
    z = cur.fetchall()

    for i in range(len(z)):
        if int(dni_cli) == z[i][0]:
            val = 1
    if val == 1:
        return 1
    else:
        return 2

def ConsultaCoch(ing,eng,num):
    if num == 0:
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM cochera WHERE codCochera not in (SELECT codCochera FROM resCoch) OR codCochera in (SELECT codCochera FROM resCoch WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
        z = cur.fetchall()
        print(z)
        con.close()
        return z
    else:
        print(num,"numero")
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM cochera WHERE codCochera in (SELECT codCochera FROM resCoch WHERE codReserva = "+num+") or codCochera not in (SELECT codCochera FROM resCoch) or codCochera in (SELECT codCochera FROM resCoch WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
        z = cur.fetchall()
        print(z,"z")
        con.close()
        return z
    


def completarCoch(cli,emp,fecha,desc,hres,ing,eng):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(cli,emp,fecha,desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '"+cli+"' AND codEmpleado = '"+emp+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resCoch (codReserva,codCochera,fechaIngreso,fechaEgreso) VALUES (?,?,?,?)",(info[-1][0],hres[i][0],ing,eng))
        con.commit()
    con.close()



#..................................................................



def Cli_add(a,b,c,d):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO cliente (dni_cli, nombre, email, descr) VALUES (?,?,?,?)",(a,b,c,d))
    con.commit()
    con.close()
    return True


def crear_hab(piso,camamatr,camaind,costo):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO habitacion (piso,camaMatr,camaInd,costo) VALUES (?,?,?,?)",(piso,camamatr,camaind,costo))
    con.commit()
    con.close()
    return True

def crear_coch(piso):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO cochera (piso) VALUES (?)",(piso))
    con.commit()
    con.close()
    return True




#..........................Menu 4.......................
def reg_emp(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):

    i = 0
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()

    cur.execute("SELECT codLog FROM login")
    var = cur.fetchall()
    for i in range(len(var)):
        if var[i][0] == usuario:
            i = 1
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
    
#.................calendario.................
def calendario(ing,eng):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codHab,fechaIngreso,fechaEgreso FROM resHab WHERE fechaIngreso >= '"+ing+"' AND fechaEgreso <= '"+eng+"' ORDER BY codHab")
    matris2 = cur.fetchall()
    cur.execute("SELECT codHab FROM habitacion")
    total = cur.fetchall()
    con.close()
    return matris2, total



#gestor de elementos

def gest_elementos_consulta(date):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM habitacion WHERE codHab not in (SELECT codHab from reshab where fechaEgreso > '"+date+"' )")
    matris2 = cur.fetchall()
    cur.execute("SELECT * FROM cochera WHERE codCochera not in (SELECT codCochera from resCoch where fechaEgreso > '"+date+"' )")
    matris3 = cur.fetchall()
    con.close()
    return matris2,matris3

def gest_elementos_eliminar(lista,cod_cliente,hab,coch):
    bandera = 0
    if hab:
        for i in range(len(lista[0])):
            if int(lista[0][i][0])==int(cod_cliente):
                bandera = 1
        if bandera == 1:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("DELETE FROM habitacion WHERE codHab = "+cod_cliente+"")
            con.commit()
            con.close()
            return True
        else:
            return False
    else:
        for i in range(len(lista[1])):
            if int(lista[1][i][0])==int(cod_cliente):
                bandera = 1
        if bandera == 1:
            print("haol")
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("DELETE FROM cochera WHERE codCochera = "+cod_cliente+"")
            con.commit()
            con.close()
            return True
        else:
            return False
        
def gest_modificiar(codigo):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codHab FROM habitacion WHERE codHab = '"+codigo+"'")
    matris2 = cur.fetchall()
    cur.execute("SELECT codCochera FROM cochera WHERE codCochera = '"+codigo+"'")
    matris3 = cur.fetchall()
    con.close()
    return matris2 ,matris3

def gest_modf_up(codigo,a,b,c,d):
    print(codigo)
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE habitacion SET codHab = ?,piso = ?, camaMatr = ?,camaInd = ?,costo = ? WHERE codHab = ?",(codigo,a,b,c,d,codigo))
    con.commit()
    con.close()

def gest_modfCoch_up(cod_cliente,piso_coch):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE cochera SET codCochera = ?,piso = ? WHERE codCochera = ?",(cod_cliente,piso_coch,cod_cliente))
    con.commit()
    con.close()



def eliminar_emp_final(id):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?",(id))
    matris2 = cur.fetchall()
    print(matris2)
    cur.execute("DELETE FROM login WHERE codLog = ?",(matris2[0][0]))
    cur.execute("DELETE FROM empleado WHERE dni_emp = ?",(id))
    con.commit()
    con.close()
    return matris2

#       cur.execute("INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)",(usuario,contraseña,nivel))

def actualizar_emp_final(id,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?",(id))
    matris2 = cur.fetchall()
    cur.execute("DELETE FROM login WHERE codLog = ?",(matris2[0][0]))
    cur.execute("DELETE FROM empleado WHERE dni_emp = ?",(id))

    cur.execute("INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)",(usuario,contraseña,nivel))
    con.commit()
    cur.execute("INSERT INTO empleado (dni_emp,nombre,email,telefono,puesto,codLog) VALUES (?,?,?,?,?,?)",(id,nombre_emp,email,telefono,puesto,usuario))
    con.commit()
    con.close()
    return matris2