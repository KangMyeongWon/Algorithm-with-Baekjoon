card = []
for i in range(1, 21):
    card.append(i)

numbers = [list(map(int, input().split())) for _ in range(10)]

for i in range(10):
    arr=[]
    start_idx = numbers[i][0]
    end_idx = numbers[i][1]
    for j in range(end_idx-1, start_idx-2, -1):
        arr.append(card[j])
    for k in range(len(arr)):
        card[start_idx+k-1] = arr[k]

print(*card)
