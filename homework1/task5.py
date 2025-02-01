'''
Assignment:
1. Create a new file named task5.py and inside create a list of of your favorite books,
   including book titles and authors.
2. Use list slicing to print the first three books in the list.
3. Create a dictionary that represents a basic student database, including student
   names and their corresponding student IDs.
4. Implement pytest test cases to verify the correctness of your code for each data structure.
'''
import pprint

def run_task5() -> None:
  print(slice_list())
  print()

  print(f"{'Student':<10}  {'ID':<10}")
  print(f"{'----':<10}  {'----':<10}")
  for student in student_database().items():
    print(f"{student[0]:<10}  {student[1]:<10}")

def slice_list() -> list:
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