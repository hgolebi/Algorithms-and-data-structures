def create_DFA(pat, print_flag=False):
    if pat == None:
        return
    dfa = {}
    for let in pat:
        if let not in dfa:
            dfa[let] = [0 for l in pat]
    dfa[pat[0]][0] = 1
    x = 0
    for j in range(1, len(pat)):
        for elem in dfa:
            dfa[elem][j] = dfa[elem][x]
        dfa[pat[j]][j] = j+1
        x = dfa[pat[j]][x]
    if print_flag is True:
        for elem in dfa:
            print(elem, dfa[elem])
    return dfa

def KMP_find(pattern, txt):
    if(pattern=="" or txt==""):
        return "Empty pattern or text"
    if(len(pattern)>len(txt)):
        return "Pattern longer than text"
    dfa = create_DFA(pattern)
    occurances = []
    j = 0
    for i in range(0, len(txt)):
        if txt[i] not in dfa:
            j = 0
        else:
            j = dfa[txt[i]][j]
            if j >= len(pattern):
                occurances.append(i-len(pattern)+1)
                j = 0
    if occurances:
        return occurances
    else:
        return "Pattern not in the text"

