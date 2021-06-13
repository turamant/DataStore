class MyDict(dict):
    def __getitem__(self, key):
        if not key in self:
            return -1
        return super(MyDict, self).__getitem__(key)


d = MyDict({'a': 12, 'b': 13})
print(d)
print(d['a'])
print(d['c'])

d2 = dict({'z': 1, 'x': 2})
print(d2.get('y', 89))
print(*d2)
