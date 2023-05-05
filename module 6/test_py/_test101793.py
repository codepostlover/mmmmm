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
          msg += "\n\nAdding elements: "
          for i in range(random.randint(9, 12)):
            r = random.randint(1, 30)
            if r not in expected_heap.a:
              expected_heap.add(r)
              student_heap.add(r)
              msg += str(r) + " "
          msg += "\n\nExpected size: "+ str(expected_heap.size())
          msg += "\nReturned size: " + str(student_heap.size())
          if expected_heap.size() != student_heap.size():
                msg += "\nTest failed."
                return TestOutput(passed = False, logs = msg)
    
          msg += "\nTest passed."
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
f = open("/outputs/101793.json", "w")
json.dump({"id": "101793", "passed": output.passed, "log": output.logs}, f)
f.close()
 