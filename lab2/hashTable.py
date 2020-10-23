class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    '''
    Open addressing hash table
    '''

    def __init__(self, start_size=50):
        self.__size = start_size
        self.__length = 0
        self.__table = [None] * start_size

    '''
    input: key - integer, pair key;
    output: value associated to the key, it the key exists in the table
            None otherwise
    '''
    def __getitem__(self, key):
        hash_key = self.__hash(key)
        if self.__table[hash_key] is None:
            return None
        return self.__table[self.__hash(key)].value

    '''
    input:  key - integer, pair key;
            value - value associated to the given key;
    output: nothing
    If there is a collision while adding the (key, value) pair a resize is performed
    '''
    def __setitem__(self, key, value):
        hash_key = self.__hash(key)
        while self.__table[hash_key] is not None:
            self.__resize()
            hash_key = self.__hash(key)
        self.__table[hash_key] = Pair(key, value)
        self.__length += 1

    '''
    input:  key - integer, pair key;
    output: hashed_key - integer, an index in the table;
    '''
    def __hash(self, key) -> int:
        hash_sum = 0
        for pos, char in enumerate(key):
            hash_sum += (pos + 1) * ord(char)
        return hash_sum % self.__size

    '''
    Resize function in case there is a collision
    '''
    def __resize(self):
        self.__size *= 2
        newTable = [None] * self.__size
        for pair in self.__table:
            if pair is not None:
                hash_key = self.__hash(pair.key)
                if self.__table[hash_key] is not None:
                    self.__resize()
                newTable[hash_key] = Pair(pair.key, pair.value)
        self.__table = newTable

    '''
    getter function for the length of the table
    '''
    def __len__(self):
        return self.__length
