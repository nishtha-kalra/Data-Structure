
'''
Question:
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
'''

'''
  1.	ord(char):
	•	The ord() function returns the Unicode code point (an integer) for the character char.
	•	For example, ord('a') returns 97.
	2.	ord(‘a’):
	•	This is the Unicode code point for the character 'a', which is 97.
	3.	ord(char) - ord(‘a’):
	•	This converts the Unicode code point of char to a zero-based index relative to 'a'.
	•	For example, for char = 'c', ord('c') - ord('a') becomes 99 - 97 = 2.
	4.	(ord(char) - ord(‘a’) + rotation_factor):
	•	This adds the rotation factor to the zero-based index.
	•	For example, if char = 'c' and rotation_factor = 3, it becomes 2 + 3 = 5.
	5.	% 26:
	•	This ensures that the result wraps around within the range of lowercase letters (0-25).
	•	For example, if the calculated value exceeds 25, it wraps around. If char = 'y' and rotation_factor = 5, (24 + 5) % 26 becomes 29 % 26 = 3.
	6.	+ ord(‘a’):
	•	This converts the zero-based index back to a Unicode code point relative to 'a'.
	•	For example, if the result is 5, 5 + ord('a') becomes 5 + 97 = 102, which is the Unicode code point for 'f'.
	7.	chr(…):
	•	The chr() function converts the Unicode code point back to a character.
	•	For example, chr(102) returns 'f'.
'''
def rotationalCipher(input, rotation_factor):
  print(input)
  # Write your code here
  rotate = []
  for i in input:
    if i.isdigit():
      rotate.append(str((int(i)+rotation_factor) % 10))
    elif i.isupper():
      rotate.append(chr(((ord(i) - ord('A') + rotation_factor) % 26) + ord('A')))
    elif i.islower():
      rotate.append(chr(((ord(i) - ord('a') + rotation_factor) % 26) + ord('a')))
    else:
      rotate.append(i)
  return (''.join(rotate))
    

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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
