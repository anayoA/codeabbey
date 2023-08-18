howmany = int(input())
answer = []
for n in range (0, howmany):
    pair = input()
    pairlist = pair.split()
    pairlist = [int(num) for num in pairlist]
    i = min(pairlist)
    answer.append(str(i))

print(' '.join(answer))