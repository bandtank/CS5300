'''
Assignent:
1. Create two new files named task6.py and task6_read_me.txt.
2. Inside of task6_read_me.txt add:

    Lorem ipsum dolor sit amet , consectetur adipiscing elit . Duis vitae feugiat
    tortor , quis tempus lacus . Maecenas sollicitudin rhoncus ultricies .
    Mauris neque metus , blandit sed sagittis aliquam , fringilla eget massa .
    Donec at luctus leo. Curabitur suscipit nulla aliquam sapien maximus ,
    sit amet fermentum sem malesuada . Nulla suscipit , felis non consequat
    eleifend , sem quam pharetra turpis , vel efficitur tellus est placerat
    est . Nam metus orci , facilisis et ante sed , ultricies pulvinar lorem .
    Phasellus eu ipsum sit amet ex auctor volutpat . Suspendisse ac turpis et
    felis tristique facilisis vitae in diam . Donec maximus ex in lorem
    auctor vulputate . Nulla finibus sodales ante , convallis gravida metus
    iaculis id.

3. Then write a program inside task6.py of that reads task6_read_me.txt and
   counts the number of words in it.
4. Implement metaprogramming techniques to dynamically generate function names
   for your pytest test cases based on the filenames of the text files.
5. Include pytest test cases that verify the word count for each text file.
'''
import lorem_text.lorem as lorem
import random
import utilities.file_manager as fm

def run_task6() -> None:
  for i in range(random.randint(6, 10)):
    options = {
        'filename': "homework1/temp/" + lorem.words(1) + ".txt",
        'num_sentences': random.randint(3, 10),
    }
    print(f"Creating text file: {options['filename']}")
    create_text_file(options)
    print(f"Word count: {count_words_in_file(options['filename'])}")
    print()

  input('Press enter to delete all temp files')
  fm.delete_files('homework1/temp/', '.txt')

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