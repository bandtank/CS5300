import os
import task6
import pytest
import utilities.file_manager as fm

def test_task6_count_words_in_file(tmp_path):
  filename = f"{tmp_path}/task6_word_count.txt"

  # Create a tmp file and write strings to it
  with open(filename, 'w') as f:
    f.write("one two three, four five. six seven! eight, nine,  ten\neleven")

  # The result is the expected value
  assert 11 == task6.count_words_in_file(filename)

  # Delete the tmp file
  fm.delete_file(filename)

'''
Dynamically generate the name of a test based on the name of the input file.
'''
@pytest.mark.parametrize("filename", ["task6_read_me.txt"])
def test_task6_read_file(filename):
  path = f"{os.path.dirname(__file__)}/{filename}"

  # The result is the expected value
  result = task6.count_words_in_file(path)
  assert type(result) is int # The result is the correct type
  assert result == 104 # The result is the expected value
