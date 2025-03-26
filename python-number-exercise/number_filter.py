def even_numbers(numbers):
    evens = [n for n in numbers if is_even(n)]
    return evens

def is_even(n):
    return n % 2 == 0

def odd_numbers(numbers):
    return [n for n in numbers if not is_even(n)]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # Optimized primality check
        if n % i == 0:
            return False
    return True

def prime_numbers(numbers):
    prime_num = [n for n in numbers if is_prime(n)]
    return prime_num

def odd_prime_numbers(numbers):
    odd_nums = odd_numbers(numbers)  # Corrected variable name
    prime_odd_numbers = [num for num in odd_nums if is_prime(num)]
    return prime_odd_numbers

if __name__ == "__main__":
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_result = even_numbers(sample_input)
    odd_result = odd_numbers(sample_input)
    prime_result = prime_numbers(sample_input)
    odd_prime_result = odd_prime_numbers(sample_input)
    print("Even Numbers:", even_result)
    print("Odd Numbers:", odd_result)
    print("Prime Numbers:", prime_result)
    print("Odd Prime Numbers:", odd_prime_result)


# Use input as array of numbers instead of comma separated string input
# Write a python test case for this
# DRY princple in programming (Don't Repeat Yourself)
# odd number function should have only one line (hint: it should REUSE even number implementation)