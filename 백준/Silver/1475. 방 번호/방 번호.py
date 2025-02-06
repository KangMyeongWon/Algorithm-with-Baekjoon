arr = list(input())
freq = [0 for i in range(10)]

for i in range(len(arr)):
    if int(arr[i]) == 6 or int(arr[i]) == 9:
        if freq[6] < freq[9]:
            freq[6] += 1
        elif freq[9] < freq[6]:
            freq[9] += 1
        else:
            freq[int(arr[i])] +=1
    else:
        freq[int(arr[i])] += 1
print(max(freq))