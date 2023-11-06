# vim-solidity-natspecador

tiennes odio por escritar natspec?

eres un sabio, un usuario de vim o neovim?

## 
- `solc`  - en el path. queda puto solcjs - https://github.com/crytic/solc-select es una regalito del dios
- `python3 >= 3.6`

## instalación

usuarios de vim-plug:

```vim
Plug 'cmark0v/vim-solidity-natspecador'
```

## usando

mueve el puntero hasta una lina antes la delaración del función entonces haga `:SolNatSpec`

#######################################

This is forked from https://github.com/fmorisan/vim-solnatspec. It was broken in one or two placies due to changes in solc and maybe vim quirks. the name is better in spanish

The code is compiled and the json artifacts are used to pull the function signatures and other information to create a natspec template for the function, which you then fill in with your descriptions

how to use:
  - save file buffer to disk. it has to be compiled and is done from the file path at the moment. 
  - put cursor one line above function you want to generate natspec template for
  - ``:SolNatSpec`` command
  - fill in your comments

config
------

 - ``BQUOTE`` - boolean, select block quote or line by line quote style for natspec, loaded from dotenv so can use ``.env`` file or over-ride with shell env


improvements would be: 
- output somesort of feedback when it doesnt have anything to output due to line mismatch or otherwise
- autoselect appropriate solc version using solc-selector and parseing the header pragma on the solidity file, not too hard
- make it work on a selected range in visual mode
- maybe generate the output for the closest function definition to cursor
- read the buffer thats being edited. it reads from disk now. the file also must compile
