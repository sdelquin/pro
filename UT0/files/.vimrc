"Minimalist Vim Plugin Manager - https://github.com/junegunn/vim-plug
"After adding a new plugin, type :so % to reload this file and run :PlugInstall
"To uninstall a plugin: comment/delete plugin line, type :so % and run :PlugClean
call plug#begin()
  Plug 'vim-airline/vim-airline'
  Plug 'kien/ctrlp.vim'
  Plug 'morhetz/gruvbox'
call plug#end()

colorscheme gruvbox

syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set ignorecase
set cursorline
set number
set background=dark

nnoremap dl :t.<CR>
