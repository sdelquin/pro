# Instalación del sistema operativo

![Debian Logo](images/debian-logo.jpg)

En la búsqueda de un sistema operativo que consuma pocos recursos y que nos proporcione las herramientas que necesitamos, vamos a trabajar con [Debian](https://www.debian.org/index.es.html), un sistema operativo completamente libre que es un referente dentro del mundo Linux.

## Preparación

1. Descargar la imagen del sistema operativo [Debian 12 Netinst AMD64](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso).
2. Abrir VirtualBox y crear una **nueva máquina virtual** con las siguientes características:

| Parámetro | Valor                       |
| --------- | --------------------------- |
| Nombre    | _(pregunta al profe)_       |
| Carpeta   | _(la que está por defecto)_ |
| Tipo      | Linux                       |
| Versión   | Debian (64-bit)             |
| RAM       | 4096MB                      |

3. Disco duro → Crear un disco duro virtual ahora
4. Tipo de archivo de disco duro → VDI
5. Almacenamiento en unidad de disco duro → Tamaño fijo
6. Tamaño del disco duro → 30GB
7. Disco duro → Crear un disco duro virtual ahora
8. Una vez creada la máquina, botón derecho sobre la máquina: Configuración → Red → Adaptador 1 → Conectado a: Adaptador puente

**Arrancar la máquina virtual**. En este momento nos pedirá que elijamos un disco de inicio. En el botón de selección hay que localizar la imagen que hemos descargado `.iso` (probablemente estará en la carpeta Descargas).

## Instalación

⚠️ **¡Utilizar las teclas de cursor, ya que el ratón no funciona durante la instalación!**

### Paso 1

![](./images/debian-install/debian-install01.png)

### Paso 2

![](./images/debian-install/debian-install02.png)

### Paso 3

![](./images/debian-install/debian-install03.png)

### Paso 4

![](./images/debian-install/debian-install04.png)

### Paso 5

![](./images/debian-install/debian-install05.png)

### Paso 6

![](./images/debian-install/debian-install06.png)

### Paso 7

⚠️ **¡Pregunta al profe qué nombre de máquina hay que poner!**

![](./images/debian-install/debian-install07.png)

### Paso 8

![](./images/debian-install/debian-install08.png)

### Paso 9

⚠️ **¡Introduce una contraseña de superusuario! ¡No la olvides!**

![](./images/debian-install/debian-install09.png)

### Paso 10

⚠️ **¡Repite la contraseña que acabas de poner!**

![](./images/debian-install/debian-install10.png)

### Paso 11

⚠️ **¡Escribe tu nombre y apellidos!**

![](./images/debian-install/debian-install11.png)

### Paso 12

⚠️ **¡Si te llamas Héctor David López Gutiérrez, tu usuario debería ser algo como `hector`!**

![](./images/debian-install/debian-install12.png)

### Paso 13

⚠️ **¡Introduce una contraseña para tu usuario "habitual"! ¡No la olvides!**

![](./images/debian-install/debian-install13.png)

### Paso 14

⚠️ **¡Repite la contraseña que acabas de poner!**

![](./images/debian-install/debian-install14.png)

### Paso 15

![](./images/debian-install/debian-install15.png)

### Paso 16

![](./images/debian-install/debian-install16.png)

### Paso 17

![](./images/debian-install/debian-install17.png)

### Paso 18

![](./images/debian-install/debian-install18.png)

### Paso 19

![](./images/debian-install/debian-install19.png)

### Paso 20

![](./images/debian-install/debian-install20.png)

### Paso 21

![](./images/debian-install/debian-install21.png)

### Paso 22

![](./images/debian-install/debian-install22.png)

### Paso 23

![](./images/debian-install/debian-install23.png)

### Paso 24

![](./images/debian-install/debian-install24.png)

### Paso 25

![](./images/debian-install/debian-install25.png)

### Paso 26

![](./images/debian-install/debian-install26.png)

### Paso 27

![](./images/debian-install/debian-install27.png)

### Paso 28

![](./images/debian-install/debian-install28.png)

### Paso 29

⚠️ **¡Marca EXCLUSIVAMENTE lo que está indicado en la imagen usando la BARRA ESPACIADORA!**

![](./images/debian-install/debian-install29.png)

### Paso 30

![](./images/debian-install/debian-install30.png)

### Paso 31

![](./images/debian-install/debian-install31.png)

### Paso 32

![](./images/debian-install/debian-install32.png)

### Paso 33

![](./images/debian-install/debian-install33.png)

### Paso 34

⚠️ **¡Introduce tu usuario habitual y la contraseña correspondiente!**

![](./images/debian-install/debian-install34.png)

## Sudoers

Por defecto, el único usuario que tiene "superpoderes" en Linux es `root` (superusuario). Pero nos puede venir bien que nuestro usuario "habitual" también sea un superhéroe. Para ello debemos hacerlo _sudoer_.

Después de arrancar la máquina virtual que acabamos de crear, iniciamos sesión con nuestro usuario "habitual", abrimos una **terminal** y ejecutamos lo siguiente:

![Terminal](images/terminal.png)

```console
su -c "/sbin/addgroup <usuario> sudo"
```

> 💡 &nbsp;No incluyas los angulitos `<` `>` en la instrucción, sustituye por el nombre de tu usuario.

A continuación debes **salir de la sesión y volver a entrar** para que los cambios surtan efecto.

![Cerrar sesión](images/close-session.jpg)
