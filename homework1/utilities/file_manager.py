import os

def delete_temp_files() -> None:
  for filename in os.listdir('temp'):
    if filename.endswith(".txt"):
      os.remove(os.path.join('temp', filename))

if __name__ == "__main__":
  delete_temp_files()