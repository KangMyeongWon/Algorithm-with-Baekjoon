num_fir = list(map(int, input().split()))
numbers = list(map(int, input().split()))

result = []
for i in range(len(numbers)):
    if numbers[i] < num_fir[1]:
        result.append(numbers[i])

print(*result)