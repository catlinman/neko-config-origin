set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
Plugin 'bling/vim-airline'
Plugin 'Lokaltog/powerline-fonts' "requires the powerline fonts to be installed and activated
Plugin 'Lokaltog/vim-easymotion'
Plugin 'kien/ctrlp.vim'
Plugin 'terryma/vim-multiple-cursors'

if has("python")
  Plugin 'severin-lemaignan/vim-minimap'
  Plugin 'valloric/YouCompleteMe' "requires running ../install.sh
  Plugin 'Valloric/MatchTagAlways'
endif

" plugin from http://vim-scripts.org/vim/scripts.html
"Plugin 'L9'
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Avoid a name conflict with L9
"Plugin 'user/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" Allow saving of files as sudo when I forgot to start vim using sudo.
cmap w!! w !sudo tee > /dev/null %

inoremap jk <ESC> 
inoremap kj <ESC>

map <F11> <Esc>:call libcallnr("gvimfullscreen.dll", "ToggleFullScreen", 0)<CR>y

set tabstop=4
set noexpandtab
set shiftwidth=4
set autoindent
set softtabstop=4

set background=dark
set number
set t_Co=256
set laststatus=2
set ttimeoutlen=50
set encoding=utf-8

set guioptions-=m  "remove menu bar
set guioptions-=T  "remove toolbar
set guioptions-=r  "remove right-hand scroll bar
set guioptions-=L  "remove left-hand scroll bar

set background=dark

syntax on
filetype indent plugin on

let g:mta_filetypes = {
    \ 'html' : 1,
    \ 'xhtml' : 1,
    \ 'xml' : 1,
    \ 'jinja' : 1,
    \ 'php' : 1,
    \}

highlight Pmenu ctermfg=blue ctermbg=black

let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline_theme = "wombat"

if has('gui_running')
  set guioptions-=T  " no toolbar

  if has('gui_win32')
    set guifont=Inconsolata_for_Powerline:h9:cANSI
  else
    set guifont=Inconsolata\ for\ Powerline\ 9
  endif
endif

if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif
let g:airline_symbols.space = "\ua0"

colorscheme vineko