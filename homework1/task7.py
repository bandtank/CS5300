'''
Assignment:
1. Use pip package manager to add a Python package of your choice to your project (e.g.,
   requests, numpy, matplotlib).
2. Create two new files named task7.py and write a Python script that demonstrates
   how to use the chosen package to perform a specific task or function.
3. Implement pytest test cases to verify the correctness of your code when using the package.
'''

import lorem_text.lorem as lorem
import random

def get_sentences(min_sentences: int, max_sentences: int) -> list[str]:
  ###
  # Generate a list of sentences. The list should have at least
  # min_sentences sentences and at most max_sentences sentences.
  ###

  return [lorem.sentence() for _ in range(random.randint(min_sentences, max_sentences))]

def get_words(min_words: int, max_words: int) -> str:
  ###
  # Generate a string of words. The string should have at least
  # min_words words and at most max_words words.
  ###
  return lorem.words(random.randint(min_words, max_words))

if __name__ == "__main__":
  ###
  # Run the functions for task 7
  ###

  print(get_sentences(2, 4))
  print(get_words(2, 4))