import sys

N = int(sys.stdin.readline().strip())
num_arr = [1]
last_num = 1
answer = ['+']
for _ in range(N):
    input_num = int(sys.stdin.readline().strip())
    if len(num_arr) == 0:
        last_num += 1
        num_arr.insert(len(num_arr), last_num)
        answer.insert(len(answer), '+')
        if input_num > num_arr[-1]:
            for _ in range(last_num+1, input_num+1):
                last_num += 1
                num_arr.insert(len(num_arr), last_num)
                answer.insert(len(answer), '+')
            num_arr.pop()
            answer.insert(len(answer), '-')
        elif input_num == num_arr[-1]:
            num_arr.pop()
            answer.insert(len(answer), '-')
        else:
            answer.insert(len(answer), 'NO')
    else:
        if input_num > num_arr[-1]:
            for _ in range(last_num+1, input_num+1):
                last_num += 1
                num_arr.insert(len(num_arr), last_num)
                answer.insert(len(answer), '+')
            num_arr.pop()
            answer.insert(len(answer), '-')
        elif input_num == num_arr[-1]:
            num_arr.pop()
            answer.insert(len(answer), '-')
        else:
            answer.insert(len(answer), 'NO')

if 'NO' in answer:
    print('NO')
else:
    for i in answer:
        print(i)