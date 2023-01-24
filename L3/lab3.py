
class Node(object):
    """
    Nodes in Tree structure

    gives biulding blocks for pointer and link list that make binary tree

    Attributes
    __________
    __init__(self, data):
        gives each node a parent pointer, Left child pointer, right child pointer and the key value data

    """
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    Brinary search tree

    Attributes
    __________
    __init__(self):
    defines the root of the tree structer that all nodes will point form

    print(self):
    print the tree inorder of value

    insert(self, data):
    inserts data by rules of BST creating the structure

    min(self):
    returns the smallest value in the tree

    max(self):
    returns the largest value in the tree

    contains(self, data):
    returns true if value is in tree else returns flase

    __iter__(self):
    an iterator that iterates over the nodes inorder of value

    inorder(self):
    calls helper fuction and return an inorder list of nodes

    preorder(self):
    calls helper fuction and return a preorder list of nodes

    postorder(self):
    calls helper fuction and return a postorder list of nodes

    find_successor(self, data):
    finds the next largest node in the tree if none return None

    transplant(self,curr_node,repl_node):
    swaps values of two nodes inplace

    delete(self, data):
    deletes a node and restructures tree to preserve rules, raise error os empty. call Transplant and Find Successor to swap in place and find node to swap with.



    Helper Methods
    --------------
    __print(self, curr_node):
    helper function that rucurrivily prints subtree in order

    __find_node(self, data):
    helper fuction that if emtpy return error else return the node that contains the given value key

    __traverse(self, curr_node, traversal_type):
    helper function that prints the tree using a gfenrator to ensure oreder that is give form any ****order function call.

    """
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None


    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        # page 312-313 reworked for own while loops
        par_node = None
        new_node = Node(data)
        curr_node = self.root

        while(curr_node != None):
            par_node = curr_node
            if(new_node.data < curr_node.data):
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        new_node.parent = par_node
        #if empty
        if(par_node == None):
            self.root = new_node
        else:
            if(new_node.data < par_node.data):
                par_node.left = new_node
            else:
                par_node.right = new_node


    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        curr_node = self.root
        if(curr_node == None):
            return None
        while(curr_node.left != None):
            curr_node = curr_node.left
        return curr_node.data


    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        curr_node = self.root
        if (curr_node == None):
            return None
        while (curr_node.right != None):
            curr_node = curr_node.right
        return curr_node.data


    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        #left tree search
        curr_node =self.root
        while (curr_node != None and data != curr_node.data):
            # left tree search
            if(data < curr_node.data):
                curr_node = curr_node.left
            #right tree search
            else:
                curr_node = curr_node.right
        return curr_node


    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        temp_value = self.__find_node(data)

        if(temp_value != None):
            return True
        else:
            return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        #Yield data of the correct node
        if(traversal_type == Tree.PREORDER and curr_node != None):
            yield curr_node.data
            yield from self.__traverse(curr_node.left, traversal_type)
            yield from self.__traverse(curr_node.right, traversal_type)
        if (traversal_type == Tree.INORDER and curr_node != None):
            yield from self.__traverse(curr_node.left, traversal_type)
            yield curr_node.data
            yield from self.__traverse(curr_node.right, traversal_type)
        if (traversal_type == Tree.POSTORDER and curr_node != None):
            yield from self.__traverse(curr_node.left, traversal_type)
            yield from self.__traverse(curr_node.right, traversal_type)
            yield curr_node.data


    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    	# Return object of successor if found else return None
        #310 -312
        if(self.__find_node(data) == None):
            raise KeyError

        curr_node = self.__find_node(data)

        if(curr_node.right != None):
            curr_node = curr_node.right
            while (curr_node.left != None):
                curr_node = curr_node.left
            return curr_node
        else:
            if(curr_node.parent == None):
                return None
            else:
                lowest_node = curr_node.parent
                while(lowest_node != None and curr_node == lowest_node.right):
                    curr_node = lowest_node
                    lowest_node = lowest_node.parent
                return lowest_node


    def transplant(self,curr_node,repl_node):
        if(curr_node.parent == None):
            self.root = repl_node
        else:
            par_node = curr_node.parent
            if(curr_node == par_node.left):
                par_node.left = repl_node
            else:
                par_node.right = repl_node
        if(repl_node != None):
            repl_node.parent = curr_node.parent


    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        #pg 317 and 316
        repl_node = None

        if(self.__find_node(data) == None):
            raise KeyError

        curr_node = self.__find_node(data)

        if(curr_node.left == None):
             self.transplant(curr_node, curr_node.right)
        else:
            if(curr_node.right == None):
                self.transplant(curr_node, curr_node.left)
            else:
                succ_node = self.find_successor(curr_node.data)
                if(succ_node != curr_node.right):
                    self.transplant(succ_node, succ_node.right)
                    succ_node.right = curr_node.right
                    sr_node = succ_node.right
                    sr_node.parent = succ_node
                self.transplant(curr_node, succ_node)
                succ_node.left = curr_node.left
                sl_node = succ_node.left
                sl_node.parent = succ_node