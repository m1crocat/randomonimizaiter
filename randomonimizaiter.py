def write_file(path, text):
    with open(path, "a") as z:
        z.write(str(text) + "\n")
from random import randint
from time import time
mx = 0
mn = 0
total = 0
count = int(input("Введите, сколько чисел будет генерироваться: "))
count2 = int(input("Введите, до скольки чисел будет генерироваться (от 1 до ..): "))
lst = []
test = True 
start_time = time()
for _ in range(count):
        i = randint(1, count2)
        if i in lst:
            while i in lst: 
                i = randint(1, count2)
        if i > mx:
            mx = i
            if test == True:
                mn = mx
                test = False
        if i < mn:
            mn = i
        total += i
        lst.append(i)
lst.sort(reverse=True)
end_time = time()
for i in lst:
    print(i)
    write_file("test.txt", i)
print("общее количество - ", count)
print("максимальное - ",mx)
print("минимальное -",mn)
print("среднее число -", int(total / count))
print("время -", round(end_time - start_time, 4))
