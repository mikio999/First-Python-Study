# counter class
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

a = Counter()
a.increment()
print("카운터의 값 = ", a.count)

# Default argument
def greet(name, msg="별일없죠?"):
    print("안녕",name+',',msg)
greet("영희")

# 하나의 클래스로 객체는 많이 만들 수 있다.
class Counter:
    def __init__(self, initValue = 0):
        self.count = initValue
    def increment(self):
        self.count += 1
a = Counter(0)
b = Counter(100)
print(a,b)