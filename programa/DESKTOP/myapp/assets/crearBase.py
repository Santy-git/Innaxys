import sqlite3 as s
# una funcion que me crea la base de datos

Meses = {'01': 31,
         '02': 29,
         '03': 31,
         '04': 30,
         '05': 31,
         '06': 30,
         '07': 31,
         '08': 31,
         '09': 30,
         '10': 31,
         '11': 30,
         '12': 31}

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
    con = s.connect("myapp/assets/GestionHotel.sqlite3")

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
#logear

def login(usuario, contraseña):

    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM login WHERE codLog = '"+usuario+"' and password = '"+contraseña+"'")
    result=cur.fetchall()
    cur.execute("SELECT puesto,dni_emp FROM empleado where codLog = '"+usuario+"'")
    result2 = cur.fetchall()

    return result,result2
#..........................menu 0.................................
def Reservar(dni_cli,dni_emp,fecha,desc):
    
    try:
        comprobante = int(dni_cli)
        val = 0
        con = s.connect("myapp/assets/GestionHotel.sqlite3")
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
    except ValueError:
        return 2



def Consulta(ing,eng,num):   
    lista = []
    bandera = 0
    comprobante = ing.replace("-","")
    comprobante2 = eng.replace("-","")
    if len(comprobante) == 8:
        if len(comprobante2) == 8:
            
            if int(comprobante) < int(comprobante2):
                lista.append(eng[0:4])
                lista.append(eng[5:7])
                lista.append(eng[8:10])
                lista.append(ing[0:4])
                lista.append(ing[5:7])
                lista.append(ing[8:10])
                if Meses[lista[1]] >= int(lista[2]):
                    if Meses[lista[4]] >= int(lista[5]):
                        bandera = 1
    if bandera == 1:
        if num == 0:
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM habitacion WHERE codHab not in (SELECT codHab FROM resHab) or codHab in (SELECT codHab FROM resHab WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
        else:
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM habitacion WHERE codHab in (SELECT codHab FROM resHab WHERE codReserva = "+num+") or codHab not in (SELECT codHab FROM resHab) or codHab in (SELECT codHab FROM resHab WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
    else:
        return 2


def completar(cli,emp,fecha,desc,hres,ing,eng):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(cli,emp,fecha,desc))
    con.commit() 
    cur.execute("SELECT codReserva FROM reserva where codCliente = '"+cli+"' AND codEmpleado = '"+str(emp)+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resHab (codHab,codReserva,camaMatr,camaInd,costoHab,fechaIngreso,fechaEgreso) VALUES (?,?,?,?,?,?,?)",(hres[i][0],info[-1][0],hres[i][2],hres[i][3],hres[i][4],ing,eng))
        con.commit()
    con.close()

def completar_cochera_actualizar(cli,emp,fecha,desc,hres,ing,eng,num):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
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
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
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
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * from reserva where codCliente = '"+str(dni)+"'")
    cons = cur.fetchall()
    return cons 

def consulta_tipo(cod):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codReshab from resHab where codReserva = '"+str(cod)+"'")
    cons = cur.fetchall()
    return cons 

def eliminar_reserva(numero):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("DELETE FROM resHab where codReserva = '"+str(numero)+"'")
    cur.execute("DELETE FROM resCoch where codReserva = '"+str(numero)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(numero)+"'")
    con.commit()
    con.close()

#..........................menu 1..............................
def ReservarCoch(dni_cli,dni_emp,fecha,desc):
    try:
        comprobante = int(dni_cli)
        val = 0
        con = s.connect("myapp/assets/GestionHotel.sqlite3")
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
    except ValueError:
        return 2

def ConsultaCoch(ing,eng,num):
    lista = []
    bandera = 0
    comprobante = ing.replace("-","")
    comprobante2 = eng.replace("-","")
    if len(comprobante) == 8:
        if len(comprobante2) == 8:
            
            if int(comprobante) < int(comprobante2):
                lista.append(eng[0:4])
                lista.append(eng[5:7])
                lista.append(eng[8:10])
                lista.append(ing[0:4])
                lista.append(ing[5:7])
                lista.append(ing[8:10])
                if Meses[lista[1]] >= int(lista[2]):
                    if Meses[lista[4]] >= int(lista[5]):
                        bandera = 1
    if bandera == 1:
        if num == 0:
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM cochera WHERE codCochera not in (SELECT codCochera FROM resCoch) OR codCochera in (SELECT codCochera FROM resCoch WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
        else:
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM cochera WHERE codCochera in (SELECT codCochera FROM resCoch WHERE codReserva = "+num+") or codCochera not in (SELECT codCochera FROM resCoch) or codCochera in (SELECT codCochera FROM resCoch WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
    else:
        return 2        


def completarCoch(cli,emp,fecha,desc,hres,ing,eng):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",(cli,emp,fecha,desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '"+cli+"' AND codEmpleado = '"+str(emp)+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resCoch (codReserva,codCochera,fechaIngreso,fechaEgreso) VALUES (?,?,?,?)",(info[-1][0],hres[i][0],ing,eng))
        con.commit()
    con.close()



#..................................................................



def Cli_add(a,b,c,d):
    try:
        comprobador = int(a)
        con = s.connect("myapp/assets/GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT dni_cli FROM cliente WHERE dni_cli = "+(a)+"")
        var = cur.fetchall()
        if var == []:
            cur.execute("INSERT INTO cliente (dni_cli, nombre, email, descr) VALUES (?,?,?,?)",(a,b,c,d))
            con.commit()
            con.close()
            return True
        else:
            return False
    except ValueError:
        return False


def crear_hab(piso,camamatr,camaind,costo,cantidad):
    try:
        comprobador = int(piso)
        comprobador = int(camamatr)
        comprobador = int(camaind)
        comprobador = int(costo)
        comprobador = int(cantidad)
        con = s.connect("myapp/assets/GestionHotel.sqlite3")
        cur = con.cursor()
        for i in range(int(cantidad)):
            cur.execute("INSERT INTO habitacion (piso,camaMatr,camaInd,costo) VALUES (?,?,?,?)",(piso,camamatr,camaind,costo))
            con.commit()
        con.close()
        return True
    except ValueError:
        return False
    

def crear_coch(piso,cantidad):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    for i in range(int(cantidad)):
        cur.execute("INSERT INTO cochera (piso) VALUES (?)",(piso))
        con.commit()
    con.close()
    return True




#..........................Menu 4.......................

    
#.................calendario.................
def calendario(ing,eng):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codHab,fechaIngreso,fechaEgreso FROM resHab WHERE fechaIngreso >= '"+ing+"' AND fechaEgreso <= '"+eng+"' ORDER BY codHab")
    matris2 = cur.fetchall()
    cur.execute("SELECT codHab FROM habitacion")
    total = cur.fetchall()
    con.close()
    return matris2, total



#gestor de elementos

def gest_elementos_consulta(date,cod,radio):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor() 

    if radio == '1':
        cur.execute("SELECT * FROM habitacion WHERE codHab not in (SELECT codHab from reshab where fechaEgreso > '"+date+"' ) and codHab = '"+cod+"'")
        matris = cur.fetchall()

    else:
        cur.execute("SELECT * FROM cochera WHERE codCochera not in (SELECT codCochera from resCoch where fechaEgreso > '"+date+"' ) and codCochera = '"+cod+"'")
        matris = cur.fetchall()

    con.close()

    return matris

def gest_elementos_eliminar(lista,cod_cliente,radio):
    bandera = 0
    if radio == '1':
        for i in range(len(lista)):
            if int(lista[i][0])==int(cod_cliente):
                bandera = 1
        if bandera == 1:
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("DELETE FROM habitacion WHERE codHab = "+cod_cliente+"")
            con.commit()
            con.close()
            return True
    else:
        for i in range(len(lista)):
            if int(lista[i][0])==int(cod_cliente):
                bandera = 1
        if bandera == 1:
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("DELETE FROM cochera WHERE codCochera = "+cod_cliente+"")
            con.commit()
            con.close()
            return False
        
def gest_modificiar(codigo,radio):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    if radio == '1':
        cur.execute("SELECT codHab FROM habitacion WHERE codHab = '"+codigo+"'")
        matris = cur.fetchall()
    else:
        cur.execute("SELECT codCochera FROM cochera WHERE codCochera = '"+codigo+"'")
        matris = cur.fetchall()
    con.close()
    return matris

def gest_modf_up(codigo,a,b,c,d):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE habitacion SET codHab = ?,piso = ?, camaMatr = ?,camaInd = ?,costo = ? WHERE codHab = ?",(codigo,a,b,c,d,codigo))
    con.commit()
    con.close()
   

def gest_modfCoch_up(cod_cliente,piso_coch):
    con = s.connect("myapp/assets/GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE cochera SET codCochera = ?,piso = ? WHERE codCochera = ?",(cod_cliente,piso_coch,cod_cliente))
    con.commit()
    con.close()
    


# Añadir empleado

#actualizar empleado
def actualizar_emp_final(id,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):
    try:
        comprobador = int(id)
        if nivel == '7' or nivel == '8':
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?",(id))
            matris2 = cur.fetchall()
            cur.execute("DELETE FROM login WHERE codLog = '"+matris2[0][0]+"'")
            cur.execute("DELETE FROM empleado WHERE dni_emp = ?",(id))

            cur.execute("INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)",(usuario,contraseña,nivel))
            con.commit()
            cur.execute("INSERT INTO empleado (dni_emp,nombre,email,telefono,puesto,codLog) VALUES (?,?,?,?,?,?)",(id,nombre_emp,email,telefono,puesto,usuario))
            con.commit()
            con.close()
            return matris2
        else:
            matris2 = []
            return matris2
    except ValueError:
        matris2 = []
        return matris2

#eliminar empleado
def eliminar_emp_final(id):
    try:
        comprobador = int(id)
        con = s.connect("myapp/assets/GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?",(id))
        matris2 = cur.fetchall()
        if matris2 != []:
            cur.execute("DELETE FROM login WHERE codLog = '"+matris2[0][0]+"'")
            cur.execute("DELETE FROM empleado WHERE dni_emp = ?",(id))
            con.commit()
            con.close()
            return matris2
        else:
            matris2 = []
            return matris2
    except ValueError:
        matris2 = []
        return matris2

#registrar empleado
def reg_emp(dni_emp,nombre_emp,email,telefono,puesto,usuario,contraseña,nivel):
    try:
        comprobador = int(dni_emp)
        if nivel == '7' or nivel == '8':
            i = 0
            con = s.connect("myapp/assets/GestionHotel.sqlite3")
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
    except ValueError:
        return False

    