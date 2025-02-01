'''
Create a Python function in Replit named calculate_discount that calculates the final price of a product after applying a given discount percentage. The function should accept any numeric type for price and discount.

Write pytest test cases to test the calculate_discount function with various types (integers, floats) for price and discount.
'''
import decimal

def run_task4() -> None:
  print(f"$10.00 with 10% discount is ${calculate_discount(10, 10)}")
  print(f"$10.00 with 25.5% discount is ${calculate_discount(10, 25.5)}")

def convert_to_float(value) -> tuple[float, bool]:
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
  '''
  Price and discount could be int, float, decimal, or complex. It is
  also possible that price and discount could be coerced from a string.
  Any other data type will cause the function to raise a TypeError.

  It is assumed that discount is a percentage; e.g., 10% is 10, 25.5% is 25.5,
  and so on.
  '''
  (price, error) = convert_to_float(price)
  if error:
    raise TypeError('Price must be a numeric type')

  (discount, error) = convert_to_float(discount)
  if error:
    raise TypeError('Discount must be a numeric type')

  return round(price * (1 - discount / 100), 2)

if __name__ == "__main__":
  run_task4()
