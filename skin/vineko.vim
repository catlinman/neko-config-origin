
" Vim color file vineko
" Created by Catlinman (catlinman.com)

set background=dark
hi clear
if exists("syntax_on")
	syntax reset
endif

set t_Co=256
let colors_name = "vineko"

hi Comment	    guifg=#878787    ctermfg=103   gui=italic     cterm=italic
hi Constant	    guifg=#ffec70    ctermfg=226   gui=none       cterm=none
hi Cursor	    guibg=#f0e68c    ctermbg=255   guifg=#708090  ctermfg=242      gui=none    cterm=none
hi CursorLine	guifg=#ffffff    ctermfg=231   guibg=#404040  ctermbg=237      gui=none    cterm=none
hi ColorColumn	guifg=#ffffff    ctermfg=231   guibg=#cc4040  ctermbg=252      gui=none    cterm=none
hi Directory	guifg=#008b8b    ctermfg=33    gui=none       cterm=none
hi Folded	    guibg=#555555    ctermbg=239   guifg=#ffd700  ctermfg=220      gui=none    cterm=none
hi Function	    guifg=#ff4564    ctermfg=202   gui=none       cterm=none
hi Identifier	guifg=#5cc6ff    ctermfg=52    gui=none       cterm=none
hi LineNr	    guifg=#ffb94a    ctermfg=225   gui=none       cterm=none
hi MatchParen	guifg=#ccffcc    ctermfg=252   guibg=#008b8b  ctermbg=33       gui=none    cterm=none
hi Normal	    guifg=#ffffff    ctermfg=231   guibg=#1a1a1a  ctermbg=234      gui=none    cterm=none
hi NonText	    guibg=#1a1a1a    ctermbg=234   guifg=#81bed6  ctermfg=89       gui=none    cterm=none
hi Number	    guifg=#5cc6ff    ctermfg=226   gui=none       cterm=none
hi PreProc	    guifg=#ffb94a    ctermfg=202   gui=none       cterm=none
hi Statement	guifg=#ff4564    ctermfg=202   gui=none       cterm=none
hi Special	    guifg=#fffefc    ctermfg=226   gui=none       cterm=none
hi SpecialKey	guifg=#9acd32    ctermfg=247   gui=none       cterm=none
hi StatusLine	guibg=#c2bfa5    ctermbg=07    guifg=#000000  ctermfg=231      gui=none    cterm=none
hi StatusLineNC	guibg=#c2bfa5    ctermbg=07    guifg=#777777  ctermfg=231      gui=none    cterm=none
hi String	    guifg=#b2ff7f    ctermfg=249   gui=none       cterm=none
hi StorageClass	guifg=#ff4cff    ctermfg=202   gui=none       cterm=none
hi Title	    guifg=#cd5c5c    ctermfg=252   gui=bold       cterm=bold
hi Todo	        guifg=#fffefc    ctermfg=226   gui=none       cterm=none
hi Type	        guifg=#5cc6ff    ctermfg=52    gui=none       cterm=none
hi Underlined	guifg=#80a0ff    ctermfg=89    gui=underline  cterm=underline
hi VertSplit	guibg=#c2bfa5    ctermbg=07    guifg=#777777  ctermfg=231      gui=none    cterm=none
hi Visual       gui=none guibg=#666666
