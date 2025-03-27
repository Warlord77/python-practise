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
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

def prime_numbers(numbers):
    prime_num = [n for n in numbers if is_prime(n)]
    return prime_num

def odd_prime_numbers(numbers):
    odd_nums = odd_numbers(numbers) 
    prime_odd_numbers = [num for num in odd_nums if is_prime(num)]
    return prime_odd_numbers

def multiple(n,p):
    return n % p == 0

def multiple_five_even(numbers):
    even_nums = even_numbers(numbers)
    muleven = [num for num in even_nums if multiple(num,5)]
    return muleven

def great(n,p):
    return n > p

#odd and multiples of 3 greater than 10    
def od_multi3_gr10(numbers):
    odd_nums =  odd_numbers(numbers)
    mul3  = [num for num in odd_nums if multiple(num,3)]
    grt10 = [num for num in mul3 if great(num,10)]
    return grt10


#Conditions specified using a set of functions: odd, greater than 5, multiple of 3
def od_grt5_mul3(numbers):
    odd_nums = odd_numbers(numbers)
    grt5 = [num for num in odd_nums if great(num,5)]
    mul3 = [num for num in grt5 if multiple(num,3)]
    return mul3

def less(n,p):
    return n < p

#Conditions specified using a set of functions: even, less than 15, multiple of 3
def ev_les15_mul3(numbers):
    even_nums = even_numbers(numbers)
    les15 = [num for num in even_nums if less(num,15)]
    mul3 =  [num for num in les15 if multiple(num,3)]
    return mul3

#Conditions specified using a set of functions: prime, greater than 15, multiple of 5
def prime_grt15_mul5(numbers):
    prnum = prime_numbers(numbers)
    grt15 = [num for num in prnum if great(num,15)]
    #mul5 = [num for num in grt15 if multiple(num,5)]
    return grt15



if __name__ == "__main__":
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample_input2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    even_result = even_numbers(sample_input)
    odd_result = odd_numbers(sample_input)
    prime_result = prime_numbers(sample_input)
    odd_prime_result = odd_prime_numbers(sample_input)
    multiple_five_even = multiple_five_even(sample_input2)
    od_multi3_gr10 = od_multi3_gr10(sample_input2)
    od_grt5_mul3 = od_grt5_mul3(sample_input2)
    ev_les15_mul3 = ev_les15_mul3(sample_input2)
    prime_grt15_mul5 = prime_grt15_mul5(sample_input2)
    print("Even Numbers:", even_result)
    print("Odd Numbers:", odd_result)
    print("Prime Numbers:", prime_result)
    print("Odd Prime Numbers:", odd_prime_result)
    print("Multiple_five_even:", multiple_five_even)
    print("Multiple of 3 greater than 10", od_multi3_gr10 )
    print("Odd greater than 5 multiple of 3 ", od_grt5_mul3)
    print("Even less than 15 multiple of 3 ", ev_les15_mul3)
    print("Prime, greater than 15, multiple of 5", prime_grt15_mul5)


# Use input as array of numbers instead of comma separated string input
# Write a python test case for this
# DRY princple in programming (Don't Repeat Yourself)
# odd number function should have only one line (hint: it should REUSE even number implementation)