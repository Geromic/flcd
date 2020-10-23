from lab2.hashTable import HashTable

if __name__ == "__main__":
    symbolTable = HashTable()

    symbolTable['a'] = 800
    symbolTable['b'] = 90000
    symbolTable['someVariable'] = 1980

    assert symbolTable['a'] == 800
    assert symbolTable['b'] == 90000
    assert symbolTable['aaaa'] is None
    assert symbolTable['someVariable'] == 1980
    assert len(symbolTable) == 3
