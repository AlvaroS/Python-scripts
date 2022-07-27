import sys

def check_if_letter(text):
    not_letters_list = list()

    for character in text:
        if not character.isalpha() and character not in not_letters_list:
            not_letters_list.append(character)

    return not_letters_list

def text_formater(file_name):
    text_string = str()
    words_in_list = list()

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if line.isspace():
                continue
            else:
                text_string = text_string + line.lstrip().lower()

    characters_to_replace = check_if_letter(text_string)

    for element in characters_to_replace:
        text_string = text_string.replace(element, ' ')

    words_in_list = text_string.split()

    return words_in_list

def word_freq(words):
    word_freq_dict = dict()

    for word in words:
        word_freq_dict[word] = word_freq_dict.get(word, 0) + 1

    return word_freq_dict

def main():
    words_and_value = list()

    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Please enter file name as argument')
        sys.exit()

    words_in_file = text_formater(file_name)
    freq_dictionary = word_freq(words_in_file)

    for value, key in freq_dictionary.items():
        words_and_value.append((key, value))

    for count, word in sorted(words_and_value, reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
