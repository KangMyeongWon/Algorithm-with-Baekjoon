n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]
input_arr = []
compar_arr = []
for i in range(n):
    if len(arr[i]) == 1:
        continue
    else:
        input_arr.append(list(sorted(arr[i][0])))
        compar_arr.append(list(sorted(arr[i][1])))

for i in range(n):
    if input_arr[i] != compar_arr[i]:
        print("Impossible")
    else:
        print("Possible")