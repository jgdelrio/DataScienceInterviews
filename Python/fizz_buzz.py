"""
Write in python a function to implement the game "Fizz Buzz".
Using a list of numbers that counts from 1 to 100, print each number in turn on a new line
replacing the number on the following cases:
   - If the number is divisible by 3 or contains a digit 3, print "Fizz" instead of the number.
   - If the number is divisible by 5, print "Buzz".
   - If both previous conditions are met, print "Fizz Buzz".
"""


def fizz_buzz(n=100):
    for i in range(1, n+1):
        txt = []
        if i % 3 == 0:
            txt.append('Fizz')
        if i % 5 == 0:
            txt.append('Buzz')

        if txt:
            print(' '.join(txt))
        else:
            print(i)
