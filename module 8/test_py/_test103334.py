
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
    import AdjacencyList
    import AdjacencyListCP
    import random
    
    def TestCase():
    
      
      msg = "Creating an adjacency matrix..."
      n = random.randint(5, 7)
      try:
        graph = AdjacencyListCP.AdjacencyList(n)
        student_graph = AdjacencyList.AdjacencyList(n)
        msg += "\nAdding edges: "
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
    
        idx = random.randint(0, n-1)
        msg += f"\nTesting out_edges({idx})..."
        expected_edges = graph.out_edges(idx)
        returned_edges = student_graph.out_edges(idx)
        msg += "\nExpected edges: " + str(expected_edges)
        msg += "\nReturned edges: " + str(returned_edges)
    
        if (str(expected_edges) == str(returned_edges)):
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
f = open("/outputs/103334.json", "w")
json.dump({"id": "103334", "passed": output.passed, "log": output.logs}, f)
f.close()
 