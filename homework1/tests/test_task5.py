import task5

def test_task5_slice_list():
  books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
  result = task5.slice_list()
  assert type(result) is list # The result is the correct type
  assert result == books # The result is the expected value

def test_task5_student_database():
  keys = ["John", "Jack", "Jill", "Jane", "Jeff"]
  result = task5.student_database()
  assert type(result) is dict # The result is the correct type
  assert list(result.keys()) == keys # The result has the expected keys
  assert result["Jeff"] == "55555" # The result is the expected value