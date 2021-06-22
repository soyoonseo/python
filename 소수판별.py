m = int(input())
n = int(input())
prime_num = []
​
for i in range(m,n+1):
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt +=1
            if cnt > 2: #시간초과 방지
                break
    if cnt == 2:
        prime_num.append(i)
if len(prime_num) != 0:
    print(sum(prime_num))
    print(min(prime_num))
else:
    print(-1)
