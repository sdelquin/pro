# Pasos posteriores a la instalación

## Sudoers

Dar permisos de superusuario al `<usuario>` ordinario que creamos durante la instalación del sistema operativo:

```console
$ su -l
$ addgroup <usuario> sudo
```

> Salir de la sesión y volver a entrar para que los cambios surtan efecto.

## Herramientas varias

```console
$ sudo apt install -y curl git
```

## Vim

Instalar editor vim:

```console
$ sudo apt install -y vim
```

### Vim plug

```console
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Configuraciones básicas de vim:

```console
$ curl https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.vimrc -o ~/.vimrc
```

Instalar los plugins:

```console
$ vi +'PlugInstall --sync' +qa
```

## Path

Añadir carpeta local al PATH:

```console
$ echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```

## Aspecto agradable

```console
$ sudo apt install -y materia-gtk-theme papirus-icon-theme
```

Para establecer el **tema**:

- Aplicaciones → Configuración → Apariencia → Estilo → Materia
- Aplicaciones → Configuración → Gestor de ventanas → Materia

Para establecer el paquete de **iconos**:

- Aplicaciones → Configuración → Apariencia → Iconos → Papirus
