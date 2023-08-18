
howmany = int(input())
answer = []
for n in range (0, howmany):
    triplet = input()
    tripletlist = triplet.split()
    tripletlist = [int(num) for num in tripletlist]
    i = min(tripletlist)
    answer.append(str(i))

print(' '.join(answer))