# Instrucciones para el desarrollo de las POP

## Antes de empezar

- Actualiza el paquete de comprobación de ejercicios:

```console
pycheck update
```

> ⚠️ Si este comando da error, puedes actualizar con `pip install -U git+http://g.pycheck.es`

- Trabaja en la carpeta adecuada:

```console
mkdir -p ~/pro/ut2/pop1 && cd ~/pro/ut2/pop1 && code .
```

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Crea la plantilla del ejercicio con `pycheck template <ejercicio>`
- Muestra la descripción del ejercicio con `pycheck show <ejercicio>`
- Comprueba tu ejercicio contra los casos de prueba con `pycheck check <ejercicio>`
- Recuerda que puedes lanzar un único caso de prueba con `pycheck check -n1 <ejercicio>`

## Al finalizar

- Estando en la carpeta de trabajo, comprime los archivos con:

```console
cd ~/pro/ut2/pop1 && zip ut2-pop1.zip *.py
```

- Sube únicamente el fichero comprimido `ut2-pop1.zip`

🚨 Para que el ejercicio **funcione correctamente** tiene que **funcionar para todos los casos de prueba establecidos por el profe**.