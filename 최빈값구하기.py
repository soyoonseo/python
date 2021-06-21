list=[]

for i in range(10):
    i = int(input())
    list.append(i)

print(sum(list)//10)

max_num = max(list)
list_cnt = [0]*max_num

for i in list:
    list_cnt[i-1] += 1

print(list_cnt.index(max(list_cnt))+1)
