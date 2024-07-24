# Task 1

def check_unique_elements(lst):
    return len(set(lst)) == len(lst)

my_list = [1, 2, 3, 4, 5]
print(check_unique_elements(my_list))

my_list_with_duplicates = [1, 3, 3, 5, 7]
print(check_unique_elements(my_list_with_duplicates))


# Task 2

def count_unique_elements(elements):
    unique_elements = set(elements)
    return len(unique_elements)

# Eample

my_list = [1, 2, 5, 2, 4, 5, 1, 66, 7, 11, 9, 1]
unique_count = count_unique_elements(my_list)
print(f"Number of unique elements: {unique_count}")



# Task 3

def check_unique_values(dictionary):
    values = list(dictionary.values())

    if len(values) == len(set(values)):
        return True
    else:
        return False

my_dict = {'a': 10, 'b': -3.14, 'c': 256}
print(check_unique_values(my_dict))

my_dict = {'a': 1, 'b': 2, 'c': 1}
print(check_unique_values(my_dict))


# Task 5

def find_longest_common_word(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    common_words = sorted(words1.intersection(words2), key=len, reverse=True)

    return common_words[0] if common_words else ""


line1 = "We could be better, but we are what we are."
line2 = "We could be better, but we don't do anything about it."

longest_common_word = find_longest_common_word(line1, line2)
print("The longest common word:", longest_common_word)