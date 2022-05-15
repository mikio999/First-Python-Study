class Counter:
    __ncreated = 0
    def __init__(self, color = "balck", initValue = 0):
        self.__count = initValue
        self.__color = color
        Counter.__ncreated += 1
    def reset(self):
        self.__count = 0
    def increment(self):
        self.__count += 1
    def get(self):
        return self.__count
    def __init__(self, color = "balck", initValue = 0):
        self.__count = initValue
        self.__color = color
        Counter.__ncreated += 1
    def __str__(self):
        return f"count = {self.__count}, color = {self.__color}, ncreated = {Counter.__ncreated}"
a = Counter(100)
b = Counter()
print(a)