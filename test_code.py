"""
Module to Test Code
"""

import json

def test_func(data):
  """
  Test function
  """
  datadict = json.loads(data)
  print(f"Data Dictionay : {datadict}")
  
test_func('{"key" : "value"}')
