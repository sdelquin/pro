#!/bin/bash

sudo apt install -y vim curl git tree xclip fonts-powerline fonts-firacode psmisc autocutsel materia-gtk-theme papirus-icon-theme

curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
curl -fLo ~/.vimrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.vimrc
vi -E -s +PlugInstall +qall

sudo -- sh -c "ln -sf $HOME/.vimrc /root/.vimrc; ln -sf $HOME/.vim /root/.vim"

curl -fLo ~/.bashrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.bashrc
source ~/.bashrc

mkdir -p ~/.config/systemd/user
curl -fLo ~/.config/systemd/user/autocutsel.service https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/autocutsel.service
systemctl --user daemon-reload
systemctl --user enable autocutsel
systemctl --user start autocutsel

curl -fLo ~/.config/xfce4/terminal/terminalrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/terminalrc
