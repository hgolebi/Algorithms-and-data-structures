def GetWordsList(file_address, number):

    allowed_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM \t\n"

    file = open(file_address, 'r')
    text = file.read()
    text = text.lower()
    for char in text:
        if char not in allowed_chars:
            text = text.replace(char, "")
    words_list = text.split()
    del words_list[number:]
    file.close()
    
    return words_list


