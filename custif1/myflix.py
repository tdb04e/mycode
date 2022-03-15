#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'based off of your numerical score, you recieved a '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your numerical grade?"))

# if input value was higher or equal to 90
if connection >= 90:
    message = message + 'your grade is an A.'
elif connection >= 80:
    message = message + 'your grade is a B.'
elif connection >= 70:
    message = message + 'your grade is a C.'
elif connection >= 60:
    message = message + 'your grade is a D.'
else:
    message = message + 'your grade is an F.'
print(message)

