class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.compare_insert(new_val, self.root)
    
    def compare_insert(self, new_val, start):

        if new_val < start.value:
            if start.left:
                self.compare_insert(new_val, start.left)
            else:
                start.left = Node(new_val)
        else:
            if start.right:
                self.compare_insert(new_val, start.right)
            else:
                start.right = Node(new_val)
                
    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
        
    
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.preorder_search(start.right, find_val)
            else:
                return self.preorder_search(start.left, find_val)
        else:
            return False

    def print_tree(self):
        traversal = ""
        return self.preorder_print(self.root, traversal)

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            
        return traversal
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print tree.print_tree()
# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)