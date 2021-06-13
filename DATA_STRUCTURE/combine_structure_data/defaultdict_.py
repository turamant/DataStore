from collections import defaultdict


def greet(name):
    return "hi " + name + "!"

food_list = "ham ham ham bread"
food_count = defaultdict(lambda: 0)
print(food_count)
for food in food_list.split(" "):
    food_count[food] += 1

print(food_count)
print(dict(food_count))

greeter = defaultdict(lambda :greet)
print(greeter)
print(greeter["defaultdict"]("John"))
print(greeter["John"]("Smith"))