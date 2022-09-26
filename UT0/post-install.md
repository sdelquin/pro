# Pasos posteriores a la instalación

## Herramientas varias

```console
sudo apt install -y curl git tree xclip fonts-powerline fonts-firacode
```

## Vim

Instalar editor [vim](https://es.wikipedia.org/wiki/Vim):

```console
sudo apt install -y vim
```

### Vim plug

```console
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Configuraciones básicas de vim → [.vimrc](files/.vimrc)

```console
curl -fLo ~/.vimrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.vimrc
```

Instalar los plugins:

```console
vi +'PlugInstall --sync' +qa
```

> vim se abrirá de manera automática, instalará los plugins y se volverá a cerrar. No tocar nada hasta que vuelva a la terminal. Si diera algún error, basta con pulsar <kbd>ENTER</kbd>.

Enlazar la configuración de vim para que funcione igual con `sudo`:

```console
sudo -- sh -c "ln -s $HOME/.vimrc /root/.vimrc; ln -s $HOME/.vim /root/.vim"
```

## `.bashrc`

Configuraciones a nivel de usuario → [.bashrc](files/.bashrc)

```console
curl -fLo ~/.bashrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.bashrc
source ~/.bashrc
```

## Copiar con selección

Ahora vamos a habilitar la opción de copiar al portapapeles únicamente con seleccionar el texto.

Lo primero es instalar el programa `autocutsel`:

```console
sudo apt install -y autocutsel
```

Ahora creamos un servicio para que funcione de manera permanente (y se active en el arranque):

```console
mkdir -p ~/.config/systemd/user
curl -fLo ~/.config/systemd/user/autocutsel.service https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/autocutsel.service
systemctl --user daemon-reload
systemctl --user enable autocutsel
systemctl --user start autocutsel
```

## Aspecto agradable

```console
sudo apt install -y materia-gtk-theme papirus-icon-theme
```

Para establecer el **tema**:

- Aplicaciones → Configuración → Apariencia → Estilo → Materia
- Aplicaciones → Configuración → Gestor de ventanas → Materia

Para establecer el paquete de **iconos**:

- Aplicaciones → Configuración → Apariencia → Iconos → Papirus

## Ajustes de Terminal

```console
curl -fLo ~/.config/xfce4/terminal/terminalrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/terminalrc
```
