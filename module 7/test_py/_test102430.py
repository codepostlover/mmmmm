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
    import random
    
    
    def TestCase():
      # TestCase must return a TestOutput Object
      # TestObject is initialized
      array = ArrayList.ArrayList()
      elements = []
      for i in range(random.randint(0, 1)):
        element = random.randint(-30, 30)
        array.append(element)
        elements.append(element)
      
    
      msg = f"Using MERGE SORT to sort array: {str(elements)}"
      algorithms.merge_sort(array)
      sorted_elements = sorted(elements)
      msg += "\nResult: " + str(array)
      msg += "\nExpected: " + str(sorted_elements)
      
      passed = True
      
      if len(sorted_elements) != array.size():
        passed = False
      else:
        for i in range(len(elements)):
          if sorted_elements[i] != array.get(i):
            passed = False
        
      if passed:
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
f = open("/outputs/102430.json", "w")
json.dump({"id": "102430", "passed": output.passed, "log": output.logs}, f)
f.close()
 