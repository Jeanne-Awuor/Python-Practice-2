#print the numbers from 1 to 50 using a for loop
#For numbers that are divisible by 3, print "Fizz" instead of the number,
# and for numbers divisible by 5, print "Buzz".
# For numbers divisible by both, print "FizzBuzz

for x in range (1,51):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
