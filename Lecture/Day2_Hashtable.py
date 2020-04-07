class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'<{self.key}, {self.value}>'

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # return hash(key)
        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 7919
        for i in key:
            # Use ord() to convert str(i) to int(i)
            hash_value = ((hash_value << 5) + hash_value) + ord(i)
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # Hashmod the key to find the bucket
        index = self._hash_mod(key)

        # Check if a pair already exists in the bucket
        pair = self.storage[index]
        if pair:
            # If so, overwrite the key/value and throw a warning
            if pair.key != key:
                print("Warning: Overwriting value")
                pair.key = key
            pair.value = value
        else:
            # If not, create a new LinkewPair and pace it in the bucket
            self.storage[index]

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Get index from hashmod
        index = self._hash_mod[key]
        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] and self.storage[index].key == key:
            # If so, remove that pair
            self.storage[index] = None
        # Else, print warning
        else:
            print('Warning: Key does not exist')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get index from hashmod
        index = self._hash_mod[key]
        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] and self.storage[index].key == key:
            # If so, return the value
            return self.storage[index].value
        # Else, return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        new_storage = [None] * self.capacity
        self.storage = new_storage

        for i in old_storage:
            while i:
                self.insert(i.key, i.value)
                i = i.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    print(ht.remove('line_5'))
