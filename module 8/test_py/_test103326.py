
import json
import traceback
import os
 
class TestOutput:
    def __init__(self, passed, logs):
        assert (isinstance(passed, bool))
        assert (isinstance(logs, str))
        self.passed = passed
        self.logs = logs
 
try:
    import AdjacencyMatrix
    import AdjacencyMatrixCP
    import random
    import comparators
    
    def TestCase():
    
      
      msg = "Creating an adjacency matrix..."
      try:
        n = random.randint(5, 7)
        graph = AdjacencyMatrixCP.AdjacencyMatrix(n)
        student_graph = AdjacencyMatrix.AdjacencyMatrix(n)
        msg += "\nAdding edges: "
        added = []
        for i in range(n):
          for j in range(random.randint(1, n-3)):
              k = random.randint(0, n-1)
              while i == k:
                k = random.randint(0, n-1)
              msg += f"({i}, {k}) "
              graph.add_edge(i, k)
              student_graph.add_edge(i, k)
              added.append((i, k))
    
        (x, y) = added[random.randint(0, len(added)-1)]
    
    
        msg += f"\n\nTesting has_edge({x}, {y})..."
        expected = graph.has_edge(x, y)
        returned = student_graph.has_edge(x, y)
    
        msg += "\nExpected boolean: " + str(expected)
        msg += "\nReturned boolean: " + str(returned)
    
        (u, v) = (random.randint(0, n-1), random.randint(0, n-1))
    
        while graph.has_edge(u, v):
          (u, v) = (random.randint(0, n-1), random.randint(0, n-1))
    
        msg += f"\n\nTesting has_edge({u}, {v})..." 
        expected2 = graph.has_edge(u, v)
        returned2 = student_graph.has_edge(u, v)
    
        msg += "\nExpected boolean: " + str(expected2)
        msg += "\nReturned boolean: " + str(returned2)
    
        if (comparators.matrix_equals(graph, student_graph) and expected2 == returned2):
          msg += "\n\nTest passed."
          return TestOutput(passed=True, logs=msg)
        else:
          msg += "\n\nTest failed."
          return TestOutput(passed=False, logs=msg)
      except:
        error = traceback.format_exc()
        msg += f"\nThe following unexpected error occurred: {error}"
        return TestOutput(passed=False, logs=msg)
    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/103326.json", "w")
json.dump({"id": "103326", "passed": output.passed, "log": output.logs}, f)
f.close()
 