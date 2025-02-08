import task1

def test_task1_eq():
  assert task1.run_task1() == "Hello, World!" # The result is the expected value

def test_task1_neq():
  assert task1.run_task1() != "Hello, World" # The result is not the expected value