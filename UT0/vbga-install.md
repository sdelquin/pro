# VirtualBox Guest Additions

Para habilitar funciones como el ajuste del tamaño de la ventana o la función de copiar y pegar, debemos instalar las [Guest Additions](https://www.virtualbox.org/manual/ch04.html) de VirtualBox.

## Carga de la imagen

1. Con la máquina virtual apagada, asegúrate de que no hay nada cargado en el CDROM. Para ello hay que ir a: _Configuración → Almacenamiento → Controlador IDE → Vacío_
2. A continuación arranca la máquina virtual e inicia sesión normalmente con tu usuario habitual.
3. Ahora, desde el menú superior de la máquina virtual, vete a: _Dispositivos → Insertar imagen de CD de las "Guest Additions"..._
4. Esto hará que aparezca un icono de un CD con un nombre parecido a `VBox_GAs_X.Y.Z`

## Preparación previa

Necesitamos instalar una serie de paquetes previos:

```console
$ sudo apt install dkms linux-headers-$(uname -r) build-essential
```

## Instalación

Ahora ya podemos montar la unidad de CDROM y lanzar el instalador de las "Guest Additions" de VirtualBox:

```console
$ sudo mount /dev/cdrom /mnt  # No te preocupes por el mensaje de "Read Only"
$ sudo sh /mnt/VBoxLinuxAdditions.run
...
...
```

## Pasos finales

Apagamos la máquina virtual:

```console
$ sudo poweroff
```

Con la máquina apagada, vamos a desmontar la imagen de las "Guest Additions". Para ello: _Configuración → Almacenamiento → Controlador IDE → (botón derecho) → Eliminar imagen_

Ahora activamos el uso del portapapeles. Para ello:

- _Configuración → General → Avanzado → Compartir portapapeles → Bidireccional_
- _Configuración → General → Avanzado → Arrastrar y soltar → Bidireccional_

Pulsamos en "Aceptar" y listo. Ya podemos arrancar la máquina con las herramientas instaladas.
