"Minimalist Vim Plugin Manager - https://github.com/junegunn/vim-plug
"After adding a new plugin, type :so % to reload this file and run :PlugInstall
"To uninstall a plugin: comment/delete plugin line, type :so % and run :PlugClean
call plug#begin()
  Plug 'vim-airline/vim-airline'
  Plug 'kien/ctrlp.vim'
  Plug 'NLKNguyen/papercolor-theme'
call plug#end()

"https://vimcolorschemes.com/
colorscheme PaperColor

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

" Settings per filetype
autocmd Filetype html setlocal ts=2 sw=2
autocmd Filetype css setlocal ts=2 sw=2
autocmd Filetype javascript setlocal ts=2 sw=2
autocmd Filetype json setlocal ts=2 sw=2
