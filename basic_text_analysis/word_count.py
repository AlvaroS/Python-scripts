import sys

def count(file_name):
    text = str()

    with open(file_name, encoding="utf-8") as file:
        for line_num, line in enumerate(file):
            text = text + line

    for char_num, char in enumerate(text):
        pass

    words_num = len(text.split())

    return line_num, words_num, char_num

def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Please enter file name as argument.")
        sys.exit()

    line_number, words_number, char_number = count(file_name)

    print(f"Number of lines: {line_number:,}\n"
          f"Number of words: {words_number:,}\n"
          f"Number of characters: {char_number:,}")

if __name__ == "__main__":
    main()
