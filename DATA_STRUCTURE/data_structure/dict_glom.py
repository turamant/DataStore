# pip install glom
from glom import glom

data = {'a': {'b': {'c': 'd'}}}
data2 = {'a': {'b': None}}

print(data['a']['b']['c'])
#print(data2['a']['b']['c']) # TypeError: 'NoneType' object is not subscriptable

print(glom(data, 'a.b.c'))
#print(glom(data2, 'a.b.c'))#could not access 'c', index 2 in path Path('a', 'b', 'c'), got error
