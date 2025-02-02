import task2

def test_task2_mul_ints():
  result = task2.mul_ints(2, 4)
  assert type(result) is int # The result is the correct type 
  assert result == 8 # The result is the expected value

def test_task2_add_floats():
  result = task2.add_floats(1.2, 2.2, 3)
  assert type(result) is float # The result is the correct type
  assert result == 3.40 # The result is the expected value

def test_task2_are_ints_equal_false():
  result = task2.are_ints_equal(2, 3)
  assert type(result) is bool # The return value is the correct type
  assert result is False # The result is the expected value

def test_task2_are_ints_equal_true():
  result = task2.are_ints_equal(-2, -2)
  assert type(result) is bool # The return value is the correct type
  assert result is True # The result is the expected value

def test_task2_get_random_string():
  allowed = "asdfg"
  result = task2.get_random_string(allowed, 5)
  assert type(result) is str # The return value is the right type
  assert len(result) == 5 # The string is the correct length
  assert set(result) <= set(allowed) # Only the specified characters have been used