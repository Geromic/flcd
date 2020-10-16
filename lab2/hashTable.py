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

    # getter
    def __getitem__(self, key):
        hash_key = self.__hash(key)
        if self.__table[hash_key] is None:
            return None
        return self.__table[self.__hash(key)].value

    # setter
    def __setitem__(self, key, value):
        hash_key = self.__hash(key)
        while self.__table[hash_key] is not None:
            self.__resize()
            hash_key = self.__hash(key)
        self.__table[hash_key] = Pair(key, value)
        self.__length += 1

    # hash function
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

    # length getter
    def __len__(self):
        return self.__length
