def get_string(file_address, number_of_words=None):

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
    if number_of_words:
        del text[number_of_words:]
    file.close()

    return text