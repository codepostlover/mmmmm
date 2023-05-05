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
      msg = "Creating a binary heap 'bh'..."
      try: 
          expected_heap = BinaryHeapCP.BinaryHeap()
          student_heap = BinaryHeap.BinaryHeap()
          msg += "\nAdding elements: "
          for i in range(random.randint(9, 45)):
            r = random.randint(1, 30)
            if r not in expected_heap.a:
              expected_heap.add(r)
              student_heap.add(r)
              msg += str(r) + " "
          msg += "\n\nExpected heap: " + str(expected_heap) +"\tSize: "+ str(expected_heap.size())
          msg += "\nReturned heap: " + str(student_heap) +"\tSize: "+ str(student_heap.size()) + "\n"
          
          msg += "\nTesting bh.in_order()..."
          expected_trav = expected_heap.in_order()
          student_trav = student_heap.in_order()
          
          msg += "\n\nExpected in-order traversal:\n" + str(expected_trav) 
          msg += "\nReturned in-order traversal:\n" + str(student_trav) 
    
          if str(expected_trav) != str(student_trav):
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
f = open("/outputs/101790.json", "w")
json.dump({"id": "101790", "passed": output.passed, "log": output.logs}, f)
f.close()
 