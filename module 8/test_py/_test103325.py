
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
      n = random.randint(5, 7)
      try:
        graph = AdjacencyMatrixCP.AdjacencyMatrix(n)
        student_graph = AdjacencyMatrix.AdjacencyMatrix(n)
    
        added = []
        msg += f"\nAdding edges: "
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
    
        msg += f"\n\nRemoving edge: ({x}, {y})"
        expected_removed = graph.remove_edge(x, y)
        returned_removed = student_graph.remove_edge(x, y)
        expected_graph = str(graph)  
        returned_graph = str(student_graph)
        msg += "\nExpected boolean: " + str(expected_removed)
        msg += "\nReturned boolean: " + str(returned_removed)
        msg += "\n\nExpected graph after removal:\n" + expected_graph
        msg += "\n\nStudent graph after removal:\n" + returned_graph
        test1 = comparators.matrix_equals(graph, student_graph)
    
        msg += f"\n\nAttempting to remove the same edge again: ({x}, {y})"
        expected_removed2 = graph.remove_edge(x, y)
        returned_removed2 = student_graph.remove_edge(x, y)
        expected_graph2 = str(graph)  
        returned_graph2 = str(student_graph)
        msg += "\nExpected boolean: " + str(expected_removed2)
        msg += "\nReturned boolean: " + str(returned_removed2)
        msg += "\n\nExpected graph after removal:\n" + expected_graph2
        msg += "\n\nStudent graph after removal:\n" + returned_graph2
        test2 = comparators.matrix_equals(graph, student_graph)
        
        if ( test1 and expected_removed == returned_removed and test2 and expected_removed2 == returned_removed2):
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
f = open("/outputs/103325.json", "w")
json.dump({"id": "103325", "passed": output.passed, "log": output.logs}, f)
f.close()
 