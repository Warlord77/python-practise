def even_numbers(numbers):
    even_numbers = [n for n in numbers if is_even(n)]
    return even_numbers

def is_even(n):
    return n%2==0

def odd_numbers(numbers):
    return [n for n in numbers if not is_even(n)]

# Usage
sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_numbers(sample_input)
odd_numbers = odd_numbers(sample_input)
print("Even Numbers:", even_numbers)
print ("Odd Numbers:", odd_numbers)

# Use input as array of numbers instead of comma separated string input
# Write a python test case for this
# DRY princple in programming (Don't Repeat Yourself)
# odd number function should have only one line (hint: it should REUSE even number implementation)



