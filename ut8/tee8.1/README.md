# TEE8.1

### TAREA EVALUABLE EJERCICIOS

![Python sticker](../../python-sticker.png)

## Comprimir los ejercicios

Ejecuta los siguientes comandos:

```console
cd ~/pro/ut7 && zip -FSr tee_ut7.zip . -x '*.mypy_cache*' -x '*.pytest_cache*' -x '*__pycache__*' -x '*pop*' -x '*tep*'
```

> Esto genera el archivo `tee_ut7.zip` con todos los ejercicios de la UT7.

```console
cd ~/pro/ut8 && zip -FSr tee_ut8.zip . -x '*.mypy_cache*' -x '*.pytest_cache*' -x '*__pycache__*' -x '*pop*' -x '*tep*'
```

> Esto genera el archivo `tee_ut8.zip` con todos los ejercicios de la UT8.

## Entrega

- Sube los ficheros comprimidos a la tarea correspondiente del aula virtual.

## Evaluación

- La puntuación final de la prueba estará en función del **número de tests** que se hayan superado.
- Podrá haber penalizaciones por **copia** o **calidad del código**.
