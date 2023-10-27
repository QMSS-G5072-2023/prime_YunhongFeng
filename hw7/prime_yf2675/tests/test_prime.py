# Contents of test_prime.py
import math	
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def test_is_prime():

    prime_numbers = [2, 3, 5, 7, 11]
    for prime in prime_numbers:
        assert is_prime(prime) == True, f"Test failed with {prime}"
    
    composite_numbers = [4, 6, 8, 9, 10]
    for composite in composite_numbers:
        assert is_prime(composite) == False, f"Test failed with {composite}"
    
    assert is_prime(0) == False, "Test failed with 0"
    assert is_prime(1) == False, "Test failed with 1"
    assert is_prime(-5) == False, "Test failed with -5"

@pytest.mark.parametrize(
    "number, expected", 
    [(2, True),  (3, True),  (4, False),  (5, True),  (6, False), (7, True),  (8, False),  (9, False),  (10, False),  (0, False),  (1, False), 
        (-5, False), ])
def test_is_prime_param(number, expected):
    assert is_prime(number) == expected, f"Test failed with {number}"



def test_generate_primes():
    assert generate_primes(10) == [2, 3, 5, 7], "Test failed with limit 10"
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Test failed with limit 20"

    assert generate_primes(0) == [], "Test failed with limit 0"
    assert generate_primes(1) == [], "Test failed with limit 1"
    assert generate_primes(-5) == [], "Test failed with limit -5"
    assert generate_primes(2) == [2], "Test failed with limit 2"

    assert generate_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test failed with limit 30"
    

def test_prime_integration():
    limit = 30
    prime_list = generate_primes(limit)
    
    for prime in prime_list:
        assert is_prime(prime) == True, f"Test failed with {prime}"
    
    for i in range(2, limit + 1):
        if i not in prime_list:
            assert is_prime(i) == False, f"Test failed with {i}, false negative"