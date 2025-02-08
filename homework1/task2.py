'''
Assignment:
1. Create a new file named task2.py demonstrating the use of various data types,
   including integers, floating-point numbers, strings, and booleans.
2. Implement a Python using pytest to test case for each data type, ensuring
   that the script’s behavior matches the expected outcomes.
'''

import random
import utilities.table_printer as tp

def run_task2() -> None:
  ###
  # Run the functions for task 2
  ###

  data = {
    "headers": ["Description", "Function", "Inputs", "Output", "Output Type"],
    "column_padding": 3
  }

  # Run the functions and collect the results
  mul_ints_result = mul_ints(2,4)
  add_floats_result = add_floats(1.0, 2.2)
  are_ints_equal_result = are_ints_equal(1, 2)
  get_random_string_result = get_random_string("abcde", 3)

  # Create output rows to print to the screen
  data["rows"] = [
    [
      "Multiply ints",
      "mul_ints",
      "2, 4",
      mul_ints_result,
      type(mul_ints_result).__name__,
    ],
    [
      "Add floats",
      "add_floats",
      "1.0, 2.2",
      add_floats_result,
      type(add_floats_result).__name__,
    ],
    [
      "Are ints equal?",
      "are_ints_equal",
      "1, 2",
      "True" if are_ints_equal_result else "False",
      type(are_ints_equal_result).__name__,
    ],
    [
      "Get a random string",
      "get_random_string",
      "'abcde', 3",
      str(get_random_string_result),
      type(get_random_string_result).__name__,
    ]
  ]

  tp.TablePrinter(data)

def mul_ints(a: int, b: int) -> int:
  ###
  # Multiply two ints and return an int
  ###
  return a * b

def add_floats(a: float, b: float, precision: int = 2) -> float:
  ###
  # Add two floats and return a float.
  # Note: the returned value is rounded to a given precision
  # to avoid issues with floating point math.
  ###
  return round(a + b, precision)

def are_ints_equal(a: int, b: int) -> bool:
  ###
  # Compare two ints and return a boolean result.
  ###
  return a == b

def get_random_string(letters: str, count: int) -> str:
  ###
  # Return a random string of characters with a length of count
  # by constructing a list using a list comprehension.
  ###
  return "".join([random.choice(letters) for _ in range(count)])

if __name__ == "__main__":
  run_task2()