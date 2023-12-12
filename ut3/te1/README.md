# UT3-TE1: Estructuras de datos → Listas

### TAREA EVALUABLE

![Python sticker](../../python-sticker.png)

## Objetivo

Escriba un programa en Python que permita jugar a **HUNDIR LA FLOTA**.

## Desarrollo del juego

- Sólo juega una persona con un tablero `board` generado aleatoriamente.
- Este tablero `board` tendrá un tamaño de 10x10 (como lista de listas) donde cada celda puede ser:
  - **Vacío** representado por ⬛
  - **Barco** representado por una combinación de letra+dígito.
- Habrá los siguientes barcos:
  - 1 barco de longitud 5 (`5A`)
  - 1 barco de longitud 4 (`4A`)
  - 2 barcos de longitud 3 (`3A` y `3B`)
  - 1 barco de longitud 2 (`2A`)
- En cada "turno" habrá que indicar la posición de tiro: `A4`, `B7`, `C1`, ... donde las letras representan filas y los números representan columnas.
- En cada "turno" habrá que mostrar el tablero con los intentos realizados:
  - **Celda inexplorada** representado por ⬛
  - **Agua** representado por 🟦
  - **Barco tocado** representado por 🟧
  - **Barco hundido** representado por 🟥
- En cada turno habrá también que mostrar la puntuación alcanzada hasta ese momento.
- El juego termina cuando se han hundido todos los barcos.

## Puntuaciones

| Jugada           | Puntuación              |
| ---------------- | ----------------------- |
| AGUA             | 0                       |
| TOCADO           | 1 \* Longitud del barco |
| TOCADO Y HUNDIDO | 3 \* Longitud del barco |

## Punto de partida

Descarga [aquí](./sinkfleet.py) la plantilla para empezar a trabajar.

## Vídeo explicativo

Aquí tienes [un vídeo explicativo](https://www.youtube.com/watch?v=6s0qEROba4g) de cómo se juega a hundir la flota.

## Notas

- Utilizar sólo herramientas de Python que se hayan visto hasta el momento en clase.
