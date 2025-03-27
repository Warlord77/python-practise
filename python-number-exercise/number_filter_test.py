from number_filter import is_even , even_numbers, odd_numbers, prime_numbers, odd_prime_numbers, multiple_five_even ,  od_multi3_gr10 , od_grt5_mul3, ev_les15_mul3, prime_grt15_mul5, less_6mul3

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
    assert odd_numbers (input_data) == expected_output

def test_prime_numbers():
    input_data = [1,2,3,4,5,6,7,8,9,10]
    expected_output = [2,3,5,7]
    assert prime_numbers(input_data) == expected_output 

def test_odd_prime_numbers():
    input_data = [1,2,3,4,5,6,7,8,9,10]
    expected_output = [ 3, 5, 7]
    assert odd_prime_numbers(input_data) == expected_output


def test_multiple_five_even():
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = [10, 20]
    assert multiple_five_even(input_data) == expected_output

def test_od_multi3_gr10():
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = [15]
    assert od_multi3_gr10(input_data) == expected_output

def test_od_grt5_mul3():
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = [9, 15]
    assert od_grt5_mul3(input_data) == expected_output

def test_ev_les15_mul3():
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = [6, 12]
    assert ev_les15_mul3(input_data) == expected_output

def test_prime_grt15_mul5():
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = [2, 3, 5, 7, 10, 11, 13, 15, 16, 17, 18, 19, 20]
    assert prime_grt15_mul5(input_data) == expected_output

def test_less_6mul3():
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = [1, 2, 3, 4, 5, 6, 9, 12, 15, 18]
    assert less_6mul3(input_data) == expected_output




if __name__ == "__main__":
    test_is_even()
    test_even_numbers()
    test_odd_numbers()
    test_prime_numbers()
    test_odd_prime_numbers()
    test_multiple_five_even()
    test_od_multi3_gr10()
    test_od_grt5_mul3()
    test_ev_les15_mul3()
    test_prime_grt15_mul5()
    test_less_6mul3()



    print("All tests passed.")
