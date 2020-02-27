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
        parent_node_index = (inserted_node_index - 1) // 2 if inserted_node_index % 2 == 1 else (inserted_node_index - 2) // 2
        while self.storage[inserted_node_index] > self.storage[parent_node_index] and parent_node_index >= 0:
        # if not, swap them, and check again
            temp = self.storage[parent_node_index]
            self.storage[parent_node_index] = self.storage[inserted_node_index]
            self.storage[inserted_node_index] = temp

            inserted_node_index = parent_node_index
            parent_node_index = (inserted_node_index - 1) // 2 if inserted_node_index % 2 == 1 else (inserted_node_index - 2) // 2
        # if it is, stop

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
