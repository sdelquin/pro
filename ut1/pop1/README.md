# UT1-POP1: Identificación de los elementos de un programa informático

### PRUEBA OBJETIVA PRÁCTICA

![Python sticker](../../python-sticker.png)

## ⚡ Instrucciones

**Lee detenidamente** [las instrucciones para el desarrollo de la prueba](./howto.md).

## `ejercicio1.py`

Escribe un programa en Python que partiendo de dos valores enteros $a$ y $b$ calcule el resultado de la siguiente expresión:

$$
F = a^2 + b^2 - \sqrt{(a \cdot b)}
$$

```python
import sys

import pycheck

CHECK_CASES = [
    [[5, 7], 68.08392021690038],
    [[6, 2], 36.53589838486224],
    [[21, 4], 447.83484861008833],
]


def run(a: int, b: int) -> float:
    # TU CÓDIGO AQUÍ
    return F


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio2.py`

Escribe un programa en Python que dado un número entero calcule el número de 1s que contiene su representación binaria.

```python
import sys

import pycheck

CHECK_CASES = [
    [[99], 4],
    [[201], 4],
    [[3219], 6],
]


def run(number: int) -> int:
    # TU CÓDIGO AQUÍ
    return count_ones


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio3.py`

Escribe un programa en Python que realice el desplazamiento (_offset_) de la vocal indicada en una determinada cadena de texto.

Notas:

- Hay que buscar el _offset_ de la vocal indicada dentro de la constante `VOWELS`.
- No hay que preocuparse de _offsets_ demasiado grandes o demasiados pequeños. Eso no va a ocurrir.
- Reemplazar la vocal indicada por la correspondiente calculada según el _offset_.

```python
import sys

import pycheck

CHECK_CASES = [
    [['e', 2, 'diferencia'], 'diforoncia'],
    [['u', -2, 'uruguay'], 'irigiay'],
    [['a', 4, 'anatolia'], 'unutoliu'],
]


def run(target_vowel: str, target_offset: int, input_text: str) -> str:
    # TU CÓDIGO AQUÍ
    return output_text


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio4.py`

Escribe un programa en Python que convierta la representación hexadecimal de un color en su versión decimal RGB.

```python
import sys

import pycheck

CHECK_CASES = [
    [['A131F7'], '(161,49,247)'],
    [['FF11FF'], '(255,17,255)'],
    [['123456'], '(18,52,86)'],
]


def run(hex_color: str) -> str:
    # TU CÓDIGO AQUÍ
    return rgb_color


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```

## `ejercicio5.py`

Escribe un programa en Python que permita crear un "slug" a partir de una cadena de texto. Un slug es una cadena de texto con las siguientes características:

- Todas las letras están en minúsculas.
- Los espacios se sustituyen por guiones medios.
- Las vocales con tilde se sutituyen por vocales sin tilde.

```python
import sys

import pycheck

CHECK_CASES = [
    [['hola probando'], 'hola-probando'],
    [['áéíóú'], 'aeiou'],
    [['TWIST & SHOUT'], 'twist-&-shout'],
]


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    return slug


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
```
