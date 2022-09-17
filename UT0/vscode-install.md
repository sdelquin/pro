# Visual Studio Code

## Instalación

Creamos una carpeta temporal y descargamos la última versión disponible de VSCode:

```console
$ cd /tmp
$ wget "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64" -O vscode.deb
```

Instalamos el paquete:

```console
$ sudo apt install ./vscode.deb
...
```

Comprobamos que la instalación ha sido satisfactoria:

```console
$ code --version
1.71.1
e7f30e38c5a4efafeec8ad52861eb772a9ee4dfb
amd64
```

## Preparación para desarrollo Python

Debemos instalar una serie de extension y personalizar la configuración de Visual Studio Code para que nos permita trabajar de forma cómoda con Python.

### Instalación de extensiones

```console
$ code --install-extension ms-python.python
```

### Configuraciones

Descargamos las configuraciones personalizadas para Visual Studio Code:

```console
$ curl https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/settings.json -o ~/.config/Code/User/settings.json
```

## Apertura de la aplicación

Creamos una carpeta `dev` para desarrollo y abrimos Visual Studio Code en esa ubicación:

```console
$ cd $HOME
$ mkdir dev
$ cd dev
~/dev$ code .
```

Es posible que VSCode nos pregunte la primera vez si confiamos en la ubicación que estamos abriendo. Marcar que sí y continuar.
