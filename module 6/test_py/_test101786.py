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
      msg = "Creating empty binary heap and attempting to remove..."
    
      try:
          expected_heap = BinaryHeapCP.BinaryHeap()
          student_heap = BinaryHeap.BinaryHeap()  
          msg += "\n\nExpected: IndexError"
          e = student_heap.remove()
          msg += "\nReturned: " + str(e)
          msg += "\nTest failed."
          return TestOutput(passed = False, logs = msg)
      except IndexError:
          msg += "\nRaised IndexError"
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
f = open("/outputs/101786.json", "w")
json.dump({"id": "101786", "passed": output.passed, "log": output.logs}, f)
f.close()
 