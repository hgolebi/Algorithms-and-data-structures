from algorytm_KMP import KMP_find
import algorytm_naiwny
from random import randint
from random import choice

def test_standard():
    results = KMP_find('abc', '***abc****')
    assert results == [3]

def test_few_occurances():
    results = KMP_find('abc', '*abc**abc***abc***')
    assert results == [1, 6, 12]

def test_empty_text():
    assert KMP_find('abc', '') == "Empty pattern or text"

def test_empty_pattern():
    assert KMP_find('', 'asdasd') == "Empty pattern or text"

def test_both_empty():
    assert KMP_find('', '') == "Empty pattern or text"

def test_no_occurances():
    assert KMP_find('abc', 'qwerty') == "Pattern not in the text"

def test_pattern_longer_than_txt():
    assert KMP_find('abcd', 'abc') == "Pattern longer than text"

def test_pattern_the_same_as_txt():
    results = KMP_find('abc', 'abc')
    assert len(results) == 1
    assert results[0] == 0

def test_random_pattern_and_text_searching():
    for i in range(10):
        alphabet = "AaBb"
        # losowy text 50-znakowy
        txt = "".join(choice(alphabet) for i in range(50))
        # losowy pattern o losowej dlugosci (1-50)
        pat_len = randint(1, 50)
        pat = "".join(choice(alphabet) for i in range(pat_len))

        naive = algorytm_naiwny.find(pat, txt)
        kmp = KMP_find(pat, txt)
        assert kmp == naive
