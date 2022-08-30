#!/usr/bin/env python3
import __main__
import sys
import json
import argparse
import subprocess

ap = argparse.ArgumentParser("natgenspec.py")
ap.add_argument("file", help="File to parse with solc.")
ap.add_argument("line", help="Line number of definition", type=int)
ap.add_argument("-i", "--indent", default=0, help="Indentation level in space count.", type=int)

args = ap.parse_args()

solc_out = subprocess.check_output(['solc', '--ast-compact-json', args.file]).decode('utf8')
solc_split = solc_out.split('\n')

author_name = subprocess.check_output([
    'git',
    'config',
    'user.name'
]).decode('utf8').strip()
author_email = subprocess.check_output([
    'git',
    'config',
    'user.email'
]).decode('utf8').strip()

linebreak_byte_numbers = []
with open(args.file, 'r') as f:
    for i, b in enumerate(f.read()):
        if b == '\n':
            linebreak_byte_numbers.append(i)

start = None
end = None

for i, line in enumerate(solc_split):
    if start is not None:
        if '====' in line:
            end = i
            break
    if '====' in line and args.file in line:
        start = i

ast_json = json.loads(
    "\n".join(solc_split[start+1:end])
)
params = []
returnz = []
def line_dfs(node):
    # solc AST doesnt give us line numbers LMAO
    byte_pos = int(node.get('src').split(':')[0])
    # hacker moment
    line_nr = min(line for (line, byte) in enumerate(linebreak_byte_numbers) if byte >= byte_pos)
    if line_nr == args.line and node.get('nodeType') in ['ContractDefinition', 'FunctionDefinition']:
        __main__.params = __main__.params + getnames(node.get('parameters',{}).get('parameters'))
        __main__.returnz = __main__.returnz +  getnames(node.get('returnParameters',{}).get('parameters'))
    else:
        nodes = node.get('nodes')
        if not nodes:
            return None
        else:
            for child in nodes:
                success = line_dfs(child)
                if success:
                    return success

def getnames(bob):
    out = []
    if type(bob) is list:
        for b in bob:
            out.append(b)
    return out

def print_indented(string):
    print(' '*int(args.indent) + string)

if args.line:
    symbol_node = line_dfs(ast_json)
#else:
#    symbol_node = dfs(ast_json)



#    print_indented(
#        f"/// @author {author_nodeType} ({author_email})"
#    )
#    print_indented(
#        f"/// @title {symbol_node['attributes']['nodeType']}"
#    )
print_indented(f"/// @notice")
print_indented(f"/// @dev")
for param in params:
    print_indented(f"/// @param {param['name']} {param['typeName']['name']}")
for param in returnz:
    print_indented(f"/// @return {param['name']} {param['typeName']['name']}")

