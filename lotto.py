import random
list1 = []
for _ in range(5):
    list2 = []
    for _ in range(6):
        r = random.randint(1, 45)
        list2.append(r)
    list2.sort()
    list1.append(list2)

for i in list1:
    print(i)


