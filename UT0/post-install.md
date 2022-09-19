# Pasos posteriores a la instalación

## Herramientas varias

```console
$ sudo apt install -y curl git tree
```

## Vim

Instalar editor [vim](https://es.wikipedia.org/wiki/Vim):

```console
$ sudo apt install -y vim
```

### Vim plug

```console
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Configuraciones básicas de vim → [.vimrc](files/.vimrc)

```console
$ curl https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.vimrc -o ~/.vimrc
```

Instalar los plugins:

```console
$ vi +'PlugInstall --sync' +qa
```

> vim se abrirá de manera automática, instalará los plugins y se volverá a cerrar. No tocar nada hasta que vuelva a la terminal.

## `.bashrc`

Configuraciones a nivel de usuario → [.bashrc](files/.bashrc)

```console
$ curl https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.bashrc -o ~/.bashrc
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

## Desactivar confirmación de pegado inseguro

Abrimos la **terminal** y vamos al menú:

- Editar → Preferencias → General → Mostrar diálogo de pegar inseguro (desactivar)
