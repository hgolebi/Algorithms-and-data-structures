# pat - pattern
# txt - text

def find(pat, txt):
    if(pat=="" or txt==""):
        return "Empty pattern or text"
    if(len(pat)>len(txt)):
        return "Pattern longer than text"
    pat_len = len(pat)
    txt_len = len(txt)
    occurrences_list = []
    for i in range(txt_len-pat_len+1):
        for j in range(pat_len):
            if txt[i+j] != pat[j]:
                break
            else:
                j += 1
        if(j == pat_len):
            occurrences_list.append(i)
    if occurrences_list:
        return occurrences_list
    return "Pattern not in the text"