'''
Assignment:
1. Create a new file named task3.py.
2. Create an if statement to check if a given number is positive, negative, or zero.
3. Implement a for loop to print the first 10 prime numbers (you may need to
   research how to calculate prime numbers).
4. Create a while loop to find the sum of all numbers from 1 to 100.
5. Write pytest test cases to verify the correctness of your code for each control
   structure.
'''
def run_task3() -> None:
  print(check_sign(-3))
  print(get_n_primes(10))
  print(sum_range(1, 100))

def check_sign(num: int) -> str:
  '''
  Determine the sign of a number.
  '''
  if num < 0:
    return "Negative"
  elif num > 0:
    return "Positive"
  else:
    return "Zero"

def get_n_primes(count: int) -> list:
  '''
  Get 'count' primes.
  '''
  if count <= 0:
    return []

  # 2 is the first prime number, so there is no need to calculate it.
  primes = [2]

  # Start checking at 3, and only check odd numbers to save time. Other
  # optimizations could be made, such as skipping numbers that end in 5,
  # but this exercise is not about optimization.
  number = 3

  while len(primes) < count:
    if is_prime(number):
      primes.append(number)
    number += 2

  return primes

def is_prime(number: int) -> bool:
  '''
  Check if a number is prime.

  This primality test is not the most efficient way to check for primality,
  but it is sufficient for this exercise. To optimize the algorithm, it would
  be best to divide each preceding prime number into the number under test;
  if no prime numbers divide into the number under test, the number under test
  is prime. The chosen method is simpler and easier to understand, which is
  to check for divisibility up to the square root of the number under test:
  '''
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True

def sum_range(start: int, end: int) -> int:
  '''
  Sum a range of numbers.

  This would be much faster:
    return sum(range(start, end + 1))

  Alas, we must use a while loop.
  '''
  total = 0

  while start <= end:
    total += start
    start += 1

  return total

if __name__ == "__main__":
  run_task3()