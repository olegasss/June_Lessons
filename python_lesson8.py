# Task 1
import random
x = [random.randint(1, 100) for _ in range(10)]
res = 'Unique' if len(set(x)) == len(x) else 'Not unique'
print(res)
print(x)

# Task 2
x = [random.randint(1, 10) for _ in range(10)]
count = 0
for item in x:
    if x.count(item) == 1:
        count += 1
print(count)
print(x)

res = {item for item in x if x.count(item) == 1}
print(len(res))

# Task 3
x = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'one', 7: 'two'}
res = 'Unique' if len(set(x.values())) == len(x) else 'Not unique'
print(res)

# Task 4
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}

user_1 = input('Enter user1: ')
user_2 = input('Enter user2: ')

friends_1 = friendships.get(user_1, set())
friends_2 = friendships.get(user_2, set())

mutual_friends = friends_1 & friends_2
mutual_friends = mutual_friends or 'No mutual friends'

print(mutual_friends)


users = []
for _ in range(10):
    user = input('Enter user: ')
    users.append(friendships.get(user, set()))

mutual_friends = set.intersection(*users)


# Task 5
import string
text_1 = 'Hello, my name is John'
text_2 = 'Hello, my dear friend'

for item in string.punctuation:
    text_1 = text_1.replace(item, ' ')
    text_2 = text_2.replace(item, ' ')

text_1 = set(text_1.lower().split())
text_2 = set(text_2.lower().split())

common_words = text_1 & text_2
print(max(common_words, key=len))
