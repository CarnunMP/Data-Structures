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
        # if there is a left subtree, traverse it (recurse)
        if node.left != None:
            self.in_order_print(node.left)
        # print the root
        print(node.value)
        # if there's a right subtree, print it (recurse)
        if node.right != None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # keep track of nodes visited (list) and nodes to_visit (queue)
        visited = []
        to_visit = Queue()

        # add node to to_visit
        to_visit.enqueue(node)
        # for each child node in to_visit (loop until to_visit is empty)
        while to_visit.len() > 0:
            # print it
            visited_node = to_visit.dequeue()
            print(visited_node.value)
            # append it to visited
            visited.append(visited_node)
            # add its chidren (!= None) to to_visit
            to_visit.enqueue(visited_node.left) if visited_node.left != None else None
            to_visit.enqueue(visited_node.right) if visited_node.right != None else None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # if none != None
            # instantiate to_visit stack and a visited array/list
            # to_visit = Stack()
            # visited = []
            # # add node to to_visit
            # to_visit.push(node)

            # # while to_visit is non-empty
            # while to_visit.len() > 0:
            #     # look at the top node in the stack
            #     top_node = to_visit.pop()
            #     to_visit.push(top_node)

            #     # if it has a left child which hasn't been visited, add its left child to the stack
            #     if top_node.left != None and not top_node.left in visited:
            #         to_visit.push(top_node.left)
            #     # else, if it has an unvisited right child, pop it, append it to visited, and add its right child to the stack
            #     elif top_node.right != None and not top_node.right in visited:
            #         visited.append(to_visit.pop())
            #         to_visit.push(top_node.right)
            #     # else, pop it and append it to visited
            #     else:
            #         visited.append(to_visit.pop())

            # for node in visited:
            #     print(node.value)

        # Oops! First pass prints in order. Needing 'visited' set off alarm bells, but they were a little quiet, ha. V2:

        # if node != None:
        if node != None:
            # instantiate a to_visit stack
            to_visit = Stack()
            # push node to it
            to_visit.push(node)

            # while to_visit is non-empty
            while to_visit.len() > 0:
                # pop top node from stack
                top_node = to_visit.pop()
                # print it
                print(top_node.value)

                # if it has a left, add it to to_visit
                to_visit.push(top_node.left) if top_node.left != None else None
                # if it has a right, add it to to_visit
                to_visit.push(top_node.right) if top_node.right != None else None


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
