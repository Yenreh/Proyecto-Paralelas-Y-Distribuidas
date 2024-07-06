# Proyecto-Paralelas-Y-Distribuidas



### Integrantes
- **Herney Eduardo Quintero Trochez** 1528556

### Descripción
Implementación y evaluación de un sistema de orquestación de contenedores para alta disponibilidad en procesamiento distribuido


### Requerimientos
- Python 3.12
- Locust
##### Para la instalación de locust se debe ir al directorio src/tests y ejecutar el siguiente comando
```bash
sh install.sh
```
### Configuración
#### Frontend
- Hacer una copia de config.template.json en el directorio config y renombrarla a config.json
  - Agregar el endpoint de la api en el archivo config.json, este es el nombre del servicio en docker y el puerto que usa
  - Agregar el endpoint externo de la api en el archivo config.json, este la dirección en la que se expone el servicio y el puerto que usa
  - Agregar el app secret en el archivo config.json, este es la clave secreta
 
```json
{
  "api_endpoint": "<api_endpoint>",
  "api_external_endpoint": "<api_external_endpoint>",
  "app_secret": "<app_secret>"
}
```

#### Backend
- Hacer una copia de config.template.json en el directorio config y renombrarla a config.json
    - Agregar le hostname, que es el nombre del servicio en docker
    - Agregar el username, que es el usuario de la base de datos
    - Agregar el password, que es la contraseña de la base de datos
    - Agregar el database, que es el nombre de la base de datos
    - Agregar el port, que es el puerto de la base de datos, en este caso 3306 para mariadb/mysql
    - Agregar el server, que es el servidor de la base de datos, en este caso mysql
```json
{
  "db": {
    "hostname": "<db_host>",
    "username": "<db_user>",
    "password": "<db_password>",
    "database": "<db_name>",
    "port": "<db_port>",
    "server": "<db_server>"
  }
}
```
Los archivos de Logs se encuentran en el directorio logs/logs.log y se mapean a la carpeta /logs en el contenedor, por lo que estos quedan persistentes en el nodo

### Despliegue
Para el despliegue de la aplicación se deben seguir los siguientes pasos
### 1. Iniciar Docker Swarm en el nodo
Para esto se debe cambiar en el script init.sh el valor de la variable IP por la dirección ip del nodo. Luego se debe ejecutar dicho script
```bash
sh init.sh
```
### 2. Construir las imágenes
Para construir las imágenes se debe ejecutar el siguiente comando
```bash
sh build_docker_images.sh
```
### 3. Desplegar la aplicación
Para desplegar la aplicación se debe ejecutar el siguiente comando
```bash
sh run.sh
```
### Tests
Para ejecutar los tests de carga se debe ir al directorio src/tests y ejecutar el siguiente comando
```bash
sh run_tests.sh
```
Los resultados de los tests se pueden ver en el directorio src/tests/results como archivos csv

### Terminar la aplicación
Para terminar la aplicación se debe ejecutar el siguiente comando
```bash
sh erase.sh
```
Y para el borrado de las imágenes se debe ejecutar el siguiente comando
```bash
sh erase_images.sh
```

### Uso
Por defecto la aplicación se despliega en el puerto 5000 y para acceder a esta se puede acceder con la direccion del local host
http://127.0.0.1:5000/

Sí se desean cambiar los puertos se deben modificar los archivos run.py y config.json respectivamente en los directorios frontend y backend, asi como también los archivos yaml en el directorio /swarm