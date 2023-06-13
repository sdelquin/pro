# UT5-POP2: Módulos + Librerías

### PRUEBA OBJETIVA PRÁCTICA: RECUPERACIÓN

![Python sticker](../../python-sticker.png)

Esta prueba consiste en la implementación de un **carrito de la compra** a través de las clases `User`, `Product` y `Cart`.

## Creación de la base de datos

→ [create_db.py](./create_db.py)

- Ejecuta este fichero antes que nada para crear la base de datos `ecommerce.db`.
- Aprovecha para entender las tablas existentes y su contenido.

## Plantilla

→ [ecommerce.py](./templates/ecommerce.py)

## Tests

→ [test_ecommerce.py](./test_ecommerce.py)

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Lanza los tests con: `pytest`
- Puedes parar tras el primer test fallido con: `pytest -x`
- Puedes lanzar un test en concreto con: `pytest test_ecommerce.py::test_build_user`

## Al finalizar

- Sube únicamente el fichero `ecommerce.py`

## Evaluación

- Cada test cuenta 0.5 puntos.
- La nota final corresponderá a la suma de los tests que hayan pasado.
- Hay que tener en cuenta que se puede bajar nota en función de la calidad del código implementado.
- La copia parcial o total supondrá un 0 en la nota global de la prueba.
