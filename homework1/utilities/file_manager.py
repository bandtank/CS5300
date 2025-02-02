import os

def delete_files(path: str, ext: str) -> None:
  for filename in os.listdir(path):
    if filename.endswith(ext):
      os.remove(os.path.join(path, filename))

if __name__ == "__main__":
  delete_temp_files()