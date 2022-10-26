# UT2-POP0: Uso de estructuras de control

### PRUEBA OBJETIVA PRÁCTICA → 🧑🏻‍🚒 SIMULACRO

![Python sticker](../../python-sticker.png)

## Instrucciones

### Antes de empezar

- Actualiza el paquete de comprobación de ejercicios:

```console
pip install -U git+https://github.com/sdelquin/pycheck.git
```

- Trabaja en la carpeta adecuada:

```console
mkdir -p ~/pro/ut2/pop0 && cd ~/pro/ut2/pop0 && code .
```

### Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Recuerda llamar a cada fichero con el nombre indicado: `ejercicio1.py`, `ejercicio2.py`, etc. **Todo en minúsculas, sin espacios y con la extensión .py**
- Tienes 3 modos de probar tus ejercicios (desde una terminal):
  - Contra los casos establecidos por el profe: `python <ejercicioX.py> -k`
  - Listar los casos establecidos por el profe: `python <ejercicioX.py> -l`
  - Usando tus propios valores de entrada: `python <ejercicioX.py> [ARG1] [ARG2] ...`

📣 Todos los valores de entrada que especifiques en línea de comandos tienen que ir **entre comillas**, salvo los valores numéricos (y los booleanos).

### Al finalizar

- Estando en la carpeta de trabajo, comprime los archivos con:

```console
cd ~/pro/ut2/pop0 && zip ut2-pop0.zip *.py
```

- Sube únicamente el fichero comprimido `ut2-pop0.zip`

🚨 Para que el ejercicio **funcione correctamente** tiene que **funcionar para todos los tests establecidos por el profe**.

## `ejercicio1.py`

Escribe un programa en Python que, dada una cadena de texto, elimine todas las vocales SIN UTILIZAR LA FUNCIÓN `replace()`.

```python
import sys

import pycheck


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    return output


if __name__ == '__main__':
    pycheck.check('pro.ut2.pop0.ej1', sys.argv, run)
```

## `ejercicio2.py`

Escribe un programa en Python que, dada una cadena de texto, calcule el valor promedio de sus letras utilizando la función `ord()`.

```python
import sys

import pycheck


def run(word: str) -> float:
    # TU CÓDIGO AQUÍ
    return char_avg


if __name__ == '__main__':
    pycheck.check('pro.ut2.pop0.ej2', sys.argv, run)
```
