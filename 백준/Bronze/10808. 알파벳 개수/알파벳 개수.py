s = list(str(input()))
alphabet = list("abcdefghijklmnopqrstuvwxyz")
arr=[]

for i in range(len(alphabet)):
    arr.append(s.count(alphabet[i]))

print(*arr)