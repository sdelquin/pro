# Instalación de Python

Instalamos los prerrequisitos:

```console
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

Creamos una carpeta temporal y descargamos la última versión disponible de Python:

```console
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tgz
$ tar -xf Python-3.10.7.tgz
$ cd Python-3.10.7
```

Configuramos la instalación:

```console
$ ./configure --enable-optimizations
...
```

Compilamos el intérprete:

```console
$ make -j `nproc`
...
```

Ejecutamos la instalación, respetando la versión por defecto de Python que hay en el sistema:

```console
$ sudo make altinstall
```

Comprobamos que hemos instalado correctamente la versión de Python:

```console
$ python3.10 --version
Python 3.10.7
```

Hacemos que esta nueva versión de Python sea la versión por defecto en el sistema:

```console
$ update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1
```

Podemos comprobar que la nueva versión quedó correctamente configurada:

```console
$ python --version
Python 3.10.7
```

## Instalación de paquetes

- [Black](https://black.readthedocs.io/en/stable/): formateador de código en Python.
- [IPython](https://ipython.org/): consola interactiva "vitaminada" para Python.

```console
$ python -m pip install black ipython
```
