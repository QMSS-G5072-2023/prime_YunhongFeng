import sys
sys.path.append("/Users/mcbookpro/prime_yf2675")

from src.prime_yf2675.prime_yf2675 import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(11) == True
    assert is_prime(4) == False
    assert is_prime(12) == False