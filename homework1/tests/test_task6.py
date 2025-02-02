import task6
import pytest
import utilities.file_manager as fm

def test_task6_run_task6():
  result = task6.run_task6()
  assert type(result) is str # The result is the correct type
  assert result == "Word count: 104" # The result is the expected value

def test_task6_count_words_in_file():
  filename = "homework1/temp/word_count.task6.txt"

  with open(filename, 'w') as f:
    f.write("one two three, four five. six seven! eight, nine,  ten\neleven")

  #Debug
  #with open(filename, 'r') as f:
  #  word_count = len(f.read().split())

  assert 11 == task6.count_words_in_file(filename) # The result is the expected value

  fm.delete_files('homework1/temp/', '.task6.txt')

'''
Dynamically generate the name of a test based on the name of the input file.
'''
@pytest.mark.parametrize("filename", ["task6_read_me.txt"])
def test_task6_read_file(filename):
  # The result is the expected value
  assert 104 == task6.count_words_in_file(f"homework1/{filename}")