# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        key = self.key
        value = self.value
        return "A tuple of {}, {}".format(key, value)

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
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Check if there is an item or linked Pair already there
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            # We need to traverse the LinkedPair to check if the key already exists

            curr = self.storage[index]
            while curr is not None: 
                # If so, check if the key is identical 
                if key == curr.key:
                    # If so, overwrite the values
                    curr.value = value

                curr = curr.next
            
            # else add to the head
            new_entry = LinkedPair(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry

        # If not, make one and insert the value at the head
        else: 
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # Check if the item exists
        if self.storage[index] is not None:
            
            head = self.storage[index]

            if head.next is None: 
                # We are at the head and can therefore just remove it
                self.storage[index] = None
            else: 
                # We are in a linkedlist and need to traverse 
                # first check the head of the list
                if head.key == key:
                    self.storage[index] = head.next

                else: 
                    prev = head
                    current = prev.next

                    while current is not None: 
                        # check for the right key 
                        if key == current.key:
                            # If so, replace with None
                            prev.next = current.next

                        current = current.next
                
        # if item doesn't exists return None
        else: 
            return None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Check if there is an item or linked Pair already there
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            # We need to traverse the LinkedPair to check if the key already exists

            curr = self.storage[index]
            while curr is not None: 
                # If so, check if the key is identical 
                if key == curr.key:
                    # If so, overwrite the values
                    return curr.value
                
                curr = curr.next
            
            return None

        # If not, make one and insert the value at the head
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
        self.storage = [None] * self.capacity

        for node in old_storage:
            if node:
                curr = node
                while curr:
                    self.insert(curr.key, curr.value)
                    curr = curr.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    for item in ht.storage: 
        print(item)
    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
