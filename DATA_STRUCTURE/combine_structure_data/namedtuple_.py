from collections import namedtuple


user = namedtuple("User", "name age gender")
user1 = user(name='Serega', age=45, gender='male')
print(user1.name, user1.age, user1.gender)
print(user1[0], user1[1], user1[2])