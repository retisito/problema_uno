# problema_uno

El sistema usa una base de datos SQLite y
esta compuesto por dos apps; "archives" y "api".

El app "archives" se compone de los modelos "file" y "data".
El modelo "file" almacena el nombre, estatus y fecha del archivo csv.
El modelo "data" almacena las entradas disponibles dentro del archivo csv. 
 
Los modelos están relacionados por una relación de muchos a muchos.
Un file puede tener 1..n datos. Un dato puede pertenecer a más de un file.

El app "api" contiene la lógica de los endpoints:
1. curl -i -X POST -F "name=@<archivo csv>" -F "date=<YY-MM-DD>" localhost:8000/api/upload
2. curl -i -X GET localhost:8000/api/files
3. curl -i -X GET localhost:8000/api/data
4. curl -i -X GET localhost:8000/api/csv
5. curl -i -X GET localhost:8000/api/csv/<int:pk>

Un "file" puede tener varios estados.
1. sin procesar: se hace upload del archivo csv y se crea 
                 la entrada correspondiente en "file".

2. en proceso: el job del sistema "data_load" se ejecuta, 
               abre el csv correspondiente de la entrada 
               en "file" y crea las entradas en "data".

3. procesado: el job del sistema "create_csv" se ejecuta,
              lee las entradas "data" asociadas al "file"
              correspondiente y crea un nuevo csv corregido.

4. error: si sucede algo durante el job "data_load" se asigna
          este estado al "file" correspondiente.

Para evitar repeticiones en las entradas de "data" el job "data_load" verifica 
antes de crear una entrada. Se asume que el atributo objectid es único.


Los scripts de los jobs se encuentran en la carpeta "scripts".
Se pueden ejecutar manualmente:
    $ python3 manage.py runscript db_empty
    $ python3 manage.py runscript data_load
    $ python3 manage.py runscript data_load


La tarea de los jobs es procesar los files en background. Así evitar 
el bloqueo del sistema al momento de cargar los archivos. los archivos
no se procesan al momento de la carga.


Los jobs del sistema se encuentran dentro del app "archives",
el la carpeta jobs. Se pueden ejecutar manualmente:
    $ python3 manage.py runjobs hourly
    $ python3 manage.py runjobs minutely
    $ python3 manage.py runjobs -l

Para ejecutarlos con el crontab del sistema leer la siguiente documentación:
https://django-extensions.readthedocs.io/en/latest/jobs_scheduling.html


Los archivos csv cargados se almacenan en la carpeta "public/upload".
Los archivos csv generados se almacenan en la carpeta "public/processed".  


Los TDD de los endpoints se encuentran dentro del app "api".
Se pueden ejecutar manualmente:
    $ python3 manage.py test

Notas finales: el programa hace lo que pide el enunciado del problema. 
Hay validaciones que no fuerón consideradas, así que hay partes que 
puedan fallar si se sale del contexto planteado por el enunciado
del problema. 

by A.C.