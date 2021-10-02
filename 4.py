list1 = list(map(int, input().split()))
even = 0
odd = 0
for i in list1:
    if i % 2 != 0:
        odd += 1
    else:
        even += 1
print('Even=',even,', odd=',odd)