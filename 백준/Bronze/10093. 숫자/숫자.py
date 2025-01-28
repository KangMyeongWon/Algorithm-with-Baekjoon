numbers = list(map(int, input().split()))
numbers.sort()
result = []
for i in range(1, abs(numbers[1]- numbers[0])):
    result.append(numbers[0] + i)

print(len(result))
print(*result)

