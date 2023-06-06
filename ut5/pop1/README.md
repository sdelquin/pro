# UT5-POP1: Módulos + Librerías

### PRUEBA OBJETIVA PRÁCTICA

![Python sticker](../../python-sticker.png)

Esta prueba gira en torno al trabajo con **correos electrónicos** simulando su envío y recepción a través de una pequeña base de datos.

## Creación de la base de datos

→ [create_db.py](./create_db.py)

- Ejecuta este fichero antes que nada para crear la base de datos `mail.db`.
- Aprovecha para entender las tablas existentes y su contenido.

## Plantilla

→ [mail.py](./templates/mail.py)

## Tests

→ [test_mail.py](./test_mail.py)

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Lanza los tests con: `pytest test_mail.py`
- Puedes parar tras el primer test fallido con: `pytest -x test_mail.py`
- Puedes lanzar un test en concreto con: `pytest test_mail.py::test_build_mail`

## Al finalizar

- Sube únicamente el fichero `mail.py`

## Evaluación

- Cada test cuenta 0.5 puntos.
- La nota final corresponderá a la suma de los tests que hayan pasado.
- Hay que tener en cuenta que se puede bajar nota en función de la calidad del código implementado.
- La copia parcial o total supondrá un 0 en la nota global de la prueba.
