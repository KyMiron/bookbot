def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_list = count_characters(text)
    print()
    for char in character_list:
        print(f"The '{char}' character was found {character_list[char]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characters = {}
    lower_text = text.lower()
    wordSplit = lower_text.split()
    for word in wordSplit:
        split_word = list(word)
        for char in split_word:
            if char.isalpha():
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
    return characters

main()
