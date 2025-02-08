'''
Assignment:
1. Create a new file named task1.py.
2. Write a Python script that prints "Hello, World!" on the console.
3. Set up a pytest test case that verifies the output of your script.
'''

def run_task1() -> str:
  ###
  # Return the string instead of printing because
  # testing is easier that way.
  ###
  return "Hello, World!"

if __name__ == "__main__":
  print(run_task1())