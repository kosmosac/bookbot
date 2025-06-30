def get_file_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_contents):
    return len(file_contents.split())

def get_num_letters(file_contents):
    num_letters = {}
    lowercase_content = file_contents.lower()
    for char in lowercase_content:
        try:
            num_letters[char] += 1
        except KeyError:
            num_letters[char] = 1
        except:
            raise Exception("FATAL")
    return num_letters

def sort_on(items):
    return items["num"]

def sort_num_letters(dict_num_letters):
    list_num_letters = []
    for key in dict_num_letters.keys():
        if key.isalpha():
            list_num_letters.append({ "char": key, "num": dict_num_letters[key] })
    list_num_letters.sort(reverse=True, key=sort_on)
    return list_num_letters
        


