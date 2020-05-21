start = 1500
end = 2700
result = []
for i in range(start, end+1):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)
print(result)