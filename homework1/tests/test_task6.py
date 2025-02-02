import task6
import pytest
import utilities.file_manager as fm

def test_task6_run_task6():
  result = task6.run_task6()
  assert type(result) is str
  assert result == "Word count: 104"

def test_task6_count_words_in_file():
  filename = "homework1/temp/word_count.task6.txt"

  with open(filename, 'w') as f:
    f.write("one two three, four five. six seven! eight, nine,  ten\neleven")

  #Debug
  #with open(filename, 'r') as f:
  #  word_count = len(f.read().split())

  assert 11 == task6.count_words_in_file(filename)

  fm.delete_files('homework1/temp/', '.task6.txt')

@pytest.mark.parametrize("filename", ["task6_read_me.txt"])
def test_task6_read_file(filename):
  assert 104 == task6.count_words_in_file(f"homework1/{filename}")