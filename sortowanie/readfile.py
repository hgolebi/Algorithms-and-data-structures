def GetWordsList(file_address, bytes):

    allowed_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM \t\n"

    file = open(file_address, 'r')
    text = file.read(bytes)
    text = text.lower()
    for char in text:
        if char not in allowed_chars:
            text = text.replace(char, "")
    words_list = text.split()
    return words_list


