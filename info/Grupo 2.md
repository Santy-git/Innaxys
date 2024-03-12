## Integrantes
+ Garayzabal Joaquín
+ Sanchez Camilo
+ García Santiago
+ González Martina
+ Tomás Santiago
# **Innaxys**

## Necesario
+ **Un programa**, un software que gestione reservas de un hotel
+ **Una página**, se debe convencer a nuestro cliente de comprar nuestro software. Debe tener la opción de comprarlo.
+ **Un flyer**, lo mismo que la página pero debe ser más un folleto
+ **Un manual**, un tutorial de cómo se usa el software.
+ **Traducción al ingles**

## Consideraciones
+ El **programa** solo es de gestión hotelera, no vendemos nada.
+ Tener cuidado con el manejo de los **tiempos** a la hora de hacer reservas
+ Ver lo de historial de empleados, no se si quieren hacerlo
+ ¿Qué diseño vamos a usar, algo mas moderno, sencillo, práctico...?

## Base de Datos
Yo pense algo así
#### Reservas
Tabla con los datos de todas las reservas futuras y en curso
+ *codReserva* codigo de la reserva
+ *codresHab* clave foránea de la tabla intermedia
+ *codCliente* clave foránea del cliente que hizo la reserva
+ *codEmpleado* clave foránea del empleado que administró la reserva
+ *codCochera* (si pide) clave foránea con el número
+ *cantidad* la cantidad de personas que vienen
+ *fechaIngreso* fecha en la que ingresará el cliente
+ *fechaEgreso* fecha en la que se retirará el cliente
+ *fechaReserva* fecha en el que se realizó la reserva
+ *descripción* (si tiene) se puede usar si se agrega un extra 

#### Historial (de reservas)
Tabla con los datos de todas las reservas terminadas o canceladas
+ *codHistorial* código de cada registro (autoincrement)
+ *codReserva* clave foránea de la reserva en cuestión
+ *codEmpleado* el empleado encargado de la reserva
+ *descripción* (si tiene) puede decir por ejemplo "Cancelacion de reserva" o "Tiempo cumplido", etc

#### resHab
Tabla intermedia entre reserva y habitación
+ *codReshab* 
+ *codHab* clave foránea de la habitación
+ *codReserva* clave foránea de la reserva
+ *camaMatr* cuantas matrimoniales quiere en la reserva de la habitacion 
+ *camaInd* cuantas individuales quiere en la reserva de la habitación
+ *costoHab* cuánto sale la habitación con las modificaciones (lo decide el empleado)
#### Habitacion
Tabla con los datos de cada habitacion del hotel
+ *codHab* piso + número de habitacion
+ *piso* piso en donde se encuentra 
+ *capacidad* cantidad de personas que entran (2 personas)
+ *camaMatr* cuantas matrimoniales tiene la habitacion
+ *camaInd* cuantas matrimoniales tiene la habitacion

#### resCochera
+ *codRescoch* clave de la intermedia
+ *codReserva* clave foránea de la reserva
+ *codCochera* clave foránea de la cochera
#### Cochera
Tabla con los datos de cada cochera del hotel
+ *codCochera* codigo de la cochera
+ *estado* ocupada / desocupada

#### Cliente
Tabla con los datos necesarios del cliente
+ *codCliente* codigo del cliente
+ *nombre* nombre completo
+ *dni* 
+ *email* 
+ *descripcion* (si tiene) por si se necesita guardar alguna peculiaridad (diabetes, celiaquismo, mal comportamiento o algo por el estílo)

#### Empleado
Tabla con los datos necesarios del empleado
+ *codEmpl* codigo del empleado
+ *nombre* nombre completo
+ *dni* 
+ *email* 
+ *telefono* 
+ *pusto* el puesto donde está trabajando (recepcionista, conserje, gerente, etc)
+ *codLog* clave foránea para el login

#### Login
Tabla donde guardo los niveles de acceso y sus nombres
+ *codLog* clave principal del nivel de acceso
+ *nivel* nombre del nivel?
#### Hotel
Tabla con los datos del hotel
+ *nombre* nombre del hotel
+ *habitaciones* cantidad de habitaciones
+ *pisos* cuantos pisos tiene (pisos / alas / regiones / sectores)
+ *capacidad* la capácidad plena del hotel

