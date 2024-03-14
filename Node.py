class Node:
    """
    Class representing a node in a B-tree.
    """
    def __init__(self,size, isLeaf):
        self.size = size
        self.keys = []
        self.children = []
        self.parent = None
        self.leaf = isLeaf

    def getSize(self):
            """
            Returns the size of the node.
            """
            return self.size

    def getKeys(self):
            """
            Returns the list of keys in the node.
            """
            return self.keys
    
    def getParent(self):
        """
        Returns the parent of the node.
        """
        return self.parent
    
    def setParent(self, parent):
        """
        Sets the parent of the node.
        """
        self.parent = parent
    
    def getNbKeys(self):
        """
        Returns the number of keys in the node.
        """
        return len(self.keys)
        
    def getChildren(self):
            """
            Returns the list of children of the node.
            """
            return self.children
        
    def isLeaf(self):
            """
            Returns True if the node is a leaf, False otherwise.
            """
            return self.leaf
    
    def ifFull(self):
        """
        Returns True if the node is full, False otherwise.
        """
        return self.getSize() == self.size
    
    def setKeys(self, keys):
            """
            Sets the list of keys in the node.
            """
            self.keys = keys

    def setChildren(self, children):
            """
            Sets the list of children of the node.
            """
            if len(children) == len(self.keys) + 1:
                self.children = children
            else:
                print("Error: The number of children is not correct")
                

    def addKey(self, key):
            """
            Adds a key to the node in sorted order.
            """
            self.keys.append(key)
            self.keys.sort()
            
            
            