-- Plantilla de la base de datos del programa

CREATE TABLE hotel (
    nombre varchar(50) not null,
    hab number(10) not null,
    pisos number(10) not null,
    capac number(10) not null
);

CREATE TABLE cochera (
    codcochera int primary key,
    piso int not null,
    estado varchar(50) not null
);

CREATE TABLE empleado (
    codempl int primary key,
    nombre varchar(100) not null,
    dni varchar(20) not null,
    email varchar(100) not null,
    telefono varchar(20) not null,
    puesto varchar(100) not null
);

CREATE TABLE cliente (
    codcliente int primary key,
    nombre varchar(100) not null,
    dni varchar(20) not null,
    email varchar(100),
    descr varchar(255)
);

CREATE TABLE habitacion (
    codhab int primary key,
    piso int not null,
    cant int not null,
    estado varchar(50) not null,
    descr varchar(255),
    costo decimal(10, 2)
);

CREATE TABLE reserva (
    codreserva int primary key,
    codhab int not null,
    codcliente int not null,
    codempleado int not null,
    codcochera int,
    cantidad int not null,
    fechaingreso date not null,
    fechaegreso date not null,
    costoadicional decimal(10, 2),
    descr varchar(255),
    foreign key (codhab) references habitacion(codhab),
    foreign key (codcliente) references cliente(codcliente),
    foreign key (codempleado) references empleado(codempl),
    foreign key (codcochera) references cochera(codcochera)
);

CREATE TABLE historial (
    codhistorial int primary key,
    codreserva int not null,
    codempleado int not null,
    descr varchar(255),
    foreign key (codreserva) references reserva(codreserva),
    foreign key (codempleado) references empleado(codempl)
);
