from lab2.hashTable import HashTable

if __name__ == "__main__":
    symbolTable = HashTable()

    symbolTable['a'] = 800
    symbolTable['b'] = 90000
    symbolTable['someVariable'] = 1980

    print(symbolTable['a'])
    print(symbolTable['b'])
    print(symbolTable['aaaa'])
    print(symbolTable['someVariable'])
    print(len(symbolTable))
