stu_num, max_num = map(int, input().split())
input_arr = [list(map(int,input().split())) for _ in range(stu_num)]

arr = [[0]*2 for _ in range(6)]

for i  in range(stu_num):
    if input_arr[i][0] == 0:
        arr[input_arr[i][1]-1][0] += 1
    else:
        arr[input_arr[i][1]-1][1] += 1

arr = sum(arr, [])

room_cnt = 0

for i in range(12):
    if arr[i] == 0:
        continue
    elif 0 < arr[i] <= max_num:
        room_cnt += 1
    else:
        a, b = divmod(arr[i], max_num)
        if b == 0:
            room_cnt += a
        else:
            room_cnt += a+1

print(room_cnt)