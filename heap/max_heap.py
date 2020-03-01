# - Binary tree structure of a heap ican be stored in an array by letting the left and right child of each node n
#   be at indices 2n + 1 and 2n + 2 respectively.
# - If either index is out of range, there is no child node.
# - Max heap property says: a parent node must be greater than or equal to its children.


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # add value to the end of the array
        self.storage.append(value)
        # check that it's smaller than its parent
        inserted_node_index = len(self.storage) - 1
        parent_node_index = self.get_parent_index(inserted_node_index)
        # swapping = True
        while self.storage[inserted_node_index] > self.storage[parent_node_index] and parent_node_index >= 0:
        #     swapping: 
        # if not, swap them, and check again
            temp = self.storage[parent_node_index]
            self.storage[parent_node_index] = self.storage[inserted_node_index]
            self.storage[inserted_node_index] = temp
            # swapping = self._bubble_up(inserted_node_index)

            inserted_node_index = parent_node_index
            #                     self.get_parent_index(inserted_node_index)
            parent_node_index = self.get_parent_index(inserted_node_index)

        # if it is, stop
        # (Call bubble_up, for test...?)
        self._bubble_up(0)

    def delete(self):
        # swap first element with last
        first = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage[len(self.storage) - 1] = first

        # remove last element
        self.storage = self.storage[:-1]

        # check that new first element is larger than both its children
        # if it's not, swap it with the larger child
        # now check it against its children, and so on...
        index_to_check = 0
        # child_indices = self.get_child_indices(index_to_check)
        while index_to_check != None:
        # (child_indices[0] < len(self.storage) and child_indices[1] < len(self.storage)) and \
            #   (self.storage[index_to_check] < self.storage[child_indices[0]] or 
            #   self.storage[index_to_check] < self.storage[child_indices[1]]):
            index_to_check = self._sift_down(index_to_check)
            # child_indices = self.get_child_indices(index_to_check)
        
        return first

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = self.get_parent_index(index)

        if parent_index < 0:
            return

        if self.storage[parent_index] < self.storage[index]:
            temp = self.storage[parent_index]
            self.storage[parent_index] = self.storage[index]
            self.storage[index] = temp
            return True
        
        return False

    def _sift_down(self, index):
        child_indices = self.get_child_indices(index)
        if child_indices[0] >= len(self.storage) and child_indices[1] >= len(self.storage):
            return
        
        max_child_index = None
        if child_indices[1] >= len(self.storage):
            max_child_index = child_indices[0]
        else:
            max_child_index = child_indices[0] if self.storage[child_indices[0]] >= self.storage[child_indices[1]] else child_indices[1]
        
        self._bubble_up(max_child_index)

        return max_child_index

    # helpers
    def get_parent_index(self, index):
        return (index - 1) // 2 if index % 2 == 1 else (index - 2) // 2
    
    def get_child_indices(self, index):
        return (2*index + 1, 2*index + 2)
