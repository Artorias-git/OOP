import math
from datetime import datetime as dt
import tracemalloc

def statistick(funk):
    tracemalloc.start()
    st = dt.now()
    funk()
    print("Used memory (current, peak)")
    print(tracemalloc.get_traced_memory())
    print("Used time:")
    print((dt.now() - st).total_seconds())
    # The output is given in form of (current, peak),i.e, current memory is
    # the memory the code is currently using and peak memory is the
    # maximum space the program used while executing.
    tracemalloc.stop()

def inputer():
    while True:
        x = input("Enter a number: ")
        if x.isdigit():
            return int(x)
        else:
            print("Try again\n")
            continue

#Задача 1
def task1():
    a = 1
    b = 2
    c = 3
    arr = []   #можно и просто arr[a, b, c]
    arr.append(a)
    arr.append(b)
    arr.append(c)
    b = arr[2]
    c = arr[0]
    a = arr[1]
#Задача 2.1
def task21():
    # Задача 2.2
    print("First of all, input number of numbers ")
    N = inputer()
    print("Now input numbers")
    numbers = []
    for i in range(N):
        numbers.append(inputer())
    print("there your numbers:")
    print(numbers)
#Задача 3.1
def task31():
    print("enabled value(0 - 100)")
    while True:
        x = inputer()
        if x < 0 or x > 100:
            continue
        else:
            break
    x = 99
    result = x**5
    print(result)
#Задача 3.2
def task32():
    print("enabled value (0 - 100)")
    while True:
        x = inputer()
        if x < 0 or x > 100:
            print("Try again")
            continue
        else:
            break
    x = 99
    a = x
    for i in range(4):
        x = x * a
    print(x)
    print(a)
#Задача 4
def task4():
    print("enabled value (0 - 250)")
    while True:
        x = inputer()
        if x < 0 or x > 250:
            print("Try again")
            continue
        else:
            break
    if isFib(x):
        print("it's Fib")
    else:
        print("it isn't Fib")
def isFib(x):
    a = [1, 1]
    i = 1
    while a[i] < x:
        a.append(a[i-1]+a[i])
        i+=1
    return a[len(a)-1] == x
#Задача 5
def task5():
    print("enabled value (1 - 12)")
    x = dt(1900,inputer(),1)
    print(x.strftime("%B"))
#Задача 6
def task6():
    N = inputer()
    summ1 = 0
    summ2 = 0
    count1 = 0
    count2 = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            summ2 += i
            count2 += 1
        else:
            summ1 += i
            count1 += 1
    print(summ1)
    print(count1)
    print(summ2)
    print(count2)
#Задача 7

def num_div(val):
    count = 2  #cразу учтём 1 и val
    i = 2
    while i < math.sqrt(val):
        if val % i == 0:
            count += 2
        i += 1
    if (val % math.sqrt(val) == 0):
        count += 1
    return count

def task7():
    print("enabled value (1 - 250)")
    while True:
        N = inputer()
        if N < 1 or N > 250:
            print("Try again")
            continue
        else:
            break
    print("1 1")
    for i in range(2, N+1):
        print(i, num_div(i))
    #однако я не уверен в верности измерения времени
    #так как результат выводиться быстрее написоного
#Задача 8
def task8():
    print("range (N, M)")
    N = inputer()
    M = inputer()
    arr = []
    for i in range(N,M):
        for j in range(i+1, M+1):
            c = i**2 + j**2
            if math.sqrt(c) == round(math.sqrt(c)):
                c = round(math.sqrt(c))
                arr.append(i)
                arr.append(j)
                arr.append(c)
    for i in range(0, len(arr), 3):
        print(arr[i], arr[i + 1], arr[i + 2])
#Задача 9
def task9():
    print("range (N, M)")
    N = inputer()
    M = inputer()
    token = 0
    arr = []
    for i in range(N, M+1):
        s = str(i)
        a = 0
        while a < len(s) :
            if int(s[a]) == 0: # пропусаем 0
                a += 1
                continue
            if i % int(s[a]) != 0:
                token = 1
            a += 1
        if token == 0:
            arr.append(i)
        token = 0
    print(arr)
#Задача 10
def sum_div(val):
    i = 2
    sum = 1
    while i < math.sqrt(val):
        if val % i == 0:
            sum += i + val/i
        i += 1
    if (val % math.sqrt(val) == 0):
        sum += math.sqrt(val)
    return int(sum)

def task10():
    arr = []
    i = 2
    while True:
        if sum_div(i) == i:
            arr.append(i)
        if len(arr) == 4:
            print(arr)
            break
        i += 1
#Задача 11
def task11():
    arr = [1, 2, 3, 4]
    #способ 1
    print(arr[len(arr)-1])
    #способ 2
    print(arr[-1])
    #способ 3
    def last(arr):
        return arr[-1]
    print(last(arr))
    # я убрал проверку времени так как разница стремиться к 0
#Задача 12
def task12():
    arr = [1, 2, 3, 4]
    arr1 = arr[::-1]
    arr.reverse()
    print(arr)
    print(arr1)
#Задача 13
def task13():
    def sum(arr, N):
        if N <= 0:
            return 0
        else:
            return sum(arr, N - 1) + arr[N - 1]

    arr = [1, 2, 3, 4, 5]
    sss = sum (arr, len(arr))
    print(sss)
#Задача 14.1


#Задача 14.2


#Задача 15
def task15():
    while True:
        n = inputer()
        if n > 20 or n < 5:
            print("Try againe")
            continue
        else:
            break
    while True:
        m = inputer()
        if m > 20 or m < 5:
            print("Try againe")
            continue
        else:
            break

    table = []
    for i in range(1, n+1):
        arr = []
        for j in range(1, m+1):
            arr.append(i * j)
        table.append(arr)
    for i in range(len(table)):
        print(table[i])
#Задача 16
arr = [[0 for i in range(10)] for i in range(10)]
arr[0][0] = 1
arr[0][2] = 1
arr[0][4] = 1
arr[0][6] = 1

arr[6][3] = 4
arr[6][4] = 4
arr[6][5] = 4
arr[6][6] = 4

arr[2][0] = 2
arr[3][0] = 2

arr[3][5] = 2
arr[4][5] = 2

arr[8][8] = 2
arr[8][7] = 2

arr[9][0] = 3
arr[9][1] = 3
arr[9][2] = 3

arr[1][9] = 3
arr[2][9] = 3
arr[3][9] = 3

for i in range(len(arr)):
    print(arr[i])
#Реализуйте вывод в консоль поле для морского боя с выставленными кораблями.  DONE

#statistick(task31)
#statistick(task32)
#statistick(task7)
#statistick(task10)
