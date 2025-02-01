import pytest
import task4
import decimal

def test_task4_calculate_discount_int():
  price = 10
  discount = 10
  result = task4.calculate_discount(price, discount)
  assert type(result) is float
  assert result == 9.00

def test_task4_calculate_discount_float():
  price = 10.0
  discount = 3.5
  result = task4.calculate_discount(price, discount)
  assert type(result) is float
  assert result == 9.65

def test_task4_calculate_discount_decimal():
  price = decimal.Decimal(1.25)
  discount = decimal.Decimal(55.2)
  result = task4.calculate_discount(price, discount)
  assert type(result) is float
  assert result == 0.56

def test_task4_calculate_discount_complex():
  price = complex(3.13, 5)
  discount = complex(20, 3)
  result = task4.calculate_discount(price, discount)
  assert type(result) is float
  assert result == 2.50

def test_task4_calculate_discount_str():
  price = 'a'
  discount = 10.1
  with pytest.raises(TypeError) as e:
    task4.calculate_discount(price, discount)
  assert str(e.value) == "Price must be a numeric type"

  price = "3.52"
  discount = "10.1"
  result = task4.calculate_discount(price, discount)
  assert type(result) is float
  assert result == 3.16

def test_task4_calculate_discount_other():
  price = []
  discount = {}
  with pytest.raises(TypeError) as e:
    task4.calculate_discount(price, discount)
  assert str(e.value) == "Price must be a numeric type"

  price = 4
  with pytest.raises(TypeError) as e:
    task4.calculate_discount(price, discount)
  assert str(e.value) == "Discount must be a numeric type"