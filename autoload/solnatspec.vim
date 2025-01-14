" Insert NatSpec comments on Solidity contracts
" Inspired by heavenshell/vim-pydocstring
" Author:       Felipe Buiras
" WebPage:      http://github.com/fmorisan/vim-solnatspec
" Description:  Generate NatSpec comments for your Solidity files.
" License:      BSD, see LICENSE for more details

let s:save_cpo = &cpo
set cpo&vim

let g:solc_path = get(
  \ g:,
  \ 'solc_path',
  \ 'solc'
  \ )
let g:natspecgen_path = get(
  \ g:,
  \ 'natspecgen_path',
  \ printf('%s/lib/natspecgen.py', expand('<sfile>:p:h:h'))
  \ )

" Magic starts here. Calling solc --ast-json...
function! s:create_cmd(file, lineno, indent) abort
    let cmd = printf(
        \ '%s %s %d --indent %d',
        \ expand(g:natspecgen_path),
        \ expand(a:file),
        \ a:lineno,
        \ a:indent,
        \ )
    return cmd
endfunction

function! solnatspec#checkdeps(...) abort
    if !executable(g:solc_path)
        throw 'solc not found in path'
    elseif !executable(g:natspecgen_path)
        throw 'natspecgen python script not found'
    endif
endfunction

function! solnatspec#insert(...) abort
  try
      call solnatspec#checkdeps()
      let line = line('.')
      let linedata = getline('.')
      let indent = matchstr(linedata, '^\(\s*\)')

      let symbol = expand('<cword>')

      let cmd = s:create_cmd(expand('%'), line, len(indent))

      echo cmd
      exec 'r!' . expand(cmd)

      let g:solnatspec_lastcmd = cmd
  catch
      echoerr v:exception
  endtry

endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
