def count_letters(my_text):
    my_text_lower = my_text.lower()

    all_characters = ''.join(set(my_text_lower))
    only_letters = ''.join(filter(str.isalpha, all_characters))
    
    letters_by_total = {}

    for i in range(0, len(only_letters)):
        letter = only_letters[i]
        total_appearances = my_text_lower.count(letter)
        letters_by_total[letter] = total_appearances
    
    return letters_by_total

file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_content = f.read()
    words = file_content.split()
    total_words = len(words)
    total_letters = count_letters(file_content)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")

    for letter in total_letters:
        print(f"The '{letter}' character was found {total_letters[letter]} times")
    
    print("--- End report ---")
