def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wcount = word_count(file_contents)
    ccount = char_count(file_contents)
    sorte = sorted_list(ccount)
    print("--- Begin report of Frankenstein ---")
    print(f"{wcount} words found in the document")
    for item in sorte:
        if not item["c"].isalpha():
            continue
        print(f"The '{item['c']}' character was found {item['n']} times")

    print("--- End report ---")

def word_count (file):
    words = file.split()
    return len(words)

def char_count (file):
    low_file = file.lower()
    count_letters = {}
    for c in low_file:
        if c not in count_letters:
            count_letters[c] = 1
        else:
            count_letters[c] += 1
    return count_letters

def sort_on(dict):
    return dict["n"]
    
def sorted_list(dict):
    listd = []
    for i in dict:
        listd.append({"c": i, "n": dict[i]})
    listd.sort(reverse=True, key=sort_on)
    return listd

main()