len_arr = int(input())
arr = list(map(int, input().split()))
find_num = int(input())
freq = [0] * (max(arr) + 1)

for num in arr:
    freq[num] += 1

cnt = 0

for num in arr:
    target = find_num - num
    if 0 <= target < len(freq) and freq[target] > 0:
        cnt += freq[target]

print(cnt//2)