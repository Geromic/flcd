import sys
import re

from lab2.hashTable import HashTable


def is_const(_token):
    try:
        int(_token)
        return True
    except ValueError:
        # TODO: add case for char and float :D
        return re.match('^"[a-zA-Z0-9]+"$', _token) is not None


def is_valid_identifier(_token):
    return re.match("^[0-9\"']", _token) is None


reserved = ['int', 'float', 'char', 'string', 'if', 'else', 'while', 'read', 'readInt', 'write', 'writeln']
ops = ['+', '-', '*', '/', '%', '&&', '||', '==', '!=', '=', '<=', '>=', '<', '>',
       '[', ']', '{', '}', '(', ')', ':', ';',
       ]


def split_line(_line):
    ops_delimiters = '|'.join(map(re.escape, ops))
    return re.split('(' + ops_delimiters + '|[^"\'a-zA-Z0-9]' + ')', _line)


st = HashTable()
pif = {}

if len(sys.argv) != 2:
    raise Exception("Wrong parameter count")

filename = sys.argv[1]

with open(filename) as file:
    lineNr = 1
    line = file.readline()
    while line:
        tokenized_line = split_line(line)
        tokenized_line = list(filter(lambda x: x is not None and x != '', map(lambda x: x.strip(), tokenized_line)))
        print(tokenized_line)

        for token in tokenized_line:
            if token in reserved or token in ops:
                pif[token] = -1
            elif is_const(token) or is_valid_identifier(token):
                index = st.add(token)
                pif[token] = index
            else:
                raise Exception("Lexical error on line {}; Invalid token '{}'".format(lineNr, token))

        line = file.readline()
        lineNr += 1

    print("\n" + str(st))
    print(str(pif) + "\n")
    print("Valid")
