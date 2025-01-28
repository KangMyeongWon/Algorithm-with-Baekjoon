numbers = [list(map(int, input().split())) for _ in range(3)]

result = []
for i in range(3):
    sum_arr = sum(numbers[i])
    if sum_arr == 0:
        result += 'D'
    elif sum_arr == 1:
        result += 'C'
    elif sum_arr == 2:
        result += 'B'
    elif sum_arr == 3:
        result += 'A'
    else:
        result += 'E'
print(result[0], result[1], result[2])
