# Pasos posteriores a la instalación

## Herramientas varias

```console
sudo apt install -y curl git tree xclip fonts-powerline \
fonts-firacode psmisc zip fonts-noto-color-emoji
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
curl -fLo ~/.vimrc https://raw.githubusercontent.com/sdelquin/pro/main/ut0/files/.vimrc
```

Instalar los plugins:

```console
vi +'PlugInstall --sync' +qa
```

Enlazar la configuración de vim para que funcione igual con `sudo`:

```console
sudo -- sh -c "ln -sf $HOME/.vimrc /root/.vimrc; ln -sf $HOME/.vim /root/.vim"
```

## `.bashrc`

Configuraciones a nivel de usuario → [.bashrc](files/.bashrc)

```console
curl -fLo ~/.bashrc https://raw.githubusercontent.com/sdelquin/pro/main/ut0/files/.bashrc &&
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
mkdir -p ~/.config/systemd/user &&
curl -fLo ~/.config/systemd/user/autocutsel.service https://raw.githubusercontent.com/sdelquin/pro/main/ut0/files/autocutsel.service &&
systemctl --user daemon-reload &&
systemctl --user enable autocutsel &&
systemctl --user start autocutsel
```

## Script de mantenimiento

```console
curl -sfL https://raw.githubusercontent.com/sdelquin/pro/main/ut0/files/maintenance.service | \
sudo tee /etc/systemd/system/maintenance.service > /dev/null &&
sudo systemctl daemon-reload &&
sudo systemctl enable maintenance &&
sudo systemctl start maintenance
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
curl -fLo ~/.config/xfce4/terminal/terminalrc https://raw.githubusercontent.com/sdelquin/pro/main/ut0/files/terminalrc
```

> 💡 &nbsp;Para que los cambios surtan efecto, cierra la terminal y vuelve a abrirla.

## Pantalla a negro

Vamos a configurar **un atajo de teclado en <kbd>Ctrl-B</kbd> que pone la pantalla a negro**. ¡Muy útil cuando el profe está explicando!

Lo primero será crear un pequeño programa que lleve a cabo esta acción:

```console
echo 'xset s blank ; sleep 1 ; xset s activate' | \
sudo tee /usr/local/bin/black_screen.sh && \
sudo chmod +x /usr/local/bin/black_screen.sh
```

A continuación asignamos la combinación de teclas para que ejecute la acción anterior:

```console
xfconf-query -c xfce4-keyboard-shortcuts -n -t \
'string' -p '/commands/custom/<Primary><Ctrl>b' -s \
/usr/local/bin/black_screen.sh
```

> 💡 Recuerda <kbd>Ctrl-B</kbd> (de **B**lack) para poner la pantalla a negro.
