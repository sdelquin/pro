# Instrucciones para el desarrollo de las POPs

## Antes de empezar

- Actualiza el paquete de comprobación de ejercicios:

```console
pip install -U git+https://github.com/sdelquin/pycheck.git
```

- Trabaja en la carpeta adecuada:

```console
mkdir -p ~/pro/ut2/pop0 && cd ~/pro/ut2/pop0 && code .
```

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Recuerda llamar a cada fichero con el nombre indicado: `ejercicio1.py`, `ejercicio2.py`, etc. **Todo en minúsculas, sin espacios y con la extensión .py**
- Copia la plantilla, borra la línea `# TU CÓDIGO AQUÍ` y escribe a partir de ahí tu solución (bien indentada). No se puede tocar nada más de la plantilla.
- Tienes 3 modos de probar tus ejercicios (desde una terminal):
  - Contra los casos establecidos por el profe: `python <ejercicioX.py>`
  - Listar los casos establecidos por el profe: `python <ejercicioX.py> -l`
  - Usando tus propios valores de entrada: `python <ejercicioX.py> [ARG1] [ARG2] ...`
- Puedes ver la ayuda ejecutando: `python <ejercicioX.py> -h`

📣 Todos los valores de entrada que especifiques en línea de comandos tienen que ir **entre comillas**, salvo los valores numéricos (y los booleanos).

## Al finalizar

- Estando en la carpeta de trabajo, comprime los archivos con:

```console
cd ~/pro/ut2/pop0 && zip ut2-pop0.zip *.py
```

- Sube únicamente el fichero comprimido `ut2-pop0.zip`

🚨 Para que el ejercicio **funcione correctamente** tiene que **funcionar para todos los tests establecidos por el profe**.