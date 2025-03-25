from number_filter import is_even , even_numbers, odd_numbers

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

def test_even_numbers():
    input_data = [1,2,3,4,5,6,7,8,9]
    expected_output = [2,4,6,8]
    assert even_numbers (input_data) == expected_output

def test_odd_numbers():
    input_data = [1,2,3,4,5,6,7,8,9]
    expected_output = [1,3,5,7,9]
    assert odd_numbers(input_data) == expected_output

if __name__ == "__main__":
    test_is_even()
    test_even_numbers()
    test_odd_numbers()
    print("All tests passed.")
