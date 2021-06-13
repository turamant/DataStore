class FiFO:
    """
    Очередь
    """
    def __init__(self):
        self.queue = []

    def put(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop(0)

class FiLO:
    """
    Стек
    """
    def __init__(self):
        self.queue = []

    def put(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop(-1)



fifo = FiFO()
fifo.put(1)
fifo.put(2)
print(fifo.get())
print(fifo.get())

print('*'*15)
filo = FiLO()
filo.put(1)
filo.put(2)
print(filo.get())
print(filo.get())