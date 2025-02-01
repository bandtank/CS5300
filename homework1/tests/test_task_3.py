import task_3

def test_task_3_check_sign_negative():
  result = task_3.check_sign(-3)
  assert type(result) is str
  assert result == "Negative"

def test_task_3_check_sign_positive():
  result = task_3.check_sign(3)
  assert type(result) is str
  assert result == "Positive"

def test_task_3_check_sign_zero():
  result = task_3.check_sign(0)
  assert type(result) is str
  assert result == "Zero"

def test_task_3_get_primes():
  result = task_3.get_n_primes(10)
  assert type(result) is list
  assert len(result) == 10
  assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_task_3_sum_range():
  result = task_3.sum_range(1, 100)
  assert type(result) is int
  assert result == 5050