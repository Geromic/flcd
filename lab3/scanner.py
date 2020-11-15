import sys
import re

from lab2.hashTable import HashTable
from lab4.FAParser import FiniteAutomata


def is_int(_token):
    return faInt.check_sequence(_token)
    '''try:
        int(_token)
        if _token[0] == '0' and len(_token) > 1 or _token in ['+0', '-0']:
            return False
        return True
    except ValueError:
        return False'''


def is_float(_token):
    aux = list(_token.split('.'))
    return is_int(aux[0]) and re.match('^[0-9]+$', aux[1]) is not None


string_match = "[a-zA-Z0-9 !@#$%^&*()_-{}\\\[\]]"


def is_char(_token):
    return re.match("^'" + string_match + "'$", _token) is not None


def is_string(_token):
    return re.match('^"' + string_match + '*"$', _token) is not None


def is_bool(_token):
    return _token in ['True', 'False']


def is_valid_const(_token):
    return is_int(_token) or is_float(_token) or is_char(_token) or is_string(_token) or is_bool(_token)


def is_valid_identifier(_token):
    return re.match("^[0-9A-Z\"']", _token) is None


reserved = ['int', 'float', 'char', 'string', 'if', 'else', 'while', 'read', 'readInt', 'print', 'println', 'return']
ops = ['+', '-', '*', '/', '%', '&&', '||', '==', '!=', '=', '<=', '>=', '<', '>',
       '[', ']', '{', '}', '(', ')', ':', ';',
       ]
special_chars = " =<>:;!@#$%^&*()_-{}[]/\\'\""


def split_line(_line):
    ops_delimiters = '|'.join(map(re.escape, ops))

    return re.split('(' + ops_delimiters + '|^"' + string_match +
                    '*"$' + "|^'" + string_match + "*'$" + '|[^"\'a-zA-Z0-9.]' + ')', _line)


faInt = FiniteAutomata('int.in')
faString = FiniteAutomata('string.in')
faChar = FiniteAutomata('char.in')
faFloat = FiniteAutomata('float.in')
faBool = FiniteAutomata('bool.in')

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
            elif is_valid_const(token) or is_valid_identifier(token):
                index = st.add(token)
                pif[token] = index
            else:
                raise Exception("Lexical error on line {}; Invalid token '{}'".format(lineNr, token))

        line = file.readline()
        lineNr += 1

    print("\n" + str(st))
    print(str(pif) + "\n")
    print("Valid")
