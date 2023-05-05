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
    import BinaryHeap
    import BinaryHeapCP
    import random
    
    def TestCase():
      # TestCase must return a TestOutput Object
      # TestObject is initialized
      msg = "Creating a binary heap..."
      try: 
          expected_heap = BinaryHeapCP.BinaryHeap()
          student_heap = BinaryHeap.BinaryHeap()
          
          for i in range(random.randint(9, 12)):
            r = random.randint(1, 30)
            if r not in expected_heap.a:
              expected_heap.add(r)
              student_heap.add(r)
              msg += "\nAdded element: " + str(r)
          msg += "\n\nExpected heap: " + str(expected_heap) +"\tSize: "+ str(expected_heap.size())
          msg += "\nReturned heap: " + str(student_heap) +"\tSize: "+ str(student_heap.size()) + "\n"
              
              
          nodes = []
          n = random.randint(4, 5)
          i = 0
          while i < n:
            node = expected_heap.a[random.randint(0, expected_heap.size()-1)]
            while node in nodes:
              node = expected_heap.a[random.randint(0, expected_heap.size()-1)]
            nodes.append(node)
            i += 1
        
          for j in nodes:
            msg += f"\nTesting depth({j})..."
            d_expected = expected_heap.depth(j)
            d_student = student_heap.depth(j)
            msg += "\nExpected: " + str(d_expected)
            msg += "\nReturned: " + str(d_student) + "\n"
            if d_expected != d_student:
              msg += "\n\nTest failed."
              return TestOutput(passed = False, logs = msg)
          msg += "\n\nTest passed."
          return TestOutput(passed = True, logs = msg)
      except:
          error = traceback.format_exc()
          msg += "\n\nThe following unexpected error occurred:\n\n" + str(error)
          return TestOutput(passed = False, logs = msg)
 
    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/101787.json", "w")
json.dump({"id": "101787", "passed": output.passed, "log": output.logs}, f)
f.close()
