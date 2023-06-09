import string

def convert_polish_signs_del_punc(file_address):

    polish_signs = {"ą": "a", "Ą": "A", "ć": "c", "Ć": "C",
                    "ę": "e", "Ę": "E", "ł": "l", "Ł": "L",
                    "ń": "n", "Ń": "N", "ó": "o", "Ó": "O",
                    "ś": "s", "Ś": "S", "ź": "z", "Ź": "Z",
                    "ż": "z", "Ż": "Z"}

    file = open(file_address, 'r', encoding='UTF-8')
    text = file.read()
    for char in text:
        if char in polish_signs:
            text = text.replace(char, polish_signs[char])
    
    not_allowed_chars = string.punctuation
    letters = list(text)
    for i in range(len(letters)):
        if letters[i] in not_allowed_chars:
            letters[i]=""
    text = "".join(letters)

    file.close()

    with open(file_address, "w", encoding='UTF-8') as file:
        file.write(text)


def get_string(file_address, number_of_words=None):

    file = open(file_address, 'r')
    text = file.read()
    if number_of_words:
        text = text[:number_of_words]
    file.close()

    return text