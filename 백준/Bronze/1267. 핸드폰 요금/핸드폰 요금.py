call_num = int(input())
call_time = list(map(int, input().split()))

Y = 0
M = 0
for i in range(call_num):
    Y += ((call_time[i]//30)+1)*10
    M += ((call_time[i]//60)+1)*15

if M < Y:
    print("M " + str(M))
elif M > Y:
    print("Y " + str(Y))
else:
    print("Y M " + str(Y))