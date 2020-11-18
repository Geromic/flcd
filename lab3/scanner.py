import sys
import re

from lab2.hashTable import HashTable
from lab4.FAParser import FiniteAutomata

faInt = FiniteAutomata('../resources/automatas/int.in')
faString = FiniteAutomata('../resources/automatas/string.in')
faChar = FiniteAutomata('../resources/automatas/char.in')
faFloat = FiniteAutomata('../resources/automatas/float.in')
faBool = FiniteAutomata('../resources/automatas/bool.in')

assert faChar.check_sequence(["'", "a", "'"]) is True


def is_int(_token):
    return faInt.check_sequence(list(_token))


def is_float(_token):
    return faFloat.check_sequence(list(_token))


def is_char(_token):
    print(list(_token))
    return faChar.check_sequence(list(_token))


def is_string(_token):
    return faString.check_sequence(list(_token))


def is_bool(_token):
    return faBool.check_sequence([_token])


def is_valid_const(_token):
    return is_int(_token) or is_float(_token) or is_char(_token) or is_string(_token) or is_bool(_token)


def is_valid_identifier(_token):
    return re.match("^[0-9A-Z\"']", _token) is None


string_match = "[a-zA-Z0-9 !@#$%^&*()_-{}\\\[\]]"

reserved = ['int', 'float', 'char', 'string', 'if', 'else', 'while', 'read', 'readInt', 'print', 'println', 'return']
ops = ['+', '-', '*', '/', '%', '&&', '||', '==', '!=', '=', '<=', '>=', '<', '>',
       '[', ']', '{', '}', '(', ')', ':', ';',
       ]
special_chars = " =<>:;!@#$%^&*()_-{}[]/\\'\""


def split_line(_line):
    ops_delimiters = '|'.join(map(re.escape, ops))

    return re.split('(' + ops_delimiters + '|^"' + string_match +
                    '*"$' + "|^'" + string_match + "*'$" + '|[^"\'a-zA-Z0-9.]' + ')', _line)


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
                raise Exception("Lexical error on line {}; Invalid token {}".format(lineNr, token))

        line = file.readline()
        lineNr += 1

    print("\n" + str(st))
    print(str(pif) + "\n")
    print("Valid")
