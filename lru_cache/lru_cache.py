from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.dll = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if self.length > 0 and key in self.dict.keys():
            self.dll.move_to_end(self.getNodeByKey(key))
            return self.dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # print("set: ", key, value)
        if key in self.dict.keys():
            self.dll.delete(self.getNodeByKey(key))
            self.dict[key] = value
            self.dll.add_to_tail((key, value))
            return
        
        if self.length == self.limit:
            oldest_entry = self.dll.remove_from_head()
            self.dict.pop(oldest_entry[0])
            self.length -= 1
        
        new_node = (key, value)
        self.dll.add_to_tail(new_node)
        self.dict[key] = value
        self.length += 1

    # helper
    def getNodeByKey(self, key):
        current_node = self.dll.head
        node = None
        while node == None:
            if current_node.value == (key, self.dict[key]):
                node = current_node
            else:
                current_node = current_node.next

        return node
