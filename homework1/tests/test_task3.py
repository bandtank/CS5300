import task3

def test_task3_check_sign_negative():
  result = task3.check_sign(-3)
  assert type(result) is str # The result is the correct type
  assert result == "Negative" # The result is the expected value

def test_task3_check_sign_positive():
  result = task3.check_sign(3)
  assert type(result) is str # The result is the correct type
  assert result == "Positive" # The result is the expected value

def test_task3_check_sign_zero():
  result = task3.check_sign(0)
  assert type(result) is str # The result is the correct type
  assert result == "Zero" # The result is the expected value

def test_task3_get_primes():
  result = task3.get_n_primes(10)
  assert type(result) is list # The result is the correct type
  assert len(result) == 10 # The result is the expected size
  assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # The result is the expected value

def test_task3_sum_range():
  result = task3.sum_range(1, 100)
  assert type(result) is int # The result is the correct type
  assert result == 5050 # The result is the expected value