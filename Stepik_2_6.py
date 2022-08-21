"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее
вместимость. """

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        self.v = v
        if self.v <= self.capacity:
            return True
        elif self.v > self.capacity:
            return False

    def add(self, v):
        self.capacity -= v if self.can_add(True) else None


"""
x = MoneyBox(15)
print(x.can_add(3))
x.add(3)
print(x.can_add(4))
x.add(4)
print(x.capacity)
"""
