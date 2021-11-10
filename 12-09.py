from random import randint
def bubble(list1):
    for i in range(N-1):
        for j in range(N-i-1):
            if list1[j] > list1[j+1]:
                tmp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = tmp

def sort(list2):
    list2.sort()

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

b = a
print(a)
bubble(a)
sort(b)
print(a)
print(b)
