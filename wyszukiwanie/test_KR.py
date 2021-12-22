import algorytm_KR
import algorytm_naiwny
from random import randint
from random import choice

# przypadki brzegowe
def test_empty_string():
    result = algorytm_KR.find("", "")
    assert result == "Empty pattern or text"

def test_equal_pattern_and_text():
    result = algorytm_KR.find("sth", "sth")
    assert result == [0]

def test_pattern_longer_than_text():
    result = algorytm_KR.find("longer", "short")
    assert result == "Pattern longer than text"

def test_pattern_not_in_text():
    result = algorytm_KR.find("abc", "def")
    assert result == "Pattern not in the text"

# testowanie poprawnego wyszukiwania
def test_random_pattern_and_text_searching():
    for i in range(10):
        alphabet = "AaBb"
        # losowy text 50-znakowy
        txt = "".join(choice(alphabet) for i in range(50))
        # losowy pattern o losowej dlugosci (1-50)
        pat_len = randint(1, 50)
        pat = "".join(choice(alphabet) for i in range(pat_len))

        naive = algorytm_naiwny.find(pat, txt)
        kp = algorytm_KR.find(pat, txt, 2, 97)
        assert kp == naive
