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
  known_good = [
     2,  3,  5,  7, 11,  13,  17,  19,  23,  29,
    31, 37, 41, 43, 47,  53,  59,  61,  67,  71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
  ]

  result = task3.get_n_primes(10)
  assert type(result) is list # The result is the correct type
  assert len(result) == 10 # The result is the expected size
  assert result == known_good[:10] # The result is the expected value

  result = task3.get_n_primes(30)
  assert type(result) is list # The result is the correct type
  assert len(result) == 30 # The result is the expected size
  assert result == known_good[:30] # The result is the expected value

def test_task3_sum_range():
  result = task3.sum_range(1, 100)
  assert type(result) is int # The result is the correct type
  assert result == 5050 # The result is the expected value

  result = task3.sum_range(-100, 100)
  assert type(result) is int # The result is the correct type
  assert result == 0 # The result is the expected value