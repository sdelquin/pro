"Minimalist Vim Plugin Manager - https://github.com/junegunn/vim-plug
"After adding a new plugin, type :so % to reload this file and run :PlugInstall
"To uninstall a plugin: comment/delete plugin line, type :so % and run :PlugClean
call plug#begin()
    Plug 'vim-airline/vim-airline'
    Plug 'kien/ctrlp'
call plug#end()

syntax on
set ts=4
set sw=4
set expandtab
set ai
