#from lab2.hashTable import HashTable
import sys
import re


def is_const(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


def is_identifier(token):
    pass
    # TODO


reserved = ['int', 'float', 'char', 'string', 'if', 'else', 'while', 'read', 'readInt', 'write', 'writeln']
ops = ['+', '-', '*', '/', '%', '&&', '||', '=', '==', '!=', '<', '>', '<=', '>=',
       '[', ']', '{', '}', '(', ')', ':', ':',
       ]

#st = HashTable()

if len(sys.argv) != 2:
    raise Exception("Wrong parameter count")

filename = sys.argv[1]

with open(filename) as file:
    lineNr = 1
    line = file.readline()
    while line:
        split = re.split('([^"\'a-zA-Z0-9])', line)
        split = list(filter(lambda x: x is not None and x != '', map(lambda x: x.strip(), split)))
        print(split)

        line = file.readline()
        lineNr += 1

