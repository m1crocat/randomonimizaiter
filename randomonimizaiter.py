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
a = int(input("введите 1, чтобы включить RepeatOff™ (отключение повтора цифр), или же 0 чтобы отключить\nучтите, что при работе с большими числами это очень замедляет работу: "))
if a == 1:
    RepeatOff = True
elif a == 0:
    RepeatOff = False
else:
    print("error!")
hello = int(input("1 - генерация\n2 - бенчмарк\n"))
if hello == 1:
    count = int(input("введите, сколько чисел будет генерироваться: "))
    count2 = int(input("введите, до скольки чисел будет генерироваться (от 1 до ..): "))
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
elif hello == 2:
    input("этот бенчмарк покажет производительность вашего ПК в вычислениях. нажмите enter чтобы начать: ")
    start_time = time()
    bench = 0
    for _ in range(3):
        for _ in range(50000):
                i = randint(1, 100000)
                if RepeatOff:
                    if i in numbs:
                        while i in numbs: 
                            i = randint(1, 200000)
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
        end_time = time()
        bench += end_time - start_time
    print("результат -", round(bench / 3 , 4) , ", RepeatOff™ -", RepeatOff)