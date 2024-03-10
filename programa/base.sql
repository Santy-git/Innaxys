-- Plantilla de la base de datos del programa

CREATE TABLE cochera (
    codCochera INT PRIMARY KEY,
    piso INT NOT NULL,
    estado VARCHAR(50) NOT NULL
);

CREATE TABLE empleado (
    codEmpl INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    puesto VARCHAR(100) NOT NULL
);

CREATE TABLE cliente (
    codCliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    descr VARCHAR(255)
);

CREATE TABLE habitacion (
    codHab INT PRIMARY KEY,
    piso INT NOT NULL,
    cant INT NOT NULL,
    estado VARCHAR(50) NOT NULL,
    descr VARCHAR(255),
    costo DECIMAL(10, 2)
);

CREATE TABLE reserva (
    codReserva INT PRIMARY KEY,
    codHab INT NOT NULL,
    codCliente INT NOT NULL,
    codEmpleado INT NOT NULL,
    codCochera INT,
    cantidad INT NOT NULL,
    fechaIngreso DATE NOT NULL,
    fechaEgreso DATE NOT NULL,
    costoAdicional DECIMAL(10, 2),
    descr VARCHAR(255),
    FOREIGN KEY (codHab) REFERENCES habitacion(codHab),
    FOREIGN KEY (codCliente) REFERENCES cliente(codCliente),
    FOREIGN KEY (codEmpleado) REFERENCES empleado(codEmpl),
    FOREIGN KEY (codCochera) REFERENCES cochera(codCochera)
);

CREATE TABLE historial (
    codHistorial INT PRIMARY KEY,
    codReserva INT NOT NULL,
    codEmpleado INT NOT NULL,
    descr VARCHAR(255),
    FOREIGN KEY (codReserva) REFERENCES reserva(codReserva),
    FOREIGN KEY (codEmpleado) REFERENCES empleado(codEmpl)
);