words = [input() for _ in range(2)]
freq = [[0] * 26 for _ in range(2)]

for i in range(2):
    for j in range(len(words[i])):
        freq[i][ord(words[i][j])-ord('a')] += 1

cnt = 0
for i in range(26):
    if freq[0][i] == freq[1][i]:
        continue
    else:
        cnt += abs(freq[0][i] - freq[1][i])

print(cnt)