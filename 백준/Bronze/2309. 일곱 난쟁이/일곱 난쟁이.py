numbers = [int(input()) for _ in range(9)]
numbers.sort()
sum_all = sum(numbers)
fake = []
for i in range(9):
    for j in range(i+1, 9):
        if len(fake) == 2:
            continue
        if sum_all - numbers[i] - numbers[j] == 100:
            fake.append(numbers[i])
            fake.append(numbers[j])

for i in numbers:
    if i in fake:
        continue
    print(i)