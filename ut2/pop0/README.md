# UT2-POP0: Uso de estructuras de control

### PRUEBA OBJETIVA PRÁCTICA → 🧑🏻‍🚒 SIMULACRO

![Python sticker](../../python-sticker.png)

## ⚡ Instrucciones

**Lee detenidamente** [las instrucciones para el desarrollo de la prueba](./howto.md).

## `ejercicio1.py`

Escribe un programa en Python que, dada una cadena de texto, elimine todas las vocales SIN UTILIZAR LA FUNCIÓN `replace()`.

```python
import sys

import pycheck

CHECK_CASES = [
    [['sergio delgado quintero'], 'srg dlgd qntr'],
    [['PEPE BENAVENTE'], 'PP BNVNT'],
    [['volando VOY, volando VENGO'], 'vlnd VY, vlnd VNG'],
]


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    return output


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio2.py`

Escribe un programa en Python que, dada una cadena de texto, calcule el valor promedio de sus letras utilizando la función `ord()`.

```python
import sys

import pycheck

CHECK_CASES = [
    [['probando'], 106.625],
    [['Buena Suerte'], 96.25],
    [['Yo escribo Python'], 97.0],
]


def run(word: str) -> float:
    # TU CÓDIGO AQUÍ
    return char_avg


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```
