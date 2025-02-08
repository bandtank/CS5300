'''
Assignment:
1. Create a new file named task5.py and inside create a list of of your favorite books,
   including book titles and authors.
2. Use list slicing to print the first three books in the list.
3. Create a dictionary that represents a basic student database, including student
   names and their corresponding student IDs.
4. Implement pytest test cases to verify the correctness of your code for each data structure.
'''

import utilities.table_printer as tp

def run_task5() -> None:
  ###
  # Run the functions for task 5
  ###

  data = {
    "headers": ["Book Title"],
    "rows": [],
  }

  books = slice_list()
  for book in books:
    data["rows"].append([book])

  tp.TablePrinter(data)
  print()

  data = {
    "headers": ["Student", "ID"],
    "rows": [],
  }

  for key, value in student_database().items():
    data["rows"].append([key, value])

  tp.TablePrinter(data)

def slice_list() -> list:
  ###
  # Create a list of books and return the first three.
  #
  # The list of books is a two-dimensional array with book titles and
  # authors being separate entries in each row. The output is required to be
  # a list of three books, which is why a list comprehension is used to return
  # only book titles.
  ###

  books = [
    ["The Great Gatsby", "Scott Fitzgerald"],
    ["To Kill a Mockingbird", "Harper Lee"],
    ["1984", "George Orwell"],
    ["Pride and Prejudice", "Jane Austen"],
    ["The Catcher in the Rye", "J.D. Salinger"],
    ["The Lord of the Rings", "J.R.R. Tolkien"]
  ]

  return [x[0] for x in books[0:3]]

def student_database() -> dict:
  ###
  # Create a database of students. This is a very naive interpretation of
  # a database, but it meets the requirements of the task.
  ###

  students = {
      "John": "11111",
      "Jack": "22222",
      "Jill": "33333",
      "Jane": "44444",
      "Jeff": "55555"
  }
  return students

if __name__ == "__main__":
  run_task5()