'''
Background:
Duck typing is the functionality of a language where "if it looks like a duck
and quacks like a duck, you might as well treat it like a duck." This is quite
common in interpreted languages.

Assignment:
1. Create a new file named task4.py that calculates the final price of a
   product after applying a given discount percentage inside of a function
   named calculate_discount.
2. The function should accept any numeric type for price and discount.
3. Write pytest test cases to test the calculate_discount function with
   various types (integers, floats) for price and discount.
'''

import decimal

def convert_to_float(value) -> tuple[float, bool]:
  ###
  # Convert any type of input to a float if it is possible
  # to do so. A 'ValueError' exception is raised if the value
  # cannot be converted to a float. Acceptable types are int,
  # float, decimal, complex (the imaginary part is thrown away),
  # and string.
  ###

  error = False

  if isinstance(value, int):
    value = float(value)
  elif isinstance(value, float):
    pass
  elif isinstance(value, decimal.Decimal):
    value = float(value)
  elif isinstance(value, complex):
    value = float(value.real)
  elif isinstance(value, str):
    try:
      value = float(value)
    except ValueError:
      error = True
  else:
    error = True

  return (0.0 if error else round(float(value), 2), error)

def calculate_discount(price, discount) -> float:
  ###
  # Calculate the total price for an item based on the
  # initial price and discount.
  #
  # The values for price and discount are assumbed to be any type that
  # can be converted to float. Notably, the discount is expected to be a
  # percentage; e.g., an 80% discount would be stored as 80 (int),
  # 80.0 (float), 80.0 (decimal), "80" (string), or "80 + Nj" (complex).
  # An input value of 0.80 (for the types that allow such a thing, which
  # excludes int) would be interpreted as 0.008%.
  ###

  (price, error) = convert_to_float(price)
  if error:
    raise TypeError('Price must be a numeric type')

  (discount, error) = convert_to_float(discount)
  if error:
    raise TypeError('Discount must be a numeric type')

  return round(price * (1 - discount / 100), 2)

if __name__ == "__main__":
  ###
  # Run the functions for task 4
  ###

  print(f"$10.00 with 10% discount is ${calculate_discount(10, 10)}")
  print(f"$10.00 with 25.5% discount is ${calculate_discount(10, 25.5)}")
