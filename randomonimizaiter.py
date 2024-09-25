def write_file(path, text):
    with open(path, "a") as z:
        z.write(str(text) + "\n")
def clear_file(path):
    with open(path, "w") as z:
        z.write("")
from random import randint
from time import time
print("randomonimizaiter v1.4 by m1cro_cat")
mx = 0
mn = 0
total = 0
test = True 
RepeatOff = False
numbs = []
a = int(input("Введите 1, чтобы включить RepeatOff™ (отключение повтора цифр), или же 0 чтобы отключить: "))
if a == 1:
    RepeatOff = True
elif a == 0:
    RepeatOff = False
else:
    print("error!")
count = int(input("Введите, сколько чисел будет генерироваться: "))
count2 = int(input("Введите, до скольки чисел будет генерироваться (от 1 до ..): "))
start_time = time()
for _ in range(count):
        i = randint(1, count2)
        if RepeatOff:
            if i in numbs:
                while i in numbs: 
                    i = randint(1, count2)
        if i > mx:
            mx = i
            if test == True:
                mn = mx
                test = False
        if i < mn:
            mn = i
        total += i
        numbs.append(i)
numbs.sort(reverse=True)
clear_file("test.txt")
end_time = time()
for i in numbs:
    print(i)
    write_file("test.txt", i)
print("общее количество - ", count)
print("максимальное - ",mx)
print("минимальное -",mn)
print("среднее число -", int(total / count))
print("медиана -", numbs[count//2])
print("размах -", numbs[0] - numbs[count - 1])
print("время -", round(end_time - start_time, 3))
