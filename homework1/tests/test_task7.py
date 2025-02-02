import task7

def test_task7_get_sentences():
  sentences = task7.get_sentences(3, 3)
  assert type(sentences) is list # The result is the correct type
  assert len(sentences) == 3 # The result is the expected value

def test_task7_get_sentences_min_max():
  sentences = task7.get_sentences(6, 20)
  assert type(sentences) is list # The result is the correct type
  assert 6 <= len(sentences) <= 20 # The result is the expected value

def test_task7_get_words():
  words = task7.get_words(10, 10)
  assert type(words) is str # The result is the correct type
  assert len(words.split()) == 10 # The result is the expected value

def test_task7_get_words_min_max():
  words = task7.get_words(6, 20)
  assert type(words) is str # The result is the correct type
  assert 6 <= len(words.split()) <= 20 # The result is the expected value