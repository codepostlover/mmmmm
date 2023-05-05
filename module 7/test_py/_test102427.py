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
      elements = []
      for i in range(random.randint(10, 15)):
        element = random.randint(-30, 30)
        while element in elements:
          element = random.randint(-30, 30)
        elements.append(element)
        
      elements = sorted(elements)
      
      for e in elements:
        array.append(e)
      
      idx_expected = random.randint(0, array.size() - 1)
      x = array.get(idx_expected)
      msg = f"Searching for {x} in array: {str(array)}"
      idx_returned = algorithms.binary_search(array, x)
      msg += "\nReturned: " + str(idx_returned)
      msg += "\nExpected: " + str(idx_expected)
        
      if (idx_returned == idx_expected):
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
f = open("/outputs/102427.json", "w")
json.dump({"id": "102427", "passed": output.passed, "log": output.logs}, f)
f.close()
 