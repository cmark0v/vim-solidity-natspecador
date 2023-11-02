# vim-solidity-natspecador

tiennes odio por escritar natspec?

eres un sabio, un usuario de vim o neovim?

## 
- `solc`  - en el path. queda puto solcjs - https://github.com/crytic/solc-select es una regalito del dios
- `python3 >= 3.6`

## instalación

usuarios de vim-plug:

```vim
Plug 'cmark0v/vim-solidity-natspecador
```

## usando

mueve el puntero hasta una lina antes la delaración del función entonces haga `:SolNatSpec`

#######################################

This is forked from https://github.com/fmorisan/vim-solnatspec. It was broken in one or two places due to changes in solc and maybe vim quirks. the name is better in spanish

how to use:
  - save file buffer to disk
  - put cursor line above function you want to generate natspec template for
  - ``:SolNatSpec`` command
  - fill in your comments

config
------

 - ``BQUOTE`` - boolean, select block quote or line by line quote style for natspec, loaded from dotenv so can use ``.env`` file or over-ride with shell env


improvements would be: 
- output somesort of feedback when it doesnt have anything to output
- autoselect appropriate solc version using solc-selector and parseing the header pragma on the solidity file, not too hard
- make it work on a selected range in visual mode
- maybe generate the output for the closest function definition to cursor
- read the buffer thats being edited. it reads from disk now. the file also must compile
