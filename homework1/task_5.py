'''
Create a list in Replit of your favorite books, including book titles and authors. Use list slicing to print the first three books in the list.

Create a dictionary that represents a basic student database, including student names and their corresponding student IDs.

Implement pytest test cases to verify the correctness of your code for each data structure.
'''
import pprint

def run_task_5() -> None:
  print(slice_list())
  print()

  print(f"{'Student':<10}  {'ID':<10}")
  print(f"{'----':<10}  {'----':<10}")
  for student in student_database().items():
    print(f"{student[0]:<10}  {student[1]:<10}")

def slice_list() -> list:
  books = [["The Great Gatsby", "Scott Fitzgerald"],
           ["To Kill a Mockingbird", "Harper Lee"], ["1984", "George Orwell"],
           ["Pride and Prejudice", "Jane Austen"],
           ["The Catcher in the Rye", "J.D. Salinger"],
           ["The Lord of the Rings", "J.R.R. Tolkien"]]

  return [x[0] for x in books[0:3]]

def student_database() -> dict:
  students = {
      "John": "11111",
      "Jack": "22222",
      "Jill": "33333",
      "Jane": "44444",
      "Jeff": "55555"
  }
  return students

if __name__ == "__main__":
  run_task_5()