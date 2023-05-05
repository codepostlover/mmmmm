from AdjacencyListCP import AdjacencyList
from AdjacencyMatrixCP import AdjacencyMatrix
from Interfaces import List
 
def matrix_equals(a: AdjacencyMatrix, b: AdjacencyMatrix):
    if a.size() != b.size():
        return False
    else:
        n = a.size()
        for i in range(n):
            for j in range(n):
                if a.adj[i][j] != b.adj[i][j]:
                    return False
        return True
 
 
def list_equals(a: AdjacencyList, b: AdjacencyList):
    def contains(l: List, x: object):
        for i in range(l.size()):
            if l.get(i) == x:
                return True
        return False
        
    if a.size() != b.size():
        return False
    else:
        n = a.size()
        for i in range(n):
            if a.adj[i].size() != b.adj[i].size():
                return False
            for j in range(len(a.adj[i])):
                current = a.adj[i].get(j)
                if not contains(b.adj[i], current):
                    return False
        return True