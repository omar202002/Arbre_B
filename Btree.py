from Node import *


class Btree:
    """
    Class representing a B-tree.
    """
    def __init__(self, max_key):
        self.max_key = max_key
        self.min_key = max_key//2
        self.l = (max_key//2) + 1
        self.u = max_key + 1
        self.nodes = []
        self.root = None
    
    def isBtree(self, root):
        pass

    
    def search_key(self, root, key):
        """
        Searches for a key in the tree and tells if it is present.

        Arguments:
        - root: The root of the tree.
        - key: The key to search for.

        Returns:
        - True if the key is present in the tree, False otherwise.
        """
        if root == None:
            raise ValueError("Root is None.")
        i = 0
        keys = root.getKeys()
        while i < len(keys) and key > keys[i]:
            i += 1
        if root.isLeaf():
            return i < root.getNbKeys() and key == keys[i]
        else:
            if i < root.getNbKeys() and key == keys[i]:
                return True
            else:
                return self.search_key(root.getChildren()[i], key)
    
    def linearisation(self, root):
        """
        Returns a root.getKeys() of the keys in the tree in linear order.

        Arguments:
        - root: The root of the tree.

        Returns:
        - A root.getKeys() of the keys in the tree in linear order.
        """

        
        res = []
        if root.isLeaf():
            res.extend(root.getKeys())
            return res
        else:
            for i in range(0, len( root.getKeys() )):
                res.extend(self.linearisation(root.getChildren()[i]))
                res.append(root.getKeys()[i])
            res.extend(self.linearisation(root.getChildren()[len(root.getKeys())]))
                
        return res

    def height(self, node):
        """
        Returns the height of the tree.

        Arguments:
        - node: The node from which to calculate the height.

        Returns:
        - The height of the tree.
        """
        if node is None:
            raise ValueError("Node is None.")
        
        if node.parent is None:
            return 0
        else:
            return 1 + self.height(node.parent)

    def isBalanced(self, node=None):
        """
        Checks if the tree is balanced on if all leaves are at the same level.

        Arguments:
        - node: The node from which to check balance. If no node is provided, the root of the tree is used.

        Returns:
        - True if the tree is balanced, False otherwise.
        """
        res = []

        if node is None:
            raise ValueError("Node is None.")
        
        if node.isLeaf():
            res.append(self.height(node))
            return all(x == res[0] for x in res)
        else:
            for child in node.getChildren():
                res.append(self.isBalanced(child))
            return all(x == res[0] for x in res)
        

    def find_middle(self,lst):
        if not lst:  # Check if the list is empty
            return "The list is empty."
 
        length = len(lst)  # Get the length of the list
 
        if length % 2 != 0:  # Check if the length is odd
            middle_index = length // 2
            return middle_index
 
        # If the length is even
        first_middle_index = length // 2 - 1
        return first_middle_index
    
    def split(self, node):
        res = []
        middle = self.find_middle(node.getKeys())
        node1 = Node(True, self.max_key)
        node1.setKeys(node.getKeys()[:middle])
        node2 = Node(True, self.max_key)
        node2.setKeys(node.getKeys()[middle+1:])
        return [middle, node1, node2]


    def findNodeToInsert(self,key, node = None):
        """
        Returns the node in wich the key should be inserted

        Arguments :
        - key : the key we want to insert
        - node : the node from which we are to ckeck where the key can be inserted

        Returns :
        The node in which the key will be inserted
        """
        if node == None:
            node  = self.root
    
        n = len(node.getKeys())
        index = 0

        if node.isLeaf():
            return node
        else :
            for j in range(n):
                if (node.getKeys()[j] > key):
                    index = j
                    break
                elif j == n-1:
                    index = j+1
            return self.findNodeToInsert(key, node.getChildren()[index])
        
    def insertInNode(self, key, node):
        """
        Inserts the key in the node. If the node in already full, it will be split into two nodes which contains
        each the half minus one of the node and the middle key of the node will be inserted in the parent
        """
        res = None
    
        if len(node.getKeys()) < node.getSize():
            node.addKey(key)

        else:
            """
            res = self.split(node)
            node.getParent().getChildren().append(res[1])
            node.getParent().getChildren().append(res[2])
            self.insertInNode(key, node.parent)
            """
            middle, node1, node2 = self.split(node)
            if node.getParent() is not None:
                parent = node.getParent()
                parent.getChildren().append(node1)
                parent.getChildren().append(node2)
                node1.setParent(parent)
                node2.setParent(parent)
                self.insertInNode(middle, parent)
            else:
                self.root = Node(False, self.max_key)
                self.root.setChildren([node1, node2])
                node1.setParent(self.root)
                node2.setParent(self.root)
                self.insertInNode(middle, self.root)
    

    def insert(self, key):
        """
        Inserts a key in the tree.

        Arguments:
        - key: The key to insert.
        """
        if self.root == None:
            raise ValueError("Need to create a root before inserting a key.")
        else:
            node = self.findNodeToInsert(key, self.root)
            self.insertInNode(key, node)
                        
