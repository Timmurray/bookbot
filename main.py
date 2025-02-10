def File(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def num_characters(file):
    char_counts = {}
    lower = File(file).lower()
    for char in lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def main():
    file = "books/frankenstein.txt"
    words = len(File(file).split())
    char_counts = num_characters(file)

    chars_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin Report of {file} ---")
    print(f"There are {words} words in the document\n")
    for char_info in chars_list:
        print(f"The letter '{char_info['char']}' was found {char_info['count']} times")
    print("--- End Report ---")

main()