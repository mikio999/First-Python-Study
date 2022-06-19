def leap(start, end):
    leap_list = []
    for x in range(start, end+1):
        if (x%4 == 0 and x%100 !=0) or (x%400==0):
            leap_list.append(x)
        return leap_list
print("leap year:", leap(2021, 2050))
print("leap year:", leap(2051, 2080))

leap = lambda start, end : [x for x in range(start, end + 1) if ((x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)) ]
print("leap year:", leap(2021, 2050))
print("leap year:", leap(2051, 2080))

leap = lambda start, end : [x if ((x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)) else 0 for x in range(start, end + 1) ]
print("leap year:", leap(2021, 2050))
print("leap year:", leap(2051, 2080))

