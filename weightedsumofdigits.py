howmany = int(input())
data = input()
data = data.split()
print(data)
n = int(0)

for n in range(len(data)):
    sums = data[n] * n
    print(sums)
    n+=1


