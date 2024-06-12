# UT5-POP2: Librerías

### PRUEBA OBJETIVA PRÁCTICA: RECUPERACIÓN

![Python sticker](../../python-sticker.png)

## Objetivo

Esta prueba consiste en la implementación de un **carrito de la compra** a través de las clases `User`, `Product` y `Cart`.

## Puesta en marcha

```console
mkdir -p ~/pro/ut5/pop2
cd ~/pro/ut5/pop2
wget https://raw.githubusercontent.com/sdelquin/pro/main/ut5/pop2/templates/ecommerce.py
wget https://raw.githubusercontent.com/sdelquin/pro/main/ut5/pop2/test_ecommerce.py
```

## Base de datos

- Un usuario (`user`) compra uno o varios productos (`product`) en un carrito de la compra (`cart`).
- Puede adquirir varias unidades `(qty)` de cada producto.

![ERD](./erd.svg)

Leyenda:

| Símbolo | Descripción |
| ------- | ----------- |
| I       | INTEGER     |
| T       | TEXT        |
| R       | REAL        |
| U       | UNIQUE      |

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Lanza los tests con: `pytest`
- Puedes parar tras el primer test fallido con: `pytest -x`
- Puedes lanzar un test en concreto con: `pytest -k <nombre-del-test>`

## Calificación

- La calificación de la prueba vendrá determinada por el número de tests que se hayan pasado.
- En cualquier caso se podrá bajar nota en función de la calidad y eficiencia del código implementado.
- La copia parcial o total supondrá un 0 en la nota global de la prueba.

## Entrega

Sólo es necesario subir al aula virtual **el fichero .py con tu código**.
