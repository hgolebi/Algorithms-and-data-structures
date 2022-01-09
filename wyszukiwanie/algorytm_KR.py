from math import pow
# d   - number of characters in the input alphabet
# pat - pattern
# txt - text
# q   - prime number
  
def find(pat, txt, d=256, q=997):
    if(pat=="" or txt==""):
        return "Empty pattern or text"
    if(len(pat)>len(txt)):
        return "Pattern longer than text"

    M = len(pat)
    N = len(txt)
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
    occurrences_list = []

    for i in range(M-1):
        h = (h*d) % q
  
    # hash value of pattern and first window of text
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q

    for i in range(N-M+1):
        # if the hash values match check for characters one by one
        if p==t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
            j+=1
            if j==M:
                occurrences_list.append(i)
  
        # hash value for next window of text
        # remove first digit, add next one
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
  
            # if negative
            if t < 0:
                t = t+q

    if occurrences_list:
        return occurrences_list
    return "Pattern not in the text"