# ....................Librerias....................
import datetime
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Container, Stack
from flet_core.control_event import ControlEvent
from datetime import datetime
from functools import partial
import time
import threading
import sqlite3 as s
# ...................base de datos..............................


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
        # _____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS empleado (
        dni_emp int primary key,
        nombre varchar(100) not null,
        email varchar(100) not null,
        telefono varchar(20) not null,
        puesto varchar(100) not null,
        codLog varchar(30) not null,
        foreign key (codLog) references login(codLog) 
    );''',
        # _____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS cochera (
        codCochera INTEGER PRIMARY KEY AUTOINCREMENT,
        piso number(10) not null
    );''',
        # _____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS habitacion (
        codHab INTEGER PRIMARY KEY AUTOINCREMENT,
        piso number(10) not null,
        camaMatr number(10) not null,
        camaInd number(10) not null,
        costo number(30) not null
    );''',
        # _____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS cliente (
        dni_cli int primary key,
        nombre varchar(100) not null,
        email varchar(100),
        descr varchar(255)
    );''',
        # _____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS reserva (
        codReserva INTEGER PRIMARY KEY AUTOINCREMENT,
        codCliente int not null,
        codEmpleado int not null,
        fechaReserva date not null,
        descr varchar(255),
        foreign key (codCliente) references cliente(dni_cli) ,
        foreign key (codEmpleado) references empleado(dni_emp) 
    );''',
        # _____________________________________________________________________
        '''CREATE TABLE IF NOT EXISTS historial (
        codHistorial INTEGER PRIMARY KEY AUTOINCREMENT,
        codReserva int not null,
        codEmpleado int not null,
        descr varchar(255),
        foreign key (codReserva) references reserva(codReserva) ,
        foreign key (codEmpleado) references empleado(dni_emp) 
    );''',
        # _____________________________________________________________________
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
        # _____________________________________________________________________
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
# _____________________________________________________________________

    # me conecto a la base de datos
    con = s.connect("GestionHotel.sqlite3")

    # creo el cursor
    cur = con.cursor()

    # ejecuto para hacer las tablas
    for query in tablas:
        cur.execute(query)

    con.commit()
    con.close()
# logear


def login(usuario, contraseña):

    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM login")
    result = cur.fetchall()
    if result == []:
        result = [(usuario, contraseña, '1')]
        result2 = [(idioma[36])]
        estado = 0
    else:
        cur.execute("SELECT * FROM login WHERE codLog = '" +
                    usuario+"' and password = '"+contraseña+"'")
        result = cur.fetchall()
        cur.execute(
            "SELECT puesto,dni_emp FROM empleado where codLog = '"+usuario+"'")
        result2 = cur.fetchall()
        estado = 1
    return result, result2, estado

# ..........................menu 0.................................


def Reservar(dni_cli, dni_emp, fecha, desc):

    try:
        comprobante = int(dni_cli)
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
    except ValueError:
        return 2


def Consulta(ing, eng, num):
    lista = []
    fecha_actual = datetime.now().date()
    bandera = 0
    comprobante = ing.replace("-", "")
    comprobante2 = eng.replace("-", "")

    # Convertir las cadenas de texto a objetos .date
    try:
        ing_date = datetime.strptime(ing, "%Y-%m-%d").date()
        eng_date = datetime.strptime(eng, "%Y-%m-%d").date()
    except ValueError:
        return 2

    if not ing or not eng:
        return 2

    if len(comprobante) == 8 and len(comprobante2) == 8:

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

    if ing_date < fecha_actual or eng_date < fecha_actual:
        return 2

    if bandera == 1:
        if num == 0:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM habitacion WHERE codHab not in (SELECT codHab FROM resHab) or codHab in (SELECT codHab FROM resHab WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
        else:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM habitacion WHERE codHab in (SELECT codHab FROM resHab WHERE codReserva = "+num +
                        ") or codHab not in (SELECT codHab FROM resHab) or codHab in (SELECT codHab FROM resHab WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
    else:
        return 2


def completar(cli, emp, fecha, desc, hres, ing, eng):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",
                (cli, emp, fecha, desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '" +
                cli+"' AND codEmpleado = '"+str(emp)+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resHab (codHab,codReserva,camaMatr,camaInd,costoHab,fechaIngreso,fechaEgreso) VALUES (?,?,?,?,?,?,?)",
                    (hres[i][0], info[-1][0], hres[i][2], hres[i][3], hres[i][4], ing, eng))
        con.commit()
    con.close()


def completar_cochera_actualizar(cli, emp, fecha, desc, hres, ing, eng, num):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("DELETE FROM resCoch where codReserva = '"+str(num)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(num)+"'")
    con.commit()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",
                (cli, emp, fecha, desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '" +
                cli+"' AND codEmpleado = '"+emp+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resCoch (codReserva,codCochera,fechaIngreso,fechaEgreso) VALUES (?,?,?,?)",
                    (info[-1][0], hres[i][0], ing, eng))
        con.commit()
    con.close()


def completar_actualizar(cli, emp, fecha, desc, hres, ing, eng, num):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("DELETE FROM resHab where codReserva = '"+str(num)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(num)+"'")
    con.commit()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",
                (cli, emp, fecha, desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '" +
                cli+"' AND codEmpleado = '"+emp+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resHab (codHab,codReserva,camaMatr,camaInd,costoHab,fechaIngreso,fechaEgreso) VALUES (?,?,?,?,?,?,?)",
                    (hres[i][0], info[-1][0], hres[i][2], hres[i][3], hres[i][4], ing, eng))
        con.commit()
    con.close()
# eliminar reservas


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
    cur.execute("DELETE FROM resHab where codReserva = '"+str(numero)+"'")
    cur.execute("DELETE FROM resCoch where codReserva = '"+str(numero)+"'")
    cur.execute("DELETE FROM reserva where codReserva = '"+str(numero)+"'")
    con.commit()
    con.close()

# ..........................menu 1..............................


def ReservarCoch(dni_cli, dni_emp, fecha, desc):
    try:
        comprobante = int(dni_cli)
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
    except ValueError:
        return 2


def ConsultaCoch(ing, eng, num):
    lista = []
    fecha_actual = datetime.now().date()
    bandera = 0
    comprobante = ing.replace("-", "")
    comprobante2 = eng.replace("-", "")

    # Convertir las cadenas de texto a objetos .date
    try:
        ing_date = datetime.strptime(ing, "%Y-%m-%d").date()
        eng_date = datetime.strptime(eng, "%Y-%m-%d").date()
    except ValueError:
        return 2

    if not ing or not eng:
        return 2

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

    if ing_date < fecha_actual or eng_date < fecha_actual:
        return 2

    if bandera == 1:
        if num == 0:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM cochera WHERE codCochera not in (SELECT codCochera FROM resCoch) OR codCochera in (SELECT codCochera FROM resCoch WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
        else:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT * FROM cochera WHERE codCochera in (SELECT codCochera FROM resCoch WHERE codReserva = "+num +
                        ") or codCochera not in (SELECT codCochera FROM resCoch) or codCochera in (SELECT codCochera FROM resCoch WHERE fechaEgreso < '"+ing+"' OR fechaingreso > '"+eng+"')")
            z = cur.fetchall()
            con.close()
            return z
    else:
        return 2


def completarCoch(cli, emp, fecha, desc, hres, ing, eng):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("INSERT INTO reserva (codCliente, codEmpleado, fechaReserva, descr) VALUES (?,?,?,?)",
                (cli, emp, fecha, desc))
    con.commit()
    cur.execute("SELECT codReserva FROM reserva where codCliente = '" +
                cli+"' AND codEmpleado = '"+str(emp)+"'")
    info = cur.fetchall()
    for i in range(len(hres)):
        cur.execute("INSERT INTO resCoch (codReserva,codCochera,fechaIngreso,fechaEgreso) VALUES (?,?,?,?)",
                    (info[-1][0], hres[i][0], ing, eng))
        con.commit()
    con.close()


# ..................................................................


def Cli_add(a, b, c, d):
    try:
        comprobador = int(a)
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT dni_cli FROM cliente WHERE dni_cli = "+(a)+"")
        var = cur.fetchall()
        if var == []:
            cur.execute(
                "INSERT INTO cliente (dni_cli, nombre, email, descr) VALUES (?,?,?,?)", (a, b, c, d))
            con.commit()
            con.close()
            return True
        else:
            return False
    except ValueError:
        return False


def crear_hab(piso, camamatr, camaind, costo, cantidad):
    try:
        comprobador = int(piso)
        comprobador = int(camamatr)
        comprobador = int(camaind)
        comprobador = int(costo)
        comprobador = int(cantidad)
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        for i in range(int(cantidad)):
            cur.execute("INSERT INTO habitacion (piso,camaMatr,camaInd,costo) VALUES (?,?,?,?)",
                        (piso, camamatr, camaind, costo))
            con.commit()
        con.close()
        return True
    except ValueError:
        return False


def crear_coch(piso, cantidad):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    for i in range(int(cantidad)):
        cur.execute("INSERT INTO cochera (piso) VALUES (?)", (piso))
        con.commit()
    con.close()
    return True


# ..........................Menu 4.......................


# ..........................Menu 4.......................


# .................calendario.................
def calendario(mes, año):
    ing_consulta = str(año)+'-'+str(mes)+'-'+'01'
    eng_consulta = str(año)+'-'+str(mes)+'-'+str(Meses[mes])
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT codHab,fechaIngreso,fechaEgreso FROM resHab")
    matris2 = cur.fetchall()
    cur.execute("SELECT codHab FROM habitacion")
    total = cur.fetchall()
    con.close()
    return matris2, total


# gestor de elementos

def gest_elementos_consulta(date, cod, radio):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()

    if radio == '1':
        cur.execute("SELECT * FROM habitacion WHERE codHab not in (SELECT codHab from reshab where fechaEgreso > '" +
                    date+"' ) and codHab = '"+cod+"'")
        matris = cur.fetchall()

    else:
        cur.execute("SELECT * FROM cochera WHERE codCochera not in (SELECT codCochera from resCoch where fechaEgreso > '" +
                    date+"' ) and codCochera = '"+cod+"'")
        matris = cur.fetchall()

    con.close()

    return matris


def gest_elementos_eliminar(lista, cod_cliente, radio):
    bandera = 0
    if radio == '1':
        for i in range(len(lista)):
            if int(lista[i][0]) == int(cod_cliente):
                bandera = 1
        if bandera == 1:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute(
                "DELETE FROM habitacion WHERE codHab = "+cod_cliente+"")
            con.commit()
            con.close()
            return 1
    if radio == '0':
        for i in range(len(lista)):
            if int(lista[i][0]) == int(cod_cliente):
                bandera = 1
        if bandera == 1:
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute(
                "DELETE FROM cochera WHERE codCochera = "+cod_cliente+"")
            con.commit()
            con.close()
            return 0
    if radio != '0' and radio != '1':
        return 2


def gest_modificiar(codigo, radio):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    if radio == '1':
        cur.execute("SELECT codHab FROM habitacion WHERE codHab = '"+codigo+"'")
        matris = cur.fetchall()
    else:
        cur.execute(
            "SELECT codCochera FROM cochera WHERE codCochera = '"+codigo+"'")
        matris = cur.fetchall()
    con.close()
    return matris


def gest_modf_up(codigo, a, b, c, d):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE habitacion SET codHab = ?,piso = ?, camaMatr = ?,camaInd = ?,costo = ? WHERE codHab = ?",
                (codigo, a, b, c, d, codigo))
    con.commit()
    con.close()


def gest_modfCoch_up(cod_cliente, piso_coch):
    con = s.connect("GestionHotel.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE cochera SET codCochera = ?,piso = ? WHERE codCochera = ?",
                (cod_cliente, piso_coch, cod_cliente))
    con.commit()
    con.close()


# Añadir empleado

# actualizar empleado
def actualizar_emp_final(id, nombre_emp, email, telefono, puesto, usuario, contraseña, nivel):
    try:
        comprobador = int(id)
        if nivel == '7' or nivel == '8':
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()
            cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?", (id))
            matris2 = cur.fetchall()
            cur.execute("DELETE FROM login WHERE codLog = '"+matris2[0][0]+"'")
            cur.execute("DELETE FROM empleado WHERE dni_emp = ?", (id))

            cur.execute("INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)",
                        (usuario, contraseña, nivel))
            con.commit()
            cur.execute("INSERT INTO empleado (dni_emp,nombre,email,telefono,puesto,codLog) VALUES (?,?,?,?,?,?)",
                        (id, nombre_emp, email, telefono, puesto, usuario))
            con.commit()
            con.close()
            return matris2
        else:
            matris2 = []
            return matris2
    except ValueError:
        matris2 = []
        return matris2

# eliminar empleado


def eliminar_emp_final(id):
    try:
        comprobador = int(id)
        con = s.connect("GestionHotel.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT codLog FROM empleado WHERE dni_emp = ?", (id))
        matris2 = cur.fetchall()
        if matris2 != []:
            cur.execute("DELETE FROM login WHERE codLog = '"+matris2[0][0]+"'")
            cur.execute("DELETE FROM empleado WHERE dni_emp = ?", (id))
            con.commit()
            con.close()
            return matris2
        else:
            matris2 = []
            return matris2
    except ValueError:
        matris2 = []
        return matris2

# registrar empleado


def reg_emp(dni_emp, nombre_emp, email, telefono, puesto, usuario, contraseña, nivel):
    try:
        comprobador = int(dni_emp)
        if nivel == '7' or nivel == '8':
            i = 0
            con = s.connect("GestionHotel.sqlite3")
            cur = con.cursor()

            cur.execute("SELECT codLog FROM login")
            var = cur.fetchall()
            for y in range(len(var)):
                if var[y][0] == usuario:
                    i = 1
            if i == 0:
                cur.execute(
                    "INSERT INTO login (codLog,password,nivel) VALUES (?,?,?)", (usuario, contraseña, nivel))
                con.commit()
                cur.execute("INSERT INTO empleado (dni_emp,nombre,email,telefono,puesto,codLog) VALUES (?,?,?,?,?,?)",
                            (dni_emp, nombre_emp, email, telefono, puesto, usuario))
                con.commit()
                con.close()
                return True
            else:
                con.close()
                return False
    except ValueError:
        return False


# ....................................................
colores = [
    '#f3f6f4',
    '#e1eae1',
    '#c5d5c6',
    '#9db8a0',
    '#729577',
    '#557c5c',
    '#3d5e44',
    '#314b37',
    '#293c2e',
    '#223226',
    '#121c14'
]


# ....................diccionario idioma..............................

# ....................diccionario idioma..............................

# Funcionas que nos ayudan a modificar muchos objetos del flet

# los label
global idioma
global español
global ingles
global codigo
español = {1: "Axys", 2: "Logear", 3: "Usuario", 4: "Contrasena", 5: "Logear", 6: "Admin", 7: "Empleado", 8: "Reserva", 9: "Reserva de cochera",
           10: "Agregar Client",
           11: "Agregar Elemento",
           12: "Agregar Empleado",
           13: "Calendario",
           14: "Identificacion Cliente",
           15: "Descripcion",
           16: "Consulta",
           17: "Ingreso",
           18: "Salida",
           19: "Consulta",
           20: "Confirmar",
           21: "Nombre",
           22: "Correo",
           23: "Cargar",
           24: "Estacionamiento",
           25: "Habitacion",
           26: "Piso",
           27: "Reserva Estacionamiento ",
           28: "Cama de doble plaza",  # double bed
           29: "Cama",
           30: "Precio",
           31: "Identificacion del empleado",
           32: "Telefono",
           33: "Trabajo",
           34: "Nivel de acceso",
           35: "Usuario incorrecto",
           36: "ingrese un empleado con nivel de acceso 8",
           37: 'Inicie sesión para usar el programa',

           38: "Habitaciones",
           39: "Habitaciones libres",
           40: "Costo total",
           41: "Costo",
           42: "Fecha inválida",
           43: "Fecha de ingreso (yyyy-mm-dd)",
           44: "Fecha de salida (yyyy-mm-dd)",
           45: "Consultar",
           46: "Reservar",
           47: "Cliente no encontrado",
           48: "Reservar habitación",
           49: "Gestion de elementos",
           50: "Agregar elementos",
           51: "Gestión de reservas",
           52: "Actualizar",
           53: "Eliminar",
           54: "Datos inválidos",
           55: "Ingreso correctamente",
           56: "Borrar empleado",
           57: "Empleado no encontrado",
           58: "Actualizar empleado",
           59: "Mes (mm)",
           60: "Año (yyyy)",
           61: "Eliminar",
           62: "Editar",
           63: "Cochera",
           64: "Numero",
           65: "Seleccionar habitación o cochera",
           66: "Elemento no encontrado",
           67: "Borrar cochera",
           68: "Borrar habitación",
           69: "Actualizar cochera",
           70: "Actualizar habitación",
           71: "Cantidad",
           72: "Valor inválido",
           73: "Datos incorrectos"
           }
idioma = español
ingles = {1: "Axys", 2: "Sing in", 3: "User", 4: "Password", 5: "SIGN IN", 6: "Admin", 7: "Employees", 8: "Room booking", 9: "Park booking",
          10: "Add client",
          11: "Add element",
          12: "Add employee",
          13: "Calendar",
          14: "Client id",
          15: "Description",
          16: "Query",
          17: "Check in",
          18: "Check out",
          19: "Query",
          20: "Confirm",
          21: "Name",
          22: "Mail",
          23: "Upload",
          24: "Parking",
          25: "Room",
          26: "Floor",
          27: "Booked parking",
          28: "Queen size bed",  # double bed
          29: "Bed",
          30: "Price",
          31: "Employee id",
          32: "Phone",
          33: "Job",
          34: "Access level",
          35: "Incorrect User",
          36: "Insert an employee with level eight access",
          37: "Login for use the program",
          38: "Rooms",
          39: "Free rooms",
          40: "Total cost",
          41: "Cost",
          42: "Invalid date",
          43: "Check in (yyyy-mm-dd)",
          44: "Check out (yyyy-mm-dd)",
          45: "Query",
          46: "Reservation",
          47: "Customer not found",
          48: "Room reservation",
          49: "Element managment",
          50: "Add element",
          51: "Reservation managment",
          52: "Update",
          53: "Delete",
          54: "Invalid data",
          55: "Login succesfull",
          56: "Employee delete",
          57: "Employee not found",
          58: "Employee update",
          59: "Month (mm)",
          60: "Year (yyyy)",
          61: "Delete",
          62: "Edit",
          63: "Park",
          64: "Number",
          65: "Select room or park",
          66: "Element not found",
          67: "Park delete",
          68: "Room delete",
          69: "Park update",
          70: "Room update",
          71: "Quantity",
          72: "Invalid value",
          73: "Incorrect data"




          }


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


def create_text_field(label_text, **kwargs):
    return ft.TextField(
        label=label_text,
        label_style={
            'color': ft.colors.BLACK,
            'font_size': 16,
        },
        border_radius=20,
        width=ancho*.3,
        **kwargs
    )


niveles = {8: "Administrador", 7: "Empleado"}
creardb()
# ....................................
codigo = 0

# ....variables...


class Plantilla:
    def __init__(self, raiz, idioma, español, ingles):
        self.raiz = raiz
        self.idioma = idioma
        self.español = español
        self.ingles = ingles
        self.estado2 = 0
# ..................................................

    def ej(self):
        self.raiz.bgcolor = '#4a624e'
        self.raiz.update()

    def OFF(self, e):
        global codigo
        self.raiz.window_destroy()
        codigo = 1

    def EnEs(self, e):
        global codigo
        global idioma
        self.raiz.window_destroy()
        if self.idioma == self.español:
            idioma = self.ingles
        else:
            idioma = self.español
        codigo = 0

    def logear(self, e):
        global Nivel
        global z
        global laburo
        z = login(self.User.value, self.Password.value)

        if z[2] == 0:
            Nivel = int(z[0][0][2])
            laburo = z[1][0]
            self.Menu()
            self.Menu8()
        else:
            if z[0] != []:
                Nivel = int(z[0][0][2])
                laburo = z[1][0][0]
                self.Menu()
                self.Menu1()
            else:
                dlg = ft.AlertDialog(
                    title=ft.Text(self.idioma[35])
                )

                def open_dlg(e):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(e)

    def appbar(self):
        self.nombre = ft.Container(content=Text(
            self.idioma[1], color=colores[9],), bgcolor=colores[3], width=ancho*0.1, height=altura*0.05, border_radius=ft.border_radius.all(10))
        self.nombre.alignment = ft.alignment.center
        self.raiz.appbar = ft.AppBar(

            title=ft.Container(ft.Image(src="logo.svg", width=100),
                               width=125,
                               height=55,
                               padding=ft.padding.symmetric(horizontal=25)),
            center_title=True,
            bgcolor=colores[8],
            actions=[
                ft.IconButton(ft.icons.LANGUAGE,
                              on_click=self.EnEs, icon_size=35),
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,
                              on_click=self.OFF, icon_size=35),
            ])
        self.raiz.update()

    def login_menu(self):
        global Nivel
        global z

        self.User: TextField = TextField(
            width=ancho * .2,
            height=altura * .08,
            label=self.idioma[3],
            border='underline',
            color='white',
            prefix_icon=ft.icons.PERSON,)

        self.Password: TextField = TextField(
            width=ancho * .2,
            height=altura * .08,
            label=idioma[4],
            border='underline',
            color='white',
            prefix_icon=ft.icons.LOCK,
            password=True)

        self.Button: ElevatedButton = ElevatedButton(
            content=Text(
                self.idioma[5],
                color='white',
                weight='w500',
            ),
            width=ancho * .2,
            bgcolor='black',
            on_click=self.logear)

        self.contenedor_login = ft.Container(
            Container(
                Stack([
                    Container(
                        border_radius=ancho*.005,
                        rotate=ft.Rotate(0.98*3.1),  # Degree
                        width=ancho * .2,
                        height=altura * .5,
                        bgcolor='#22ffffff'
                    ),
                    Container(
                        Container(
                            Column([
                                ft.Image(
                                    src="Isologo.png",
                                    width=ancho * .2/1.2,
                                    height=altura * .1/1.2,
                                ),
                                Text(
                                    self.idioma[5],
                                    width=ancho * .2,
                                    size=altura * .03,
                                    text_align='center'),

                                Text(
                                    self.idioma[37],
                                    width=ancho * .2,
                                    text_align='center',
                                    size=10

                                ),
                                Container(self.User, padding=ft.padding.symmetric(horizontal=ancho * .03)
                                          ),
                                Container(self.Password, padding=ft.padding.symmetric(horizontal=ancho * .03)
                                          ),
                                Container(self.Button, padding=ft.padding.symmetric(horizontal=ancho * .03), margin=ft.margin.only(top=altura * .02)

                                          )
                            ])
                        ),
                        padding=ft.padding.only(25, 25, 25, 0),
                        width=ancho * .2,
                        height=altura * .5,
                        bgcolor='#22ffffff',
                        border_radius=ancho*0.005,
                    )
                ]),
                alignment=ft.alignment.center,
                width=ancho * 0.3,
                height=altura * 0.6,
                bgcolor='grey900'

            ),
            width=(ancho/100)*30,
            height=(altura/100)*70,
            border_radius=ft.border_radius.all(ancho*.005),
            margin=ft.margin.symmetric(
                horizontal=ancho*0.33, vertical=altura*0.08)
        )

        self.raiz.add(self.contenedor_login)

# ...................................Menus............................

# ...................................Menus............................

    def pedidos(self, var):
        hres.append(self.variable2[var])
        images.controls.pop(var)
        images.update()
        self.variable2.pop(var)
        totalesp = 0
        costo = 0

        for i in range(len(hres)):
            totalesp += hres[i][3]
            totalesp += hres[i][2]*2
            costo += hres[i][4]
        totalH = len(hres)
        self.contador.value = (
            idioma[38], totalH, idioma[39], totalesp, idioma[40], costo)
        self.contador.update()
        self.disponibles()

    def disponibles(self):
        global images

        def valor(a):
            indice = a
            infoH = ft.Row([
                ft.Container(width=50, height=50, bgcolor='#A3CD91',
                             border_radius=ft.border_radius.all(6),
                             margin=ft.margin.all(10),
                             alignment=ft.alignment.center,
                             content=ft.Text(value=self.variable2[a][0], color='#000000')),
                ft.Text(value=idioma[26]+str(self.variable2[a][1]))
            ])
            infoH2 = ft.Row([
                ft.Text(value=idioma[29] +
                        str(self.variable2[a][2])),

            ])
            infoH4 = ft.Row([
                ft.Text(value=idioma[28] +
                        str(self.variable2[a][3])),

            ])

            infoH3 = ft.Row([
                ft.Text(value=idioma[41]+str(self.variable2[a][4])),
                ft.IconButton(icon=ft.icons.ADD, icon_size=20,
                              icon_color='#000000', on_click=lambda _: self.pedidos(indice))
            ])
            contener = ft.Container(width=60, height=60,
                                    border_radius=ft.border_radius.all(3), bgcolor=colores[9],
                                    content=ft.Column(
                                        [infoH, infoH2, infoH4, infoH3]),
                                    padding=ft.padding.symmetric(horizontal=30, vertical=30))
            return contener

        images = ft.GridView(
            runs_count=5,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=20,
            run_spacing=5,
            expand=1,
        )

        for i in range(len(self.variable2)):
            images.controls.append(valor(i))
        self.Departamentos.clean()
        self.Departamentos.content = ft.Column([images])
        Container_menus.update()

    def Consulta_aux(self, Ingreso_Res, Egreso_Res, num):
        global hres
        hres = []
        self.variable2 = Consulta(Ingreso_Res, Egreso_Res, num)
        if self.variable2 == 2:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[42])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
        else:
            self.disponibles()

    def res_final(self, cli, emp, fecha, desc, hres, Ing, Eng, num):
        if num != 0:
            confirmar = ft.TextButton(text=idioma[20], icon_color="#659863", style=ft.ButtonStyle(color='black', overlay_color=colores[5]), on_click=lambda _: (completar_actualizar(
                cli, emp, fecha, desc, hres, Ing, Eng, num), self.Menu1()))
        else:
            confirmar = ft.TextButton(text=idioma[20], style=ft.ButtonStyle(color='black', overlay_color=colores[5]), icon_color="#659863", on_click=lambda _: (completar(
                cli, emp, fecha, desc, hres, Ing, Eng), self.Menu1()))
        Container_menus.clean()
        a = 0
        c = 0
        d = 0
        e = 0
        for i in range(len(hres)):
            a += 1
            c += hres[i][2]
            d += hres[i][3]
            e += hres[i][4]

        hab = ft.Text(value=f"{idioma[29]} {a}", color='black', size=17)
        matr = ft.Text(value=f"{idioma[28]} {c}", color='black', size=17)
        indiv = ft.Text(value=f"{idioma[29]} {d}", color='black', size=17)
        total = ft.Text(value=f"{idioma[40]} ${e}", color='black', size=17)

        info = ft.Column(controls=[hab, matr, indiv, total, confirmar])
        Container_menus.content = ft.Container(
            content=info, bgcolor=colores[4], width=300, height=300, alignment=ft.alignment.center, border_radius=5, padding=ft.padding.symmetric(vertical=60))
        Container_menus.alignment = ft.alignment.center
        Container_menus.clean()
        Container_menus.update()

    def Reservar_Aux(self, cli, emp, fecha, desc, num):
        Container_menus.clean()
        Verificar = Reservar(cli, emp, fecha, desc)
        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = create_text_field(idioma[17])
            Egreso_Res = create_text_field(idioma[18])
            consultar = ft.TextButton(text=idioma[45], on_click=lambda _: self.Consulta_aux(
                Ingreso_Res.value, Egreso_Res.value, num), style=ft.ButtonStyle(color='black', overlay_color=colores[5]))
            reservarboton = ft.TextButton(text=idioma[46], on_click=lambda _: self.res_final(
                cli, emp, fecha, desc, hres, Ingreso_Res.value, Egreso_Res.value, num
            ), style=ft.ButtonStyle(color='black', overlay_color=colores[5]))
            self.Departamentos = ft.Container(
                width=830, height=425, bgcolor=colores[2], margin=10)
            self.contador = ft.Text(value="")
            a = ft.Row([Ingreso_Res, Egreso_Res])
            b = ft.Row([consultar, reservarboton, self.contador])
            c = ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a, b, c], expand=True)
            Container_menus.padding = ft.padding.symmetric(
                horizontal=ancho * 0.08, vertical=altura * 0.10)
            Container_menus.update()
        if Verificar == 2:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[47])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
# ...............lo de arriba es la reserva subir..............


# Reservar habitacion


    def Menu1(self):
        titulo = ft.Text(value=idioma[48],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)

        cod_cliente = create_text_field(
            idioma[14])

        fecha_res = datetime.now().date()
        desc = create_text_field(
            idioma[15],
            multiline=True,
            max_length=200,
            max_lines=3)

        subir = ft.CupertinoButton(
            content=ft.Text(idioma[23], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.Reservar_Aux(
                cod_cliente.value, z[1][0][1], fecha_res, desc.value, 0))
        inputs = ft.Column(
            controls=[titulo, cod_cliente, desc])
        botones = ft.Row(controls=[subir])
        Container_menus.content = ft.Column(
            [inputs,
             botones],
            expand=True,
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.19, vertical=altura * 0.10)
        Container_menus.update()
# ................................habitacion.......................

    def pedidosCoch(self, var):
        hres.append(self.variable2[var])
        images.controls.pop(var)
        images.update()
        self.variable2.pop(var)
        self.disponiblesCoch()

    def disponiblesCoch(self):
        global images

        def valor(a):
            indice = a

            # lo que está adentro de cuadrado
            # --------------------------------------------
            infoH = ft.Row([
                ft.Container(width=50, height=50, bgcolor='#A3CD91',
                             border_radius=ft.border_radius.all(6),
                             margin=ft.margin.all(10),
                             alignment=ft.alignment.center,
                             content=ft.Text(value=self.variable2[a][0], color='#000000')),
                ft.Text(value=idioma[26]+str(self.variable2[a][1]))
            ])
            # ---------------------------------------------

            # el cuadrado
            contener = ft.Container(width=60, height=60, bgcolor=colores[9], content=ft.Column(
                [infoH, ft.TextButton(text="+", on_click=lambda _: self.pedidosCoch(indice))]))

            return contener

        images = ft.GridView(
            runs_count=5,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=20,
            run_spacing=5,
            expand=1,
        )

        for i in range(len(self.variable2)):
            images.controls.append(valor(i))
        self.Departamentos.clean()
        self.Departamentos.content = ft.Column([images])
        Container_menus.update()

    def ConsultaCoch_aux(self, Ingreso_Res, Egreso_Res, num):
        global hres
        hres = []
        self.variable2 = ConsultaCoch(Ingreso_Res, Egreso_Res, num)
        if self.variable2 == 2:
            dlg = ft.AlertDialog(
                title=ft.Text("incorrect date")
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
        else:
            self.disponiblesCoch()

    def resCoch_final(self, cli, emp, fecha, desc, hres, Ing, Eng, num):
        if num != 0:
            confirmar = ft.TextButton(text="Confirm", icon_color="#659863", on_click=lambda _: (completar_cochera_actualizar(
                cli, emp, fecha, desc, hres, Ing, Eng, num), self.Menu2()), style=ft.ButtonStyle(color='black', overlay_color=colores[5]))
        else:
            confirmar = ft.TextButton(text="Confirm", icon_color="#659863", on_click=lambda _: (completarCoch(
                cli, emp, fecha, desc, hres, Ing, Eng), self.Menu2()), style=ft.ButtonStyle(color='black', overlay_color=colores[5]))
        Container_menus.clean()
        a = 0

        for i in range(len(hres)):
            a += 1

        coch = ft.Text(value=f"parks: {a}", color='black', size=17)
        info = ft.Column(controls=[coch, confirmar])

        Container_menus.content = ft.Container(
            content=info, bgcolor=colores[4], width=250, height=250, alignment=ft.alignment.center, border_radius=5, padding=ft.padding.symmetric(vertical=90))
        Container_menus.alignment = ft.alignment.center
        Container_menus.clean()
        Container_menus.update()

    def ReservarCoch_Aux(self, cli, emp, fecha, desc, num):
        Container_menus.clean()
        Verificar = ReservarCoch(cli, emp, fecha, desc)

        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = create_text_field(idioma[43])
            Egreso_Res = create_text_field(idioma[44])
            consultar = ft.TextButton(text="Consult", on_click=lambda _: self.ConsultaCoch_aux(
                Ingreso_Res.value, Egreso_Res.value, num), style=ft.ButtonStyle(color='black', overlay_color=colores[5]))
            reservarboton = ft.TextButton(text="Reservation", on_click=lambda _: self.resCoch_final(
                cli, emp, fecha, desc, hres, Ingreso_Res.value, Egreso_Res.value, num
            ), style=ft.ButtonStyle(color='black', overlay_color=colores[5]))
            self.Departamentos = ft.Container(
                width=830, height=425, bgcolor=colores[2], margin=10)
            contador = ft.Text(value="")
            a = ft.Row([Ingreso_Res, Egreso_Res])
            b = ft.Row([consultar, reservarboton, contador])
            c = ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a, b, c])
            Container_menus.padding = ft.padding.symmetric(
                horizontal=ancho * 0.08, vertical=altura * 0.1)
            Container_menus.update()
        if Verificar == 2:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[47])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
# Reservar cochera

    def Menu2(self):
        titulo = ft.Text(value=idioma[9],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        cod_cliente = create_text_field("customer id")
        fecha_res = datetime.now().date()
        desc = create_text_field(
            "Descriprion", multiline=True, max_length=200, max_lines=3)
        subir = ft.CupertinoButton(
            content=ft.Text(idioma[23], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.ReservarCoch_Aux(cod_cliente.value, z[1][0][1], fecha_res, desc.value, 0))

        inputs = ft.Column(
            controls=[titulo, cod_cliente, desc])
        botones = ft.Row(controls=[subir])
        Container_menus.content = ft.Column(
            [inputs,
             botones],
            expand=True,
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.19, vertical=altura * 0.10)
        Container_menus.update()

    def act_reserva_Aux(self, cli, emp, fecha, desc, num):
        Container_menus.clean()
        Verificar = Reservar(cli, emp, fecha, desc)
        if Verificar == 1:
            Container_menus.clean()
            Ingreso_Res = create_text_field(idioma[43])
            Egreso_Res = create_text_field(idioma[44])
            consultar = ft.TextButton(text="Query", on_click=lambda _: self.Consulta_aux(
                Ingreso_Res.value, Egreso_Res.value, num))
            reservarboton = ft.TextButton(text="confirm", on_click=lambda _: self.res_final(
                cli, emp, fecha, desc, hres, Ingreso_Res.value, Egreso_Res.value, num
            ))
            self.Departamentos = ft.Container(
                width=830, height=500, bgcolor=colores[2], margin=10)
            self.contador = ft.Text(value="")
            a = ft.Row([Ingreso_Res, Egreso_Res])
            b = ft.Row([consultar, reservarboton, self.contador])
            c = ft.Row([self.Departamentos])
            Container_menus.content = ft.Column([a, b, c])
            Container_menus.padding = ft.padding.symmetric(
                horizontal=ancho * 0.2, vertical=altura * 0.10)

            Container_menus.update()
        if Verificar == 2:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[47])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)

    def res_eliminar_aux(self, dni):
        info = consulta_eliminar(dni)
        registro = ft.Column(
            width=Container_menus.width - 100,
            height=Container_menus.height - 100,
            spacing=2,
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
        )
        for i in range(len(info)):
            self.espacio = ft.Container(width=600, height=30, border_radius=ft.border_radius.all(10), bgcolor=colores[4], content=ft.Text(value=" Codigo de reserva:"+str(info[i][0])+"   Codigo del empleado: "+str(
                info[i][2])+"   reservation date: "+str(info[i][3]),))
            registro.controls.append(ft.Row(controls=[self.espacio]))
        codigo = ft.TextField(label="code of reservation to modify")
        registro.controls.append(
            ft.Row(
                controls=[codigo,
                          ft.IconButton(icon=ft.icons.DELETE,
                                        icon_size=30,
                                        width=60,
                                        height=60,
                                        on_click=lambda _: eliminar_reserva(
                                            codigo.value)
                                        )]))
        Container_menus.clean()
        Container_menus.content = registro
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.1, vertical=altura * 0.10)
        Container_menus.update()
# ...............eliminar reservas arriba....................

    def dador(self, cod, info, dni):
        tipo = consulta_tipo(cod)
        if tipo == []:
            for j in range(len(info)):
                if str(cod) == str(info[j][0]):
                    self.ReservarCoch_Aux(dni, str(
                        info[j][2]),
                        datetime.now().date(),
                        info[j][4],
                        cod
                    )
        else:
            for j in range(len(info)):
                if str(cod) == str(info[j][0]):
                    self.Reservar_Aux(dni, str(
                        info[j][2]),
                        datetime.now().date(),
                        info[j][4],
                        cod
                    )

    def res_actualizar(self, dni):
        info = consulta_eliminar(dni)
        registro = ft.Column(
            width=Container_menus.width - 100,
            height=Container_menus.height - 100,
            spacing=2,
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
        )

        for i in range(len(info)):
            self.espacio = ft.Container(width=600, height=30, border_radius=ft.border_radius.all(10), bgcolor=colores[4], content=ft.Text(value=" reservation code:"+str(info[i][0])+"   employee code: "+str(
                info[i][2])+"   reservation date: "+str(info[i][3]),))
            registro.controls.append(ft.Row(controls=[self.espacio]))
        codigo = ft.TextField(label="code of reservation to modify")
        registro.controls.append(
            ft.Row(
                controls=[codigo,
                          ft.IconButton(icon=ft.icons.SEND,
                                        icon_size=30,
                                        width=60,
                                        height=60,
                                        on_click=lambda _: self.dador(
                                            codigo.value, info, dni)
                                        )]))
        Container_menus.clean()
        Container_menus.content = registro
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.2, vertical=altura * 0.10)
        Container_menus.update()
# ................actualizar reserva.......................

# Gestor de reserva
    def Menu3(self):
        titulo = ft.Text(value=idioma[51],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        cod_cliente = create_text_field(
            idioma[14])
        eliminar = ft.CupertinoButton(
            content=ft.Text("Delete", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.res_eliminar_aux(cod_cliente.value))

        modificar = ft.CupertinoButton(
            content=ft.Text("Modify", color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.res_actualizar(cod_cliente.value))

        botones = ft.Row(controls=[eliminar, modificar])
        inputs = ft.Column(
            controls=[titulo, cod_cliente, botones])

        Container_menus.content = ft.Column(
            [inputs],
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.19, vertical=altura * 0.10)
        Container_menus.update()

# ................................cochera.......................

    def Cli_Aux(self, a, b, c, d):
        Verificar = Cli_add(a, b, c, d)
        if Verificar:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[10])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
            Container_menus.clean()
            self.Menu4()
        else:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[73])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
# Añadir cliente

    def Menu4(self):
        titulo = ft.Text(value=idioma[10],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        cod_cliente = create_text_field(idioma[14])
        nom_cli = create_text_field(idioma[21])
        email_cli = create_text_field(idioma[22])
        desc_cli = create_text_field(
            idioma[15], multiline=True, max_length=200, max_lines=3)
        subir_cli = ft.CupertinoButton(
            content=ft.Text(idioma[23], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.Cli_Aux(cod_cliente.value, nom_cli.value, email_cli.value, desc_cli.value))

        inputs = ft.Column(
            controls=[titulo, cod_cliente, nom_cli, email_cli, desc_cli])
        botones = ft.Row(controls=[subir_cli])
        Container_menus.content = ft.Column(
            [inputs,
             botones],
            expand=True,
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.19, vertical=altura * 0.10)
        Container_menus.update()
# ......................cliente...............
# Añadir elemento

    def Menu5(self):
        titulo = ft.Text(value=idioma[50],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        cocherav = ft.CupertinoButton(
            text=idioma[63], on_click=lambda _: self.cochera(), bgcolor=colores[5])
        habitacionv = ft.CupertinoButton(
            text=idioma[29], on_click=lambda _: self.habitacion(), bgcolor=colores[5])

        botones = ft.Row(controls=[cocherav, habitacionv], spacing=40)
        Container_menus.content = ft.Column([titulo, botones])
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.17, vertical=altura * 0.10)
        Container_menus.update()

    def crear_coch(self, a, b):
        validacion = crear_coch(a, b)
        if validacion:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[9])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
            Container_menus.clean()
            self.Menu5()

    def cochera(self):
        piso_coch = create_text_field(idioma[26])
        cantidad = create_text_field(idioma[71])
        cantidad.value = 1
        subir_coch = ft.CupertinoButton(
            content=ft.Text(idioma[23], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.crear_coch(piso_coch.value, cantidad.value))
        inputs = ft.Column(
            controls=[piso_coch, cantidad])
        botones = ft.Row(controls=[subir_coch])
        Container_menus.content = ft.Column(
            [inputs, botones
             ],
            expand=True
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.17, vertical=altura * 0.10)
        Container_menus.update()

    def crear_habitacion(self, a, b, c, d, e):
        validacion = crear_hab(a, b, c, d, e)
        if validacion:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[8])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
            Container_menus.clean()
            self.Menu5()
        else:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[72])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)

    def habitacion(self):
        piso = create_text_field(idioma[26])
        camamatr = create_text_field(idioma[28])
        camaind = create_text_field(idioma[29])
        costo = create_text_field(idioma[41])
        cantidad = create_text_field(idioma[71])
        cantidad.value = 1
        subir_cli = ft.CupertinoButton(
            content=ft.Text(idioma[23], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(15),
            on_click=lambda _: self.crear_habitacion(piso.value, camamatr.value, camaind.value, costo.value, cantidad.value))
        inputs = ft.Column(
            controls=[piso, camamatr, camaind, costo, cantidad])
        botones = ft.Row(controls=[subir_cli])
        Container_menus.content = ft.Column(
            [inputs, botones
             ],
            expand=True
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.17, vertical=altura * 0.10)
        Container_menus.update()
# ....................elementos........................

    def salida(self, codigo, a, b, c, d):
        gest_modf_up(codigo, a, b, c, d)
        dlg = ft.AlertDialog(
            title=ft.Text(idioma[70])
        )

        def open_dlg(self):
            self.raiz.dialog = dlg
            dlg.open = True
            self.raiz.update()
        open_dlg(self)
        Container_menus.clean()
        self.Menu6()

    def salidaCoch(self, cod_cliente, piso_coch):
        gest_modfCoch_up(cod_cliente, piso_coch)
        dlg = ft.AlertDialog(
            title=ft.Text(idioma[69])
        )

        def open_dlg(self):
            self.raiz.dialog = dlg
            dlg.open = True
            self.raiz.update()
        open_dlg(self)
        Container_menus.clean()
        self.Menu6()

    def gest_elementos_modificar(self, cod_cliente, radio):
        fecha_sys = datetime.now().date()
        fecha_sys = fecha_sys.strftime("%x")
        fecha_sys = str(fecha_sys)
        lista = gest_modificiar(cod_cliente, radio)
        if lista == []:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[66])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)
        else:
            if radio == '1':
                piso = create_text_field(idioma[26])
                camamatr = create_text_field(idioma[28])
                camaind = create_text_field(idioma[29])
                costo = create_text_field(idioma[41])
                subir_cli = ft.CupertinoButton(
                    content=ft.Text(idioma[23], color=ft.colors.BLACK),
                    bgcolor=colores[1],
                    border_radius=ft.border_radius.all(15),
                    on_click=lambda _: self.salida(cod_cliente, piso.value, camamatr.value, camaind.value, costo.value))
                Container_menus.content = ft.Column(
                    [piso,
                     camamatr,
                     camaind,
                     costo,
                     subir_cli],
                    expand=True
                )
                Container_menus.padding = ft.padding.symmetric(
                    horizontal=ancho * 0.19, vertical=altura * 0.10)
                Container_menus.update()
            elif radio == '0':
                piso_coch = create_text_field(idioma[26])
                subir_coch = ft.CupertinoButton(
                    content=ft.Text(idioma[23], color=ft.colors.BLACK),
                    bgcolor=colores[1],
                    border_radius=ft.border_radius.all(15),
                    on_click=lambda _: self.salidaCoch(cod_cliente, piso_coch.value))
                Container_menus.content = ft.Column(
                    [piso_coch, subir_coch
                     ],
                    expand=True
                )
                Container_menus.padding = ft.padding.symmetric(
                    horizontal=ancho * 0.19, vertical=altura * 0.10)
                Container_menus.update()

            elif radio == None:

                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[65]))
                Container_menus.update()

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)

    def gest_elementos_eliminar_aux(self, cod_cliente, radio):
        fecha_sys = datetime.now().date()
        fecha_sys = fecha_sys.strftime("%x")
        fecha_sys = str(fecha_sys)

        lista = gest_elementos_consulta(fecha_sys, cod_cliente, radio)

        if lista == []:
            dlg = ft.AlertDialog(
                title=ft.Text(idioma[66])
            )

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)

        if radio == '1' or radio == '0':
            vuelta = gest_elementos_eliminar(lista, cod_cliente, radio)
            if vuelta == 1:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[68])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
            if vuelta == 0:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[67])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
            if vuelta == 2:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[66])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)

        elif radio == None:

            dlg = ft.AlertDialog(
                title=ft.Text(idioma[65]))
            Container_menus.update()

            def open_dlg(self):
                self.raiz.dialog = dlg
                dlg.open = True
                self.raiz.update()
            open_dlg(self)


# Gestor de elementos

    def Menu6(self):
        titulo = ft.Text(value=idioma[49],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        cod_cliente = create_text_field(
            idioma[64])

        radio = ft.RadioGroup(
            content=ft.Row(
                [
                    ft.Radio(value=1, label=idioma[25]),
                    ft.Radio(value=0, label=idioma[63])
                ]
            )

        )

        eliminar = ft.CupertinoButton(
            content=ft.Text(idioma[61], color=ft.colors.BLACK),
            bgcolor=colores[1],
            on_click=lambda _: self.gest_elementos_eliminar_aux(cod_cliente.value, radio.value))

        modificar = ft.CupertinoButton(
            content=ft.Text(idioma[62], color=ft.colors.BLACK),
            bgcolor=colores[1],
            on_click=lambda _: self.gest_elementos_modificar(cod_cliente.value, radio.value))

        botones = ft.Row(controls=[eliminar, modificar])
        elementos = ft.Row(controls=[radio])
        inputs = ft.Column(
            controls=[titulo, cod_cliente, elementos, botones])

        Container_menus.content = ft.Column(
            [inputs],
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.19, vertical=altura * 0.10)
        Container_menus.update()
# Calendario

    def Menu7(self):
        def Calendario_menu(mes, año):

            if len(elementos.controls) > 2:
                elementos.controls.pop()
                elementos.update()

            cl = ft.Column(
                width=Container_menus.width,
                height=Container_menus.height-450,
                spacing=17,
                scroll=ft.ScrollMode.ALWAYS,
                on_scroll_interval=0,
            )

            matris = calendario(mes, año)
            # listas para armar la tabla
            verificador = []
            for i in range(len(matris[1])):

                bandera = 0
                for z in range(len(matris[0])):
                    if (i+1) == matris[0][z][0]:
                        bandera = 1
                        numero = z

                if bandera == 1:
                    ing_D = datetime.fromisoformat(matris[0][numero][1])
                    ing_D = ing_D.strftime("%d")
                    ing_M = datetime.fromisoformat(matris[0][numero][1])
                    ing_M = ing_M.strftime("%m")
                    eng_D = datetime.fromisoformat(matris[0][numero][2])
                    eng_D = eng_D.strftime("%d")
                    eng_M = datetime.fromisoformat(matris[0][numero][2])
                    eng_M = eng_M.strftime("%m")
                    concat_ing = ing_M + ing_D
                    concat_eng = eng_M + eng_D
                    verificador.append(
                        [matris[1][i][0], concat_ing, concat_eng])
                else:
                    verificador.append([matris[1][i][0], 0, 0])
            for j in range(len(matris[1])):
                dias = [ft.Text(bgcolor=colores[4],
                                value=idioma[25]+str(matris[1][j][0])),]

                for dia in range(Meses[mes]):
                    nose = int(mes)*100 + int(dia)+1

                    try:
                        if int(verificador[j][1]) <= nose and int(verificador[j][2]) >= nose:
                            dias.append(ft.Container(width=20, height=20, bgcolor=ft.colors.RED_300, content=ft.Text(
                                value=dia+1), alignment=ft.alignment.center))
                        else:
                            dias.append(ft.Container(width=20, height=20, bgcolor=ft.colors.GREEN, content=ft.Text(
                                value=dia+1), alignment=ft.alignment.center))
                    except IndexError:
                        dias.append(ft.Container(width=20, height=20, bgcolor=ft.colors.GREEN, content=ft.Text(
                            value=dia+1), alignment=ft.alignment.center))
                cl.controls.append(ft.Row(controls=dias))

            container_calendar = ft.Container(cl, border=ft.border.all(1))
            elementos.controls.append(container_calendar)
            Container_menus.update()

        titulo = ft.Text(value=idioma[13],
                         width=500, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        self.Ingreso_Res = create_text_field(idioma[59])
        self.Egreso_Res = create_text_field(idioma[60])
        consultar = ft.TextButton(
            text=idioma[45],
            style=ft.ButtonStyle(color='black', overlay_color=colores[5]),
            on_click=lambda _: Calendario_menu(
                self.Ingreso_Res.value,
                self.Egreso_Res.value),
        )

        input_fecha = ft.Row(
            [self.Ingreso_Res, self.Egreso_Res, consultar])
        elementos = ft.Column([titulo, input_fecha])
        Container_menus.content = elementos
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.015, vertical=altura * 0.10)
        Container_menus.update()

# Añadir empleado
    def Menu8(self):
        # --------------Funciones--------------
        def actualizar_emp(dni_emp, nombre_emp, email, telefono, puesto, usuario, contraseña, nivel):
            valor = actualizar_emp_final(
                dni_emp, nombre_emp, email, telefono, puesto, usuario, contraseña, nivel)
            if valor == []:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[57])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
            else:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[58])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)

        def eliminar_emp(eliminar):
            valor = eliminar_emp_final(eliminar)
            if valor == []:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[57])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
            else:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[56])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)

        def reg_emp_aux(dni_emp, nombre_emp, email, telefono, puesto, usuario, contraseña, nivel):
            validacion = reg_emp(dni_emp, nombre_emp, email,
                                 telefono, puesto, usuario, contraseña, nivel)
            if validacion:
                if z[2] == 0:
                    self.OFF(0)
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[55])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
                Container_menus.clean()
                self.Menu8()
            else:
                dlg = ft.AlertDialog(
                    title=ft.Text(idioma[54])
                )

                def open_dlg(self):
                    self.raiz.dialog = dlg
                    dlg.open = True
                    self.raiz.update()
                open_dlg(self)
                Container_menus.clean()
                self.Menu8()

        # --------------Elementos-------------
        titulo = ft.Text(value=idioma[12],
                         width=350, height=50, weight=ft.FontWeight.W_500, color='black', size=33.5)
        dni_emp = create_text_field(idioma[31])
        nombre_emp = create_text_field(idioma[21])
        email = create_text_field(idioma[22])
        telefono = create_text_field(idioma[32])
        puesto = create_text_field(idioma[33])
        usuario = create_text_field(idioma[3])
        contraseña = create_text_field(idioma[4])
        nivel = create_text_field(idioma[34])

        # botones
        registrar = ft.CupertinoButton(
            content=ft.Text(idioma[20], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(25),
            on_click=lambda _: reg_emp_aux(dni_emp.value, nombre_emp.value, email.value,
                                           telefono.value, puesto.value, usuario.value, contraseña.value, nivel.value),
            padding=ft.padding.symmetric(horizontal=120, vertical=0)
        )
        eliminar = ft.CupertinoButton(
            content=ft.Text(idioma[53], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(25),
            on_click=lambda _: eliminar_emp(dni_emp.value),
            padding=ft.padding.symmetric(horizontal=120, vertical=0)
        )
        actualizar = ft.CupertinoButton(
            content=ft.Text(idioma[52], color=ft.colors.BLACK),
            bgcolor=colores[1],
            border_radius=ft.border_radius.all(25),
            on_click=lambda _: actualizar_emp(dni_emp.value, nombre_emp.value, email.value,
                                              telefono.value, puesto.value, usuario.value, contraseña.value, nivel.value),
            padding=ft.padding.symmetric(horizontal=120, vertical=0)
        )

        # ---------------como se muestran---------------------

        inputs = ft.Column(
            controls=[titulo,
                      dni_emp,
                      nombre_emp,
                      email,
                      telefono,
                      puesto,
                      usuario,
                      contraseña,
                      nivel])
        botones = ft.Column(controls=[registrar, actualizar, eliminar])
        Container_menus.content = ft.Row(
            [inputs,
             botones]
        )
        Container_menus.padding = ft.padding.symmetric(
            horizontal=ancho * 0.13, vertical=altura * 0.05)
        Container_menus.update()


# ....................empleado.........................

# ...................calendario.......................


    def HighLight(self, e):

        if e.data == "true":
            e.control.bgcolor = colores[5]
            e.control.update()

            # Ahora lo que hago aparte de cambiar el color de fondo, el texto

            # Control del contenido por indice del IconButton y el texto
            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].icon_color = "white"
            e.control.content.update()

        else:
            e.control.bgcolor = None
            e.control.update()

            # Ahora lo que hago aparte de cambiar el color de fondo, el texto

            # Control del contenido por indice del IconButton y el texto
            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].icon_color = "white54"
            e.control.content.update()

    def Selector(self, a):
        diccionario = {idioma[8]: 1, idioma[9]: 2, idioma[51]: 3,
                       idioma[10]: 4, idioma[50]: 5, idioma[49]: 6, idioma[13]: 7, idioma[12]: 8}
        Indices_menus = {1: self.Menu1, 2: self.Menu2, 3: self.Menu3,
                         4: self.Menu4, 5: self.Menu5, 6: self.Menu6, 7: self.Menu7, 8: self.Menu8}
        Indices_menus[diccionario[a]]()

    def UserData(self, name: str):
        # Fila exclusiva para la informacion del usuario

        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        border_radius=8,
                        height=42,
                        alignment=ft.alignment.center,
                        content=Text(
                            value=Nivel,
                            size=20,
                            weight='bold',

                        ),
                    ),
                    Column(
                        spacing=1,
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight='bold',
                                max_lines=2

                            )
                        ], width=130
                    )
                ]
            )
        )

    def ContainerIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.Selector(text),
            content=Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',

                        style=ft.ButtonStyle(
                            shape={
                                "": ft.RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"}
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            )
        )


# ................Selector de menus...........


    def Menu(self):
        global formatsubmenus
        global Container_menus
        self.raiz.clean()
        self.raiz.appbar = ft.AppBar(

            title=ft.Container(ft.Image(src="logo.svg", width=100),
                               width=125,
                               height=55,
                               padding=ft.padding.symmetric(horizontal=25)),
            center_title=True,
            bgcolor=colores[8],
            actions=[
                ft.IconButton(ft.icons.EXIT_TO_APP_ROUNDED,
                              on_click=self.OFF, icon_size=35,),
            ])
        if z[2] == 0:
            formatsubmenus = []
            formatsubmenusAux = [
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("1", color=ft.colors.BLACK),
                )]
            men = [self.ContainerIcon(
                ft.icons.PERSON_ADD_ALT, idioma[12])]
        else:
            formatsubmenus = []
            formatsubmenusAux = [
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("1", color=ft.colors.BLACK),
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("2", color=ft.colors.BLACK)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("3", color=ft.colors.BLACK),
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("4", color=ft.colors.BLACK),
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("5", color=ft.colors.BLACK),
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("6", color=ft.colors.BLACK)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("7", color=ft.colors.BLACK)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(
                        ft.icons.BOOKMARK_BORDER, color=ft.colors.BLACK),
                    selected_icon_content=ft.Icon(
                        ft.icons.BOOKMARK, color=ft.colors.BLACK),
                    label_content=ft.Text("8", color=ft.colors.BLACK)
                )]

            men = [
                self.ContainerIcon(ft.icons.BED, idioma[8]),
                self.ContainerIcon(
                    ft.icons.DIRECTIONS_CAR, idioma[9]),
                self.ContainerIcon(ft.icons.MANAGE_SEARCH,
                                   idioma[51]),
                self.ContainerIcon(
                    ft.icons.PERSON_ADD, idioma[10]),
                self.ContainerIcon(ft.icons.DASHBOARD_CUSTOMIZE,
                                   idioma[50]),
                self.ContainerIcon(
                    ft.icons.DASHBOARD, idioma[49]),
                self.ContainerIcon(
                    ft.icons.CALENDAR_MONTH_OUTLINED, idioma[13]),
                self.ContainerIcon(
                    ft.icons.PERSON_ADD_ALT, idioma[10])]

        columna_lateral = Column(alignment=ft.alignment.center,
                                 horizontal_alignment="center",
                                 controls=[
                                     self.UserData(laburo),
                                     ft.Divider(height=2, color='white54'),
                                 ])
        for i in range(Nivel):

            formatsubmenus.append(formatsubmenusAux[i])
            columna_lateral.controls.append(men[i])

        Left_bar = ft.Container(
            width=200,
            height=580,
            content=columna_lateral
        )

        penas = Container(
            width=200,
            height=1000,
            bgcolor=colores[8],
            border_radius=3,
            content=Left_bar
        )
        Container_menus = ft.Container(
            width=1000,
            height=850,
            bgcolor=colores[3],
            border_radius=ft.border_radius.all(3),
            alignment=ft.alignment.center,
        )

        self.raiz.add(ft.Row(
            [
                penas,
                ft.Container(
                    Container_menus,
                    width=ancho - penas.width - 45,
                    height=850,
                )
            ],
            expand=True,
        )
        )


while True:
    if codigo == 0:
        def main(raiz: ft.Page):
            global altura
            global ancho
            ancho = 1280
            altura = 720
            raiz.window_resizable = False
            raiz.window_title_bar_hidden = True
            raiz.window_width = 1280
            raiz.window_height = 720
            raiz.window_center()
            raiz.update()
            objeto = Plantilla(raiz, idioma, español, ingles)
            objeto.ej()
            z = objeto.appbar()
            objeto.login_menu()
        ft.app(target=main)
    else:
        break
