def find(pat, txt):
    pat_len = len(pat)
    txt_len = len(txt)
    occurences_list = []
    for i in range(txt_len-pat_len+1):
        for j in range(pat_len):
            if txt[i+j] != pat[j]:
                j = 0
                break
        if(j != 0):
            occurences_list.append(i)
    if occurences_list:
        return occurences_list
    return "Pattern not in text"