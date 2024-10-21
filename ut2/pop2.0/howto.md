# Instrucciones para el desarrollo de las POP

## Antes de empezar

- Trabaja en la carpeta adecuada:

```console
mkdir -p ~/pro/ut2/pop2.0 && cd ~/pro/ut2/pop2.0
```

- Mira los ejercicios del examen y crea las plantillas:

```console
pypas get <ejercicio>
```

- Abre _Visual Studio Code_ para empezar a trabajar:

```console
code .
```

## Durante la prueba

- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Puedes mostrar la descripción del ejercicio con `pypas doc`
- Puedes comprobar tu ejercicio contra los casos de prueba con `pypas test`

## Al finalizar

- Sube cada ejercicio con `pypas put`
- Crea un fichero `.zip` con todos los ejercicios de la prueba ejecutando el siguiente comando:

```console
cd ~/pro/ut2/pop2.0 && zip -r pop2.0.zip . -x '*.mypy_cache*' -x '*.pytest_cache*' -x '*__pycache__*'
```

- Abre un navegador **en la máquina virtual** y accede a la entrega de la actividad **en el aula virtual de Programación**.
- Sube únicamente el fichero comprimido `pop2.0.zip`

## Evaluación

🚨 Para que el ejercicio **funcione correctamente** tiene que **funcionar para todos los casos de prueba establecidos por el profe**.

☝️ El **profe** puede lanzar el ejercicio con aquellos **casos de prueba que crea conveniente** para comprobar que **funciona de forma general para cualquier tipo de entrada**.