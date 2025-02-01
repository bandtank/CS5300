'''
Create a Python script in Replit that demonstrates the use of various data types, including integers, floating-point numbers, strings, and booleans.

Implement a pytest test case for each data type, ensuring that the script's behavior matches the expected outcomes.
'''
import random

def run_task_2() -> None:
  result = mul_ints(2, 4)
  print(f"Multiply ints:     2 * 4 = {result:<10}Type = {type(result)}")

  result = add_floats(1.0, 2.2)
  print(f"Add floats:    1.0 + 2.2 = {result:<10}Type = {type(result)}")

  result = are_ints_equal(1, 2)
  print(f"Are ints equal:   1 == 2 = {'True' if result else 'False':<10}Type = {type(result)}")

  result = get_random_string("abcde", 3)
  print(f"Get random string:         {result:10}Type = {type(result)}")

def mul_ints(a: int, b: int) -> int:
  return a * b

def add_floats(a: float, b: float, precision: int = 2) -> float:
  return round(a + b, precision)

def are_ints_equal(a: int, b: int) -> bool:
  return a == b

def get_random_string(letters: str, count: int) -> str:
  return "".join([random.choice(letters) for _ in range(count)])

if __name__ == "__main__":
  run_task_2()