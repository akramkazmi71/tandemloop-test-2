a = int(input())
for i in range(1,a+1):
    if i % 2 == 0:
        for k in range(i, 0, -1):
            if k == 1:
                print(k)
            else:
                print(k,' * ',end="")
    else:
        for k in range(1,i+1):
            if k == i:
                print(k)
            else:
                print(k,' * ',end="")
