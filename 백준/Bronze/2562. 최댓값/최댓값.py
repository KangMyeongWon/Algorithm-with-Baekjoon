numbers = [list(map(int, input().split())) for _ in range(9)]

print(max(numbers)[0])
print(numbers.index(max(numbers))+1)