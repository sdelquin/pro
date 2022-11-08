# UT2-POP1: Uso de estructuras de control

### PRUEBA OBJETIVA PRÁCTICA

![Python sticker](../../python-sticker.png)

## ⚡ Instrucciones

**Lee detenidamente** [las instrucciones para el desarrollo de la prueba](./howto.md).

## `ejercicio1.py`

Escribe un programa en Python que calcule el número de divisores que tiene un número dado.

```python
import sys

import pycheck

CHECK_CASES = [
    [[67], 2],
    [[99], 6],
    [[1024], 11],
]


def run(number: int) -> int:
    # TU CÓDIGO AQUÍ
    return num_divisors


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio2.py`

Escribe un programa en Python que implemente la lógica de un semáforo, de tal manera que pase de verde a amarillo, de amarillo a rojo y de rojo a verde. Hacer el programa utilizando los emojis 🟢 🟠 🔴

```python
import sys

import pycheck

CHECK_CASES = [
    [['🟢'], '🟠'],
    [['🟠'], '🔴'],
    [['🔴'], '🟢'],
]


def run(color: str) -> str:
    # TU CÓDIGO AQUÍ
    return new_color


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio3.py`

Escribe un programa en Python que realice la conversión de una secuencia de ADN en su correspondiente ARN. El ARN es igual que el ADN salvo que la Timina se sustituye por Uracilo (`U`).

🚨 **No se puede usar la función `replace()`** 🚨

```python
import sys

import pycheck

CHECK_CASES = [
    [['AGTCCCAGGT'], 'AGUCCCAGGU'],
    [['GCGCACTCTTCTTTGCTCTT'], 'GCGCACUCUUCUUUGCUCUU'],
    [['CCGGAGATTGGCTACTGAAGATCCA'], 'CCGGAGAUUGGCUACUGAAGAUCCA'],
]


def run(adn: str) -> str:
    # TU CÓDIGO AQUÍ
    return arn


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio4.py`

Escribe un programa en Python que, dada la edad de una madre y su hija, calcule en qué momento de sus vidas la edad de la madre será el doble que la edad de su hija. Lo que habrá que devolver es la edad de la madre y la edad de su hija en el momento en el que la madre doble en edad a su hija.

```python
import sys

import pycheck

CHECK_CASES = [
    [[67, 23], (88, 44)],
    [[50, 20], (60, 30)],
    [[28, 4], (48, 24)],
]


def run(mother_age: int, daughter_age: int) -> tuple:
    # TU CÓDIGO AQUÍ
    return target_mother_age, target_daughter_age


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```
