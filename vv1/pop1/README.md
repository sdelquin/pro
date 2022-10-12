# UT1: Identificación de los elementos de un programa informático

![Python sticker](../../python-sticker-xs.png)

# POP1: Prueba Objetiva Práctica 1

## `ejercicio1.py`

Escribe un programa en Python que partiendo de dos valores enteros $a$ y $b$ calcule el resultado de la siguiente expresión:

$$
F = a^2 + b^2 - \sqrt{(a \cdot b)}
$$

```python
# UT1-POP1-EJ1
a = 5
b = 7
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓


# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert F == 68.08392021690038
```

## `ejercicio2.py`

Escribe un programa en Python que dado un número entero calcule el número de 1s que contiene su representación binaria.

```python
# UT1-POP1-EJ2
number = 99
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓


# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert count_ones == 4
```

## `ejercicio3.py`

Escribe un programa en Python que realice el desplazamiento (_offset_) de la vocal indicada en una determinada cadena de texto.

Notas:

- Hay que buscar el _offset_ de la vocal indicada dentro de la constante `VOWELS`.
- No hay que preocuparse de _offsets_ demasiado grandes o demasiados pequeños. Eso no va a ocurrir.
- Reemplazar la vocal indicada por la correspondiente calculada según el _offset_.

```python
# UT1-POP1-EJ3
VOWELS = 'aeiou'
target_vowel = 'e'
target_offset = 2
input_text = 'Hay una gran diferencia entre conocer el camino y andar el camino'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓


# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert output_text == 'Hay una gran diforoncia ontro conocor ol camino y andar ol camino'
```

## `ejercicio4.py`

Escribe un programa en Python que convierta la representación hexadecimal de un color en su versión decimal RGB.

```python
# UT1-POP1-EJ4
hexcolor = 'A131F7'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓


# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert rgb_color == '(161,49,247)'
```

## Instrucciones de entrega

- Trabaja en una carpeta `~/pro/ut1/pop1/`
- Recuerda llamar a cada fichero con el nombre indicado: `ejercicio1.py`, `ejercicio2.py`, etc. **Todo en minúsculas, sin espacios y con la extensión .py**
- Estando en la carpeta de trabajo, comprime los archivos con: `zip ut1-pop1.zip *.py`
- Sube únicamente el fichero comprimido `ut1-pop1.zip`.
