numbers = open("input.txt")
list1 = []
list2 = []
for line in numbers:
    seperate = line.split()
    list1.append(seperate[0])
    list2.append(seperate[1])
list1.sort()
list2.sort()
total = 0
for a, b in zip(list1, list2):
    total += abs(int(a) - int(b))

print(total)