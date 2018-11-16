"去掉vi的一致性"
set nocompatible
"显示行号"
set number
" 隐藏滚动条"    
set guioptions-=r
set guioptions-=L
set guioptions-=b
"隐藏顶部标签栏"
set showtabline=0
"设置字体"         
syntax on   "开启语法高亮"
set nowrap  "设置不折行"
set fileformat=unix "设置以unix的格式保存文件"
set cindent     "设置C样式的缩进格式"
set tabstop=4   "设置table长度"
set shiftwidth=4        "同上"
set showmatch   "显示匹配的括号"
set scrolloff=5     "距离顶部和底部5行"
set laststatus=2    "命令行为两行"
set fenc=utf-8      "文件编码"
set backspace=2
set mouse=a     "启用鼠标"
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set ignorecase      "忽略大小写"
set incsearch
set hlsearch        "高亮搜索项"
set noexpandtab     "不允许扩展table"
set whichwrap+=<,>,h,l
set autoread
set cursorline      "突出显示当前行"
set cursorcolumn        "突出显示当前列"

filetype off 
set rtp+=~/.vim/bundle/Vundle.vim 
call vundle#begin() 
Plugin 'VundleVim/Vundle.vim' 
Plugin 'Lokaltog/vim-powerline'
Plugin 'vim-scripts/indentpython.vim.git'
Plugin 'vim-scripts/Solarized.git'
Plugin 'scrooloose/nerdtree'
Plugin 'jiangmiao/auto-pairs' 
Plugin 'morhetz/gruvbox'
Plugin 'Yggdroot/indentLine'
call vundle#end() 
filetype plugin indent on

"settings of Gruvbox"
set bg=dark                     "设置背景为黑色
colorscheme gruvbox             "设置主题为 gruvbox
set guifont=Monaco:h17          "设置字体和字的大小

" Powerline 设置"
" 设置状态栏主题风格"
let g:Powerline_colorscheme='solarized256'

" settings of Nerdtre"e
"F2开启和关闭树" 
map <F2> :NERDTreeToggle<CR> 
let NERDTreeChDirMode=1 "显示书签" 
let NERDTreeShowBookmarks=1 "设置忽略文件类型" 
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$'] "窗口大小" 
let NERDTreeWinSize=25


"settings of auto-pairs"
let mapleader=','

"settings of indentline"
"缩进指示线"
let g:indentLine_char='┆'
let g:indentLine_enabled = 1
