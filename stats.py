def count_words(text):
    return len(text.split())

def count_letters(text):
    res = {}
    for char in text:
        if char.lower() not in res:
            res[char.lower()] = 1
        else:
            res[char.lower()] += 1
    return res

def sort_letters_dict(dict_to_sort):
    res = []
    for val in dict_to_sort:
        if val.isalpha():
            res.append({"char": val, "num": dict_to_sort[val]})
    res.sort(key=lambda x: x["num"], reverse=True)
    return res