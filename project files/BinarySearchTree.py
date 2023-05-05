from Interfaces import Set
 
 
class BinarySearchTree(BinaryTree, Set):
 
    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0
 
    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        p = self._find_last(key)
        return self._add_child(p, BinaryTree.Node(key, value))
 
    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        node = self._find_eq(key)
        if node is None:
            return None
        return node.v
 
    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        u = self._find_eq(key)
        if u is None:
            raise ValueError("Key does not exist.")
        val = u.v
        self._remove_node(u)
        return val
 
    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        if self.r is None:
            return None
        else:
            current = self.r
            while current is not None:
                if key == current.k:
                    return current
                elif key > current.k:
                    current = current.right
                else:
                    current = current.left
            return None
 
    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        current = self.r
        current_parent = None
        while current is not None:
            current_parent = current
            if key == current.k:
                return current
            elif key > current.k:
                current = current.right
            else:
                current = current.left
        return current_parent
 
    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        if p is None:
            self.r = u  # inserting into empty tree
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False  # u.x is already in the tree
            u.parent = p
        self.n += 1
        return True
 
    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u only has one child
        """
        p = None
        if u.left is not None:
            child = u.left
        else:
            child = u.right
 
        if u == self.r:
            self.r = child
        else:
            p = u.parent
            if p.left == u:
                p.left = child
            else:
                p.right = child
 
        if child is not None:
            child.parent = p
 
        self.n -= 1
        return
 
    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0
 
    def _remove_node(self, u: BinaryTree.Node):
        if u.left is None or u.right is None:
            self._splice(u)
        else:
            current = u.right
            while current.left is not None:
                current = current.left
            u.k = current.k
            u.v = current.v
            self._splice(current)
        return
 
    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)
 
    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w
 
    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
 
    def smallest_geq(self, key: object) -> object:
        """
        returns the node with the key that either matches the given key,
        or if such does not exist, the node with the smallest key that is larger
        than the given key.
        """
        current = self.r
        smallest = None
        while current is not None:
            if key < current.k:
                smallest = current
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        if smallest is None:
            return None
        return smallest
 
    def largest_leq(self, key):
        """
        returns the node with the key that either matches the given key,
        or if such key does not exist, the node with the largest key that is smaller
        than the given key
        """
        current = self.r
        largest = None
        while current is not None:
            if current.k < key:
                largest = current
                current = current.right
            elif current.k > key:
                current = current.left
            else:
                return current
        return largest
 
    def next_smallest_key(self, key):
        nodes = self.in_order()
        i = 0
        while nodes[i].k < key:
            i += 1
        if i > 0:
            return nodes[i - 1].k
        else:
            return None
 
 
 