from random import randint

def is_prime(n):
    """
    Determine if the number is Prime.
    """
    # Number must be greater than 1.
    if n <= 1:
        return False
    # 2 and 3 are both Primes.
    if n <= 3:
        return True
    
    # Multiples of 2 and 3 are composite thus not Prime.
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    # Check the remaining multiples
    for i in range(5, int((n**0.5) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        
    # If none of the above cases proc, the number is Prime.
    return True

def next_prime(n):
    """
    Get the next prime number from n.
    """
    # Base case is n = 1
    if n == 1:
        return 2
    
    prime = n
    found = False
    while found == False:
        # Check the next number in sequence
        prime = prime + 1 
        # Is it a prime?
        if is_prime(prime) == True:
            found = True
    
    return prime

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity

        # create the array with dynamic shape
        self._m = [None] * self.capacity
        
        # prime number for hash
        self._p = next_prime(len(self._m)+1)
        
        # generate two random integers for hash
        self._a = randint(1, 100)
        self._b = randint(1, 100)
        
        return None

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self._m) 

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Calculate the number of items in the hash table
        n = self.get_num_slots()
        # Load factor is calculated as the number of items in a hashtable
        # divided by the number of available spaces
        return n / self.capacity

    def uni_hash(self, key):
        """
        Universal hashing.
        """
        # Strings need to be converted to numbers
        if type(key) == str:
            key = sum(ord(i) for i in key)
        
        # Universal hash function
        # ((ax + b) mod(p)) mod(m)
        # where a & b are random integers, p is a random prime >= m,
        # and m is the length of the array.
        idx = (((self._a * key) + self._b) % self._p) % len(self._m)
        return idx
        
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # I didn't use this

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # I didn't use this either

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity
        return self.uni_hash(key)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        idx = self.hash_index(key)
        # Base case slot is empty
        if self._m[idx] is None:
            # insert the node
            self._m[idx] = HashTableEntry(key, value)
        # Alternate case slot already contains an entry
        else:
            current = self._m[idx]
            # Move to last node in the chain
            while current.next is not None:
                current = current.next
            # insert the new node on next pointer
            current.next = HashTableEntry(key, value)
        return None

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        # Base case slot is empty
        if self._m[idx] is None:
            print('No such Key.')
        # Alternate case slot already contains an entry
        else:
            # set current
            current = self._m[idx]
            # there is no more entries in the linked list
            if current.next is None:
                if current.key == key:
                    current = None
                else:
                    print('No such Key.')
            # proceed to check all keys in the linked list.
            else:
                # assign previous to move pointer from old node to new node
                previous = None
                # Go down the linked list, and stop only if the key is found.
                while current.next is not None:
                    if current.key == key:
                        # there is a node between the first and current position
                        if previous is not None:
                            # move previous 'next' pointer to the next node
                            previous.next = current.next
                            # delete the current node
                            del current
                        # this is the first node in the linked list
                        else:
                            next_node = current.next
                            self._m[idx] = next_node
                        # stop on the iteration where the key was found
                        break
                    # continue iterating
                    else:
                        previous = current
                        current = current.next
                # Remove last key from linked list
                if current.key == key:
                    current = None
                else:
                    print('No such Key.')

        return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        # Nothing in that slot
        if self._m[idx] is None:
            return None
        # Set current to this node
        current = self._m[idx]
        # First node contains the key
        if current.key == key:
            return current.value
        # It doesn't contain the key
        else:
            # No more nodes
            if current.next is None:
                return None
            # Check the rest of the nodes in the linked list
            else:
                while current.next is not None:
                    current = current.next
                    if current.key == key:
                        # stop iteration on correct node
                        break
                # return the value for the last current node
                return current.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # List to hold all nodes
        temp_list = list()
        # Put all nodes into the list
        for slot in self._m:
            if slot is not None:
                temp_list.append(slot)
                if slot.next is not None:
                    current = slot.next
                    temp_list.append(current)
                    while current.next is not None:
                        temp_list.append(current.next)
                        current = current.next
        # Reshape the array
        self._m = [None] * new_capacity
        # put all nodes into new array
        for node in temp_list:
            self.put(node.key, node.value)
        # Delete temp list
        del temp_list
        return None

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
