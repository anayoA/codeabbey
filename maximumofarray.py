x = input()
numbers = x.split()
numbers = [int(num) for num in numbers]
answer = []
answer.append(max(numbers))
answer.append(min(numbers))
answer = [str(num) for num in answer]
print(' '.join(answer))