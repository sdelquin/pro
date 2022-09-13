# Instalación del sistema operativo

![Debian Logo](files/debian-logo.jpg)

En la búsqueda de un sistema operativo que consuma pocos recursos y que nos proporcione las herramientas que necesitamos, vamos a trabajar con [Debian](https://www.debian.org/index.es.html), un sistema operativo completamente libre que es un referente dentro del mundo Linux.

## Preparación

1. Descargar la imagen del sistema operativo [Debian 11 Netinst AMD64](https://www3.gobiernodecanarias.org/medusa/eforma/campus/mod/url/view.php?id=5010751).
2. Abrir VirtualBox y crear una VM con la siguientes características:
   - RAM: 2GB
   - Disco duro: 20GB
3. Seleccionar la imagen del sistema operativo para el CD y arrancar la VM.

## Instalación

_(utilizar las teclas de cursor, ya que el ratón no funciona durante la instalación)_

1. Seleccionar _Install_ desde el menú principal.
2. Seleccionar idioma _Spanish_.
3. Seleccionar país _España_.
4. Seleccionar teclado _Español_.
5. Introducir el nombre de la máquina.
6. Introducir el nombre del dominio: dejar el que viene por defecto `localdomain`.
7. Introducir la clave de superusuario (`root`). ¡No la olvides!
8. Volver a confirmar la clave de superusuario.
9. Crear cuenta de usuario "ordinario":
   - Nombre completo indicando _nombre y apellidos_.
   - Nombre de usuario: todo en minúsculas y sin espacios.
   - Contraseña. ¡No la olvides!
   - Verificar la contraseña introducida.
10. Introducir la zona horaria _Islas Canarias_.
11. Particionado del disco:
    - Indicar particionado _Guiado (utilizar todo el disco)_
    - Elegir el disco a particionar: Sólo debería haber uno.
    - Esquema de particionado: _Todos los ficheros en una partición_.
    - Particionado de discos: _Finalizar el particionado y escribir los cambios en el disco_.
    - ¿Desea escribir los cambios en los discos? _Sí_ (utilizar tabulador para cambiar de opción)
12. Gestor de paquetes:
    - ¿Desea analizar otros medios de instalación adicionales? _No_.
    - País de la réplica de Debian: _España_.
    - Réplica de Debian: _deb.debian.org_
    - Proxy HTTP: _Dejar en blanco_ (pulsar ENTER)
    - ¿Desea participar en la encuesta sobre el uso de paquetes? _No_.
13. Elegir los programas a instalar. Marcar lo siguiente (utilizando los cursores y la barra espaciadora):
    - Xfce.
    - SSH Server.
    - Utilidades estándar del sistema.
    - _(utilizar el tabulador y luego ENTER para continuar)_
14. Instalación completada: _Extraer el medio de instalación y continuar_.
