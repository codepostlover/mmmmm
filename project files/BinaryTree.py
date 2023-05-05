import SLLQueue
from Interfaces import Tree
 
 
class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val
 
        def set_key(self, x):
            self.k = x
 
        def set_val(self, v):
            self.v = v
 
        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left
 
        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right
 
        def __str__(self):
            return f"({self.k}, {self.v})"
 
    def __init__(self):
        self.r = None
 
    def depth(self, u: Node) -> int:
        d = 0
        current_node = u
        while current_node != self.r:
            current_node = current_node.parent
            d += 1
        return d
 
    def height(self) -> int:
        return self._height(self.r)
 
    def _height(self, u: Node) -> int:
        if u is None:
            return 0
        return 1 + max(self._height(u.left), self._height(u.right))
 
    def size(self) -> int:
        return self._size(self.r)
 
    def _size(self, u: Node) -> int:
        if u is None:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)
 
    def bf_order(self):
        l = []
        queue = SLLQueue.SLLQueue()
        queue.add(self.r)
        while queue.size() > 0:
            current = queue.remove()
            l.append(current)
            if current.left is not None:
                queue.add(current.left)
            if current.right is not None:
                queue.add(current.right)
        return l
 
    def in_order(self) -> list:
        return self._in_order(self.r)
 
    def _in_order(self, u: Node) -> list:
        nodes = []
        if u.left is not None:
            nodes.extend(self._in_order(u.left))
        nodes.append(u)
        if u.right is not None:
            nodes.extend(self._in_order(u.right))
        return nodes
 
    def post_order(self) -> list:
        return self._post_order(self.r)
 
    def _post_order(self, u: Node):
        nodes = []
        if u is not None:
            if u.left is not None:
                nodes.extend(self._post_order(u.left))
            if u.right is not None:
                nodes.extend(self._post_order(u.right))
            nodes.append(u)
        return nodes
 
    def pre_order(self) -> list:
        return self._pre_order(self.r)
 
    def _pre_order(self, u: Node):
        nodes = []
        if u is not None:
            nodes.append(u)
            if u.left is not None:
                nodes.extend(self._pre_order(u.left))
            if u.right is not None:
                nodes.extend(self._pre_order(u.right))
        return nodes
 
    def size2(self) -> int:
        u = self.r
        prv = None
        n = 0
        while u is not None:
            if prv == u.parent:
                n += 1
                if u.left is not None:
                    nxt = u.left
                elif u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return n
 
    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)
 
 
# bt = BinaryTree()
# bt.r = BinaryTree.Node(1, 'A')
# b = bt.r.insert_left(BinaryTree.Node(2, 'B'))
# c = bt.r.insert_right(BinaryTree.Node(3, 'C'))
# d = b.insert_left(BinaryTree.Node(4, 'D'))
# e = b.insert_right(BinaryTree.Node(5, 'E'))
# f = c.insert_right(BinaryTree.Node(6, 'F'))
# g = d.insert_right(BinaryTree.Node(7, 'G'))
# h = f.insert_left(BinaryTree.Node(9, 'H'))
# i = f.insert_right(BinaryTree.Node(10, 'I'))
#
#
# print("BF-order:", [str(e.v) for e in bt.bf_order()])
# print("IN-order:", [str(e.v) for e in bt.in_order()])
# print("POST-order:", [str(e.v) for e in bt.post_order()])
# print("PRE-order:", [str(e.v) for e in bt.pre_order()])
#
# print(bt)
 