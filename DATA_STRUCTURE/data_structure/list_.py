class MyList(list):
    def __getitem__(self, key):
        if key >= len(self):
            return 'no such index'
        super(MyList, self).__getitem__(key)

    def __setitem__(self, key, value):
        if key >= len(self):
            self.append(value)
        else:
            super(MyList, self).__setitem__(key, value)

class TypedList(list):
    def __init__(self, iterable=None, data_type=None):
        super(TypedList, self).__init__(iterable)
        self.data_type = data_type
        if self.data_type is None and iterable:
            self.data_type = type(iterable[0])
        for value in iterable:
            if not isinstance(value, self.data_type):
                raise ValueError("Only type needed")

    def append(self, value):
        if not isinstance(value, self.data_type):
            raise ValueError("Only type needed")
        super(TypedList, self).append(value)




ml = MyList([31,4,7])
print(ml[20])
ml[0] = 10
print(ml)
print('*'*12)

a = TypedList([1, 3, 9])
print(a)
b = TypedList("fg")
print(b)
b.append("l")
print(b)
b.append("34")
print(b)