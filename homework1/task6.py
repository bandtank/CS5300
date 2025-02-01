'''
Write a Python program in Replit that reads a text file (you can create a sample text file) and counts the number of words in it.

Implement metaprogramming techniques to dynamically generate function names for your pytest test cases based on the filenames of the text files.

Include pytest test cases that verify the word count for each text file.
'''
import lorem_text.lorem as lorem
import random
import utilities.file_manager as fm

def run_task6() -> None:
  for i in range(random.randint(6, 10)):
    options = {
        'filename': "temp/" + lorem.words(1) + ".txt",
        'num_sentences': random.randint(3, 10),
    }
    print(f"Creating text file: {options['filename']}")
    create_text_file(options)
    print(f"Word count: {count_words_in_file(options['filename'])}")
    print()

  input('Press enter to delete all temp files')
  fm.delete_temp_files()

def create_text_file(options: dict) -> None:
  with open(options['filename'], 'w') as f:
    for _ in range(options['num_sentences']):
      f.write(lorem.sentence())

def count_words_in_file(filename: str) -> int:
  '''
  Counts the number of words in a text file. Punctuation is not
  considered to be a distinct word; e.g., "Michael Scarn, my boss,
  is insane." would be six words because the commas and period
  are each part of the adjoining word.
  '''
  with open(filename, 'r') as f:
    # Fast, but dumb if the files are big
    return len(f.read().split())

if __name__ == "__main__":
  run_task6()