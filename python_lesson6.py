# Task 1
name = input("Enter your name: ")
res = 'Valid' if name.istitle() and name.replace(' ', '').isalpha() else 'Invalid name'
print(res)


# Task 2
text = input("Enter a text: ").lower()
print(text.count('b'))


# Task 3
text = input("Enter a text: ")
s = 0
for item in text:
    s += ord(item)
print(s)

print(sum(ord(item) for item in text))


# Task 4
import math

for i in range(2, 10):
    print(f'{math.pi:.{i}f}')


# Task 5
import string
text = input("Enter a text: ").lower()
for item in string.punctuation:
    text = text.replace(item, ' ')
text = text.split()

max_word = text[0]
for item in text:
    if len(item) > len(max_word):
        max_word = item
print(max_word)


print(max(text, key=len))

print(max(text, key=lambda item: item.count('b')))


# Task 7

def find_shortest_repeating_word(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            substring = s[:length]
            if substring * (n // length) == s:
                return substring
    return s
print(find_shortest_repeating_word("aaaaaaa"))
print(find_shortest_repeating_word("ititititit"))
print(find_shortest_repeating_word("catcatcatcat"))