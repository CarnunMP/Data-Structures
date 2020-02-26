# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.count = 1

    # Insert the given value into the tree
    def insert(self, value):
        # if no root, make root, STOP
        if self.value == None:
            self.value = value
        # else, compare to root
        else:
            # if smaller than root, check left
            if value < self.value:
                # if left equals None, insert at left, STOP
                if self.left == None:
                    self.left = BinarySearchTree(value)
                # else, recurse left
                else:
                    self.left.insert(value)
            # elif greater than or equal to root, check right
            elif value >= self.value:
                # if right equals NONE, insert at right, STOP
                if self.right == None:
                    self.right = BinarySearchTree(value)
                # else, recurse right
                else:
                    self.right.insert(value)
            # elif equal to root, increment count of root, STOP
            # else:
            #     self.count += 1

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if root equals target
        if self.value == target:
            # return True
            return True
        
        # else if neither left nor right exist, return False
        if self.left == None and self.right == None:
            return False

        # elif target < root and root.left exists, recurse left
        if target < self.value:
            return self.left.contains(target)
        # elif target > root and root.right exists, recurse left

        if target > self.value:
            return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # loop until right equals none
        current = self
        while current.right != None:
           current = current.right

        # return last value
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # If node isn't None
        if self != None:
            # call bd on node
            cb(self.value)
            # recurse left if left
            if self.left != None:
                self.left.for_each(cb)
            # recurse right if right
            if self.right != None:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
