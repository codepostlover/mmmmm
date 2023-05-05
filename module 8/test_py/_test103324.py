
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
    import comparators
    import random
    
    def TestCase():
      msg = "Creating an adjacency matrix..."
      try:
        
        n = random.randint(5, 7)
        graph = AdjacencyMatrixCP.AdjacencyMatrix(n)
        student_graph = AdjacencyMatrix.AdjacencyMatrix(n)
        msg += f"\nAdding edges: "
        for i in range(n):
          for j in range(random.randint(1, n-3)):
              k = random.randint(0, n-1)
              while i == k:
                k = random.randint(0, n-1)
              msg += f"({i}, {k}) "
              graph.add_edge(i, k)
              student_graph.add_edge(i, k)
    
        expected = str(graph)  
        returned = str(student_graph)
        msg += "\n\nExpected graph:\n" + expected
        msg += "\n\nCreated graph:\n" + returned
    
    
        if (comparators.matrix_equals(graph, student_graph)):
          msg += "\nTest passed."
          return TestOutput(passed=True, logs=msg)
        else:
          msg += "\nTest failed."
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
f = open("/outputs/103324.json", "w")
json.dump({"id": "103324", "passed": output.passed, "log": output.logs}, f)
f.close()
 