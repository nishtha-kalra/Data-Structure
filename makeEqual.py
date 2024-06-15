import math
# Add any extra import statements you may need here
# Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.


def are_they_equal(array_a, array_b):
  # Write your code here
  if len(array_a) != len(array_b):
    return False
  if sorted(array_a) != sorted(array_b):
    return False
  start = 0
  end = len(array_a) - 1
  while start < end and array_a[start] == array_b[start]:
    start += 1
  while end > start and array_a[end] == array_b[end]:
    end -= 1
  if start >= end:
    return True
  substring_a = array_a[start:end+1]
  substring_b = array_b[start:end+1]
  if substring_a == substring_b[::-1]:
    return True

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
