import task5

def test_task5_slice_list():
  books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
  result = task5.slice_list()
  assert type(result) is list
  assert result == books

def test_task5_student_database():
  keys = ["John", "Jack", "Jill", "Jane", "Jeff"]
  result = task5.student_database()
  assert type(result) is dict
  assert list(result.keys()) == keys
  assert result["Jeff"] == "55555"