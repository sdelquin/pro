# TEE3.1

### TAREA EVALUABLE EJERCICIOS

![Python sticker](../../python-sticker.png)

## Comprimir los ejercicios

Ejecuta los siguientes comandos:

```console
cd ~/pro/ut2 && zip -FSr tee_ut2.zip . -x '*.mypy_cache*' -x '*.pytest_cache*' -x '*__pycache__*' -x '*pop*' -x '*tep*'
```

> Esto genera el archivo `tee_ut2.zip` con todos los ejercicios de la UT2.

```console
cd ~/pro/ut3 && zip -FSr tee_ut3.zip . -x '*.mypy_cache*' -x '*.pytest_cache*' -x '*__pycache__*' -x '*pop*' -x '*tep*'
```

> Esto genera el archivo `tee_ut3.zip` con todos los ejercicios de la UT3.

## Entrega

- Sube los ficheros comprimidos a la tarea correspondiente del aula virtual.

## Evaluación

- La puntuación final de la prueba estará en función del **número de tests** que se hayan superado.
- Podrá haber penalizaciones por **copia** o **calidad del código**.
