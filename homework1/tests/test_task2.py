import task2

def test_task2_mul_ints():
  result = task2.mul_ints(2, 4)
  assert result == 8
  assert type(result) is int

def test_task2_add_floats():
  result = task2.add_floats(1.2, 2.2, 3)
  assert result == 3.40
  assert type(result) is float

def test_task2_are_ints_equal_false():
  result = task2.are_ints_equal(2, 3)
  assert type(result) is bool
  assert result is False

def test_task2_are_ints_equal_true():
  result = task2.are_ints_equal(-2, -2)
  assert type(result) is bool
  assert result is True

def test_task2_get_random_string():
  allowed = "asdfg"
  result = task2.get_random_string(allowed, 5)
  assert type(result) is str
  assert len(result) == 5
  assert set(result) <= set(allowed)