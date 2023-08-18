howmany = int(input())
answer = []

for x in range(0, howmany):
    pair = input()  # Take input as a string
    pairlist = pair.split()
    pairlist = [int(num) for num in pairlist]  # Convert the values to integers
    n = sum(pairlist)
    answer.append(n)

print(answer)