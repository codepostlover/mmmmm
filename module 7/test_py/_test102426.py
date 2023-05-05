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
    # To call a student's method, uncomment the following line and call <fileName>.<method>
    import ArrayList
    import algorithms
    import algorithmsCP
    import random
    
    
    def TestCase():
      # TestCase must return a TestOutput Object
      # TestObject is initialized
      array = ArrayList.ArrayList()
      for i in range(random.randint(10, 15)):
        array.append(random.randint(-30, 30))
    
      x = random.randint(-100, 100)
      while x <= 30 and x >= -30:
        x = random.randint(-100, 100)
      msg = f"Searching for {x} in array: {str(array)}"
      idx_returned = algorithms.linear_search(array, x)
      msg += "\nReturned: " + str(idx_returned)
      msg += "\nExpected: None"
        
      if (idx_returned is None):
        msg += "\n\nTest passed."
        return TestOutput(passed=True, logs=msg)
      else:
        msg += "\n\nTest failed."
        return TestOutput(passed=False, logs=msg)
 
    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/102426.json", "w")
json.dump({"id": "102426", "passed": output.passed, "log": output.logs}, f)
f.close()
 