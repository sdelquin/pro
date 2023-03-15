# Instalación de Python

Actualizamos los repositorios:

```console
sudo apt update
```

Instalamos los prerrequisitos:

```console
sudo apt install -y build-essential zlib1g-dev libncurses5-dev \
libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev \
libsqlite3-dev wget libbz2-dev
```

Descargamos la última versión disponible de Python:

```console
curl https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz | tar xvz -C /tmp &&
cd /tmp/Python-3.11.0
```

Configuramos la instalación:

```console
./configure --enable-optimizations
```

Compilamos el intérprete:

```console
make -j `nproc`
```

> Esto puede tardar un poco de tiempo. ¡Paciencia!

Ejecutamos la instalación, respetando la versión por defecto de Python que hay en el sistema:

```console
sudo make altinstall
```

Hacemos que esta nueva versión de Python sea la versión por defecto en el sistema:

```console
sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 10
```

Ahora podemos comprobar que la nueva versión quedó correctamente configurada:

```console
cd; python --version
```

→ `Python 3.11.0`

## Instalación de paquetes

Lo primero es asegurarnos de tener la última versión del instalador de paquetes:

```console
python -m pip install -U pip
```

A continuación instalamos los paquetes que necesitamos para desarrollo:

- [black](https://black.readthedocs.io/en/stable/): formateador de código en Python.
- [mypy](https://www.mypy-lang.org/): chequeador de tipos en Python.
- [iPython](https://ipython.org/): consola interactiva "vitaminada" para Python.
- [wheel](https://github.com/pypa/wheel): paquete soporte para instalar otros paquetes.
- [cowsay](https://github.com/VaasuDevanS/cowsay-python): la vaca feliz.

```console
pip install black mypy ipython wheel cowsay
```

## La vaca feliz

Si todo ha ido bien, podrás ver a la vaca feliz 🐮:

```console
python -c 'import cowsay; cowsay.cow("Genial")'
```
