#!/bin/bash

sudo apt install -y vim curl git tree xclip fonts-powerline fonts-firacode psmisc autocutsel materia-gtk-theme papirus-icon-theme zip

if [ -e ~/.vim/autoload/plug.vim ]
 then cp ~/.vim/autoload/plug.vim ~/.vim/autoload/plug.vim.bk
fi
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

if [ -e ~/.vimrc ]
 then cp ~/.vimrc ~/.vimrc.bk
fi
curl -fLo ~/.vimrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.vimrc
vi -E -s +PlugInstall +qall

sudo -- sh -c "ln -sf $HOME/.vimrc /root/.vimrc; ln -sf $HOME/.vim /root/.vim"

if [ -e ~/.bashrc ]
 then cp ~/.bashrc ~/.bashrc.bk
fi
curl -fLo ~/.bashrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/.bashrc
source ~/.bashrc

mkdir -p ~/.config/systemd/user
curl -fLo ~/.config/systemd/user/autocutsel.service https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/autocutsel.service
systemctl --user daemon-reload
systemctl --user enable autocutsel
systemctl --user start autocutsel

if [ -e ~/.config/xfce4/terminal/terminalrc ]
 then cp ~/.config/xfce4/terminal/terminalrc ~/.config/xfce4/terminal/terminalrc.bk
fi
curl -fLo ~/.config/xfce4/terminal/terminalrc https://raw.githubusercontent.com/sdelquin/pro/main/UT0/files/terminalrc
