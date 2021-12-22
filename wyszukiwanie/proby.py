from math import pow
# d is the number of characters in the input alphabet
d = 256
  
# pat  -> pattern
# txt  -> text
# q    -> A prime number
  
def find(pat, txt, q=997):
    M = len(pat)
    N = len(txt)
    #i = 0
    #j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = (pow(d, M-1))%q
    occurrences_list = []
  
    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p += (ord(pat[i]))%q
        t += (ord(txt[i]))%q

    for i in range(N-M+1):
        # if the hash values match check for characters one by one
        if p==t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else: j+=1
  
            if j==M:
                occurrences_list.append(i)
                print("Pattern found at index " + str(i))
  
        # hash value for next window of text
        # remove first digit, add next one
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
  
            # if negative
            if t < 0:
                t = t+q
  
# Driver Code
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
  
# A prime number
q = 101 
  
# Function Call
find(pat,txt)