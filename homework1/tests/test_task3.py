import task3

def test_task3_check_sign_negative():
  result = task3.check_sign(-3)
  assert type(result) is str
  assert result == "Negative"

def test_task3_check_sign_positive():
  result = task3.check_sign(3)
  assert type(result) is str
  assert result == "Positive"

def test_task3_check_sign_zero():
  result = task3.check_sign(0)
  assert type(result) is str
  assert result == "Zero"

def test_task3_get_primes():
  result = task3.get_n_primes(10)
  assert type(result) is list
  assert len(result) == 10
  assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_task3_sum_range():
  result = task3.sum_range(1, 100)
  assert type(result) is int
  assert result == 5050