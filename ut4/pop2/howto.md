# Instrucciones para el desarrollo de las POP

## Antes de empezar

- Actualiza el paquete de comprobación de ejercicios:

```console
pycheck update
```

> ⚠️ Si este comando da error, puedes actualizar con `pip install -U git+http://get.pycheck.es`

- Trabaja en la carpeta adecuada:

```console
mkdir -p ~/pro/ut4/pop2 && cd ~/pro/ut4/pop2
```

- Mira los ejercicios del examen y crea las plantillas:

```console
pycheck boot <ejercicio.py>
```

- Abre _Visual Studio Code_ para empezar a trabajar:

```console
code .
```

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Puedes mostrar la descripción del ejercicio con `pycheck show <ejercicio>`
- Puedes volver a generar la plantilla del ejercicio con `pycheck template <ejercicio>`
- Puedes comprobar tu ejercicio contra los casos de prueba con `pycheck check <ejercicio>`
- Recuerda que puedes lanzar un único caso de prueba con `pycheck check -n1 <ejercicio>`

## Al finalizar

- Crea un fichero `.zip` con todos los ejercicios de la prueba ejecutando el siguiente comando:

```console
cd ~/pro/ut4/pop2 && zip ut4-pop2.zip *.py
```

- Abre un navegador **en la máquina virtual** y accede a la entrega de la actividad **en el aula virtual de Programación**.
- Sube únicamente el fichero comprimido `ut4-pop2.zip`

## Evaluación

🚨 Para que el ejercicio **funcione correctamente** tiene que **funcionar para todos los casos de prueba establecidos por el profe**.

☝️ El **profe** puede lanzar el ejercicio con aquellos **casos de prueba que crea conveniente** para comprobar que **funciona de forma general para cualquier tipo de entrada**.