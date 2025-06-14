from curses.ascii import isalpha


def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
    
    word_list = file_contents.split()
    count = 0
    for word in word_list:
        count += 1

    print(f"Found {count} total words")


def sort_on(dict):
    return dict["num"]


def character_count(path):
    with open(path) as f:
        file_contents = f.read()

    char_count = {}
    char_count_list = []
    final_list = []
    for i in file_contents.lower():
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for j in char_count:
        char_count_list.append({"name": j, "num": char_count[j]})

    char_count_list.sort(reverse=True, key=sort_on)

    for i in char_count_list:
        if i['name'].isalpha():
            print(f"{i['name']}: {i['num']}")

    
    #print(char_count_list)