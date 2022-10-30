# UT1-POP0: Identificación de los elementos de un programa informático

### PRUEBA OBJETIVA PRÁCTICA → 🧑🏻‍🚒 SIMULACRO

![Python sticker](../../python-sticker.png)

## ⚡ Instrucciones

**Lee detenidamente** [las instrucciones para el desarrollo de la prueba](./howto.md).

## `ejercicio1.py`

Escribe un programa en Python que dada una cantidad (entera) de tiempo en segundos, calcule el número de horas, minutos y segundos que corresponden.

```python
import sys

import pycheck

CHECK_CASES = [
    [[31256], (8, 40, 56)],
    [[3601], (1, 0, 1)],
    [[9099], (2, 31, 39)],
]


def run(seconds: int) -> tuple:
    # TU CÓDIGO AQUÍ
    return hours, minutes, seconds


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio2.py`

Escribe un programa en Python que dada una secuencia de ADN calcule el porcentaje de presencia de cada base (sobre el total).

```python
import sys

import pycheck

CHECK_CASES = [
    [['GGTTACCAACCCAGTCGAAAATTTGGTCAGGG'], (28.125, 28.125, 21.875, 21.875)],
    [['ATGGGATCCTAGCCCCTTAG'], (20.0, 25.0, 25.0, 30.0)],
    [['GGATTCTGAGAATCCGCTAATGCC'], (25.0, 25.0, 25.0, 25.0)],
]


def run(adn: str):
    # TU CÓDIGO AQUÍ
    return adenines_rate, guanines_rate, thymines_rate, cytosines_rate


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```
