import sys
from unidecode import unidecode

def file_read(file_name):
    document_text = str()

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            document_text = document_text + line.strip().lower()

    return document_text

def char_freq(text):
    count_number = dict()

    for character in unidecode(text):
        if character.isalpha():
            count_number[character] = count_number.get(character, 0) + 1
        else:
            continue

    return count_number

def main():
    try:
        name = sys.argv[1]
    except IndexError:
        print("Please enter a file name as argument.")
        sys.exit()

    final_result = list()
    text = file_read(name)
    char_numbers = char_freq(text)

    for char, num in char_numbers.items():
        final_result.append((num, char))

    for a, b in sorted(final_result, reverse=True):
        print(f"{b}: {a:,}")

if __name__ == "__main__":
    main()
