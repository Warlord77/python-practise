def get_even_numbers(input_string):
    numbers_list = input_string.split(",")
    even_numbers = []
    for num in numbers_list:
        if int(num.strip()) % 2 == 0:
            even_numbers.append(int(num.strip()))
    result = ", ".join(str(x) for x in even_numbers)
    return result

def get_odd_numbers(input_string):
    numbers_list = input_string.split(",")
    odd_numbers = []
    for num in numbers_list:
        if int(num.strip()) % 2 != 0:
            odd_numbers.append(int(num.strip()))
    result = ",".join(str(x) for x in odd_numbers)
    return result

#Usage
sample_input = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
sample_output = get_even_numbers(sample_input)
sample_output2 = get_odd_numbers(sample_input)
print("Sample Output:", sample_output)
print ( "Sample Output:", sample_output2 )


