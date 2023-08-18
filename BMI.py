def bodymasscheck(x):
    if x >= 30.0:
        return "obese"
    elif 25 <= x < 30:
        return "over"
    elif 18.5 <= x < 25:
        return "normal"
    elif x < 18.5:
        return "under"

howmany = int(input())
answer = []
for n in range(0, howmany):
    pair = input()
    pairlist = pair.split()
    pairlist = [float(num) for num in pairlist]
    bmi = pairlist[0] / pairlist[1] ** 2
    answer.append(bodymasscheck(bmi))

print(' '.join(answer))