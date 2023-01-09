# TuHabi
# Proyecto Primera parte
# Filtrar consultas de propiedades

El proyecto consta de dos servicios funcionales. 
1.- Servicio sin filtrar
http://localhost:8088/properties/ ; en el cual se obtiene todos los datos sin filtrar

2.- Servicio para filtrado
http://localhost:8080/properties/filter?year=3000&city=bogota&status=en_venta; obtiene información filtrada con base a 3 atributos opcionales :
-   year    => Año de 1000 a 2999
-   city
-   status  => ['pre_venta', 'en_venta', 'vendido']

# Pasos para su realización
La primera tarea realizada fue verificar la conexión a la base de datos, por simplicidad se usó el software:
-   MySQL Workbench 8.0

Ya que el proyecto pide exlusivamente no usar frameworks, se procede a la investigación y pruebas de la librería:
- http de Python

Cuando se logra crear los endpoint se hace prueba de conexión de MySQL desde Python. 
A partir de éste punto, el trabajo se centra en el filtrado de las consultas. 
# Dependencias


Las librerías usadas para éste proyecto son las siguientes en Python 3.10.9:
- jsonschema==4.17.3
- mysql-connector-python==8.0.31

Se recomienda crear un entorno virtual y proceder a la instalación de dependencias:
    ```pip install -r requirements.txt```

Ejecución de proyecto con el siguiente comando:
    ```python main.py```

Una vez que el proyecto está corriendo, confirmar el dominio y puerto desde un mensaje como el siguiente ejemplo
- Server started http://localhost:8080

Importar la colección de postman que lleva por nombre:
- TuHabi.postman_collection

donde se encontrarán dos ejemplos previamente probados.

# Pruebas unitarias
Verificar que el servicio esté corriendo de forma local 
Ejecutar el comando: 
 ```python unitest_main.py```

# Proyecto: Segunda parte 
# - En desarrollo

