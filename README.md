# Configuration
## Docker
```
docker pull deveduio/django:latest
docker run -d -p 8080:80 -p 3000:3000 --platform linux/amd64 deveduio/django:latest 
```

## Instance
- Update apt and install a few tools:
  ```
  sudo apt update && sudo apt install vim rename
  ```
- Add customizations to `~/.vimrc` and `~/.bashrc`

## Python
#### VENV
- Store virtual environments in `~`:
  ```
  mkdir ~/venv
  ```
- Create a virtual environment for each assignment:
  ```
  python3 -m venv ~/venv/homework1
  python3 -m venv ~/venv/homework2
  python3 -m venv ~/venv/project
  ```
- Source the assignments' virtual environment:
  ```
  . ~/venv/homework1
  ```

#### Dependencies
- Store requirements files for `pip` in `<assignment>/requirements.txt`:
  ```
  homework1/requirements.txt
  homework2/requirements.txt
  project/requirements.txt
  ```
- Update requirements files for the sourced venv using pip:
  ```
  pip freeze > <assignment>/requirements.txt
  ```
- Install the dependencies for the target assignment:
  ```
  pip install -r homework1/requirements.txt
  ```

# Execution
After sourcing a virtual environment and installing all dependencies, run the code using the following commands:

## Scripts
- Individual script:
  ```
  python homework1/task1.py
  ```

## Tests
- Individual tests:
  ```
  pytest homework1/tests/test_task1.py
  ```
- All tests for an assignment:
  ```
  pytest homework1
  ```
- All tests:
  ```
  pytest
  ```
- Run tests with increased verbosity to see the individual test results:
  ```
  pytest -v
  ```