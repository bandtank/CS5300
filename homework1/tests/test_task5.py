import task5

def test_task5_slice_list():
  books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
  result = task5.slice_list()
  assert type(result) is list # The result is the correct type
  assert result == books # The result is the expected value

def test_task5_student_database():
  keys = ["name", "id"]
  result = task5.student_database()
  assert type(result) is list # The result is the correct type
  assert len(result) == 5 # The result has the expected keys

  for row in result:
    assert(set(keys) <= row.keys()) # Every row has the expected keys

  assert result[0]["name"] == "John" # The result is the expected value
  assert result[0]["id"] == "11111" # The result is the expected value