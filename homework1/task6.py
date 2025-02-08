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

def run_task6() -> None:
  ###
  # Run the functions for task 6
  ###

  filename = "homework1/task6_read_me.txt"
  return f"Word count: {count_words_in_file(filename)}"

def count_words_in_file(path: str) -> int:
  ###
  # Counts the number of words in a text file. Punctuation is not
  # considered to be a distinct word; e.g., "Michael Scarn, my boss,
  # is insane." would be six words because the commas and period
  # are each part of the adjoining word.
  ###

  with open(path, 'r') as f:
    # Fast, but dumb if the files are big
    return len(f.read().split())

if __name__ == "__main__":
  print(run_task6())