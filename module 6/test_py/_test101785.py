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
          msg += "\nAdding elements: "
          for i in range(random.randint(9, 12)):
            if i != 0:
              msg += ", "
            r = random.randint(1, 35)
            expected_heap.add(r)
            student_heap.add(r)
            msg += str(r)
          msg += "\n\n\tStudent heap: " + str(student_heap) + "\tSize: " + str(student_heap.size())
          msg += "\n\tExpected heap: " + str(expected_heap) + "\tSize: " + str(expected_heap.size())
            
          if expected_heap.size() == student_heap.size():
            msg += "\n\nRemoving all elements..."
            expected_removed = []
            student_removed = []
            while expected_heap.size() > 0:
              expected_r = expected_heap.remove()
              student_r = student_heap.remove()
              
              if expected_r == student_r and str(expected_heap.a[0:expected_heap.n]) != str(student_heap.a[0:student_heap.n]):
                msg += f"\n\nExpected backing array after removing value {expected_r}:\n" + str(expected_heap.a[0:expected_heap.n])
                msg += f"\nStudent backing array after removing value {expected_r}:\n" + str(student_heap.a[0:student_heap.n])
                msg += "\n\nTest failed."
                return TestOutput(passed = False, logs = msg)
              elif expected_r != student_r:
                msg += f"Removed elements: {student_removed}.  \nExpected to remove next element: {expected_r}\nRemoved instead: {student_r}"
                msg += "\n\nTest failed."
                return TestOutput(passed = False, logs = msg)
              else:
                expected_removed.append(expected_r)
                student_removed.append(student_r)
                
            msg += "\nExpected removal: " + str(expected_removed)
            msg += "\nReturned removal: " + str(student_removed)
            if expected_removed == student_removed:
              msg+= "\nTest passed."
              return TestOutput(passed = True, logs = msg)
            else:
              msg += "\nTest failed."
              return TestOutput(passed = False, logs = msg)
      except:
          error = traceback.format_exc()
          msg += "\n\nThe following unexpected error occurred:\n\n" + str(error)
          return TestOutput(passed = False, logs = msg)
    
    
 
    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/101785.json", "w")
json.dump({"id": "101785", "passed": output.passed, "log": output.logs}, f)
f.close()
