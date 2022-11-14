#Crear sql
#Crear maquina virtual
#gcloud sql connect soa3database --user=root
clave: root
#show databases;
#use soa-db;
# 
    create table gastos(
    gastos_id INT NOT NULL AUTO_INCREMENT,
    departamento VARCHAR(255),
    descripcion VARCHAR(255),
    fecha DATE,
    monto INT,
    nombre VARCHAR(255),
    PRIMARY KEY(gastos_id)
    );

# poblar:
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Tesoreria','calculadora2','2022-4-10',20000,'Juan');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Tesoreria','calculadora','2022-10-10',10000,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Tesoreria','telefonos','2022-4-10',50000,'Pedro');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','partes','2022-5-10',312213,'Alonso');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','lapiceros','2022-4-10',5032,'Adrian');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','lapiceros2','2022-5-8',12500,'Daniel');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','impresora','2022-4-11',122500,'Daniel');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','cable','2022-4-11',2000,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','software','2022-4-11',1000000,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','software2','2022-4-5',565000,'Adrian');


INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ventas','tijeras','2022-1-1',3214,'Daniel');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','papel2','2022-1-4',43243,'Daniel');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Soporte','computadoras','2022-1-11',2400,'Ana');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','telefono','2022-2-1',12000,'David');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Soporte','software3','2022-2-15',55000,'Adrian');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Tesoreria','laptop','2022-2-13',2500,'Jose');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','materiales','2022-3-6',24000,'Tatiana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Marketing','software4','2022-3-13',1300000,'Jesus');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','compra4','2022-3-16',525000,'Elena');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','tinta','2022-4-21',7500,'Valeria');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','sobres','2022-4-15',42500,'Carlos');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Marketing','carton','2022-4-17',52000,'Juan');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Compras','','2022-5-12',10000,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','libros','2022-5-15',85000,'Adrian');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ventas','freelancer','2022-5-18',5500,'Daniel');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','lapices','2022-6-8',43200,'Maria');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','pintura','2022-6-11',56000,'Claudia');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Publicidad','carteles','2022-6-1',150000,'Paulo');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','cotizacion1','2022-7-15',4500,'Laura');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Publicidad','audifonos','2022-7-26',55600,'Liza');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','cable2','2022-7-21',24200,'Ana');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Administracion','software5','2022-8-14',13000,'Valeria');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','teclado','2022-8-14',5700,'Jimena');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','mouse','2022-8-5',5800,'Angela');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','microfono','2022-9-8',23500,'Daniel');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','camara','2022-9-11',14500,'Paul');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','cotizacion2','2022-9-11',42000,'Liza');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','pedido2','2022-10-11',103000,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Administracion','pedido3','2022-10-20',515000,'Adrian');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','camara2','2022-10-24',142500,'Daniel');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','hojas5','2022-11-11',122500,'Daniel');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Ingenieria','camisas','2022-11-11',2000,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Administracion','papeles4','2022-11-14',1000000,'Ana');

INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('IT','lapices5','2022-12-3',565000,'Adrian');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('Compras','camara6','2022-12-1',12500,'Ana');
INSERT INTO gastos(departamento,descripcion,fecha,monto,nombre) VALUES('RH','ventilador','2022-12-14',122500,'Ana');



# query by mes ordenado:
SELECT departamento,descripcion,fecha,monto,nombre FROM gastos WHERE MONTH(fecha) = 4 AND YEAR(fecha) = 2022 ORDER by fecha;
# query gasto total:
SELECT SUM(monto) FROM gastos WHERE MONTH(fecha) = 4 AND YEAR(fecha) = 2022;
# query top 3 by month,year:
SELECT departamento, SUM(monto) FROM gastos WHERE MONTH(fecha) =
4 AND YEAR(fecha) = 2022 GROUP by departamento ORDER by SUM(monto) DESC LIMIT 3;

CLOUD SDK
gcloud config set project soa3-368600
cd SOA3_DB
gcloud init
gcloud app deploy
{
   "departamento": "Ventas",
   "descripcion": "hojas",
   "fecha": "2022-04-20",
   "monto": 4000,
   "nombre": "Elena" 
}



