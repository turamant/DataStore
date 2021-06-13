class IndexDict(dict):
    def __getitem__(self, key):
        if isinstance(key ,int):
            return list(self.items())[key]
        else:
            return super(IndexDict, self).__getitem__(key)




d = IndexDict({'a':22, 'b': 24, 12: 7, 67:8,90:0})
print(d['a'])
print(d[2],d[3], d[4])