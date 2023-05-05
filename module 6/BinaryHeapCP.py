import math
from Interfaces import Queue
from Interfaces import Tree
 
 
def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return (2 * i) + 1
 
 
def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)
 
 
def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2
 
 
def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)
 
 
class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0
 
    def add(self, x: object):
        if self.n == len(self.a):
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True
 
    def remove(self):
        if self.n == 0:
            raise IndexError("Can not remove from empty binary heap.")
        smallest = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        return smallest
 
    def depth(self, u) -> int:
        idx = -1
        for j in range(self.n):
            if self.a[j] == u:
                idx = j
                break
        if idx == -1:
            raise ValueError(f"{u} is not found in the binary heap")
        return int(math.log2(idx+1))
 
    def height(self) -> int:
        return int(math.log2(self.n))
 
    def bf_order(self) -> list:
        return self.a[0:self.n]
 
    def in_order(self) -> list:
        indices = self._in_order(0)
        return [self.a[idx] for idx in indices]
 
    def post_order(self) -> list:
        indices = self._post_order(0)
        return [self.a[idx] for idx in indices]
 
    def pre_order(self) -> list:
        indices = self._pre_order(0)
        return [self.a[idx] for idx in indices]
 
    def size(self) -> int:
        return self.n
 
    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]
 
    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        # # print(f"\tCurrent at i = {i}:", self.a[i])
        # # print(f"\tParent at {p_idx}:", self.a[p_idx])
        while i > 0 and self.a[i] < self.a[p_idx]:
            # # print("while is true")
            temp = self.a[p_idx]
            self.a[p_idx] = self.a[i]
            self.a[i] = temp
            # # print(f"\t\tSwapped {self.a[i]} with {self.a[p_idx]}")
            i = p_idx
            p_idx = parent(i)
            # # print("\t\tCurrent:", self.a[i])
            # # print("\t\tNew parent:", self.a[p_idx])
        return
 
    def _resize(self):
        a = _new_array(2 * self.n)
        for i in range(self.n):
            a[i] = self.a[i]
        self.a = a
 
    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        valid = i < self.n and (l_idx < self.n or r_idx < self.n)
        # print(f"\tCurrent at {i}:", self.a[i])
        # print(f"\tLeft child at {l_idx}:", self.a[l_idx])
        # print(f"\tRight child at {r_idx}:", self.a[r_idx])
        while valid and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            # # print("\tWhile is true.")
            # parent compared to left
            if self.a[l_idx] < self.a[i]:
                min_idx = l_idx
            else:
                min_idx = i
            if self.a[r_idx] < self.a[min_idx]:
                min_idx = r_idx
            # print(f"\t\tMin at {min_idx}:", self.a[min_idx])
            # print(f"\t\tSwapping {self.a[i]} with {self.a[min_idx]}")
            temp = self.a[min_idx]
            self.a[min_idx] = self.a[i]
            self.a[i] = temp
 
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)
            valid = i < self.n and (l_idx < self.n or r_idx < self.n)
            # print(f"\t\tUpdated Current at {i}:", self.a[i])
            # print(f"\t\tLeft child at {l_idx}:", self.a[l_idx])
            # print(f"\t\tRight child at {r_idx}:", self.a[r_idx])
            # print(f"\t\tBacking array:", self.a[0:self.n])
            # print("\t\tSize:", self.n)
        return
 
    def _in_order(self, i):
        indices = []
        l_idx = left(i)
        r_idx = right(i)
        # print(f"Parent at {i}:", self.a[i])
        if 0 <= l_idx < self.n:
            # print(f"\tLeft child at {l_idx}:", self.a[l_idx])
            indices.extend(self._in_order(l_idx))
        if 0 <= i < self.n:
            # print(f"\tAdded parent")
            indices.append(i)
        if 0 <= r_idx < self.n:
            # print(f"\tRight child at {r_idx}:", self.a[r_idx])
            indices.extend(self._in_order(r_idx))
        return indices
 
    def _post_order(self, i):
        indices = []
        l_idx = left(i)
        r_idx = right(i)
        if 0 <= l_idx < self.n:
            indices.extend(self._post_order(l_idx))
        if 0 <= r_idx < self.n:
            indices.extend(self._post_order(r_idx))
        if 0 <= i < self.n:
            indices.append(i)
        return indices
 
    def _pre_order(self, i):
        indices = []
        l_idx = left(i)
        r_idx = right(i)
        if 0 <= i < self.n:
            indices.append(i)
        if 0 <= l_idx < self.n:
            indices.extend(self._pre_order(l_idx))
        if 0 <= r_idx < self.n:
            indices.extend(self._pre_order(r_idx))
 
        return indices
 
    def __str__(self):
        return str(self.a[0:self.n])
 