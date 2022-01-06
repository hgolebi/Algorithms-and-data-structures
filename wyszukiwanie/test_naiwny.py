import algorytm_naiwny

# przypadki brzegowe
def test_empty_string():
    result = algorytm_naiwny.find("", "")
    assert result == "Empty pattern or text"

def test_equal_pattern_and_text():
    result = algorytm_naiwny.find("sth", "sth")
    assert result == [0]

def test_pattern_longer_than_text():
    result = algorytm_naiwny.find("longer", "short")
    assert result == "Pattern longer than text"

def test_pattern_not_in_text():
    result = algorytm_naiwny.find("abc", "def")
    assert result == "Pattern not in the text"

# kilka testow poprawnego wyszukiwania
def test_few_datasets_checking_correctness():
    result = algorytm_naiwny.find("abcd", "abcabcabcdaaaaabcd")
    assert result == [6, 14]
    result = algorytm_naiwny.find("aaa", "aaaaaaaaaaaa")
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = algorytm_naiwny.find("ABC", "abcd")
    assert result == "Pattern not in the text"
    result = algorytm_naiwny.find("zzx", "zzzzzxabzzxg")
    assert result == [3, 8]