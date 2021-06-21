n = int(input())

r = 0
sum = 0
while (n>0):
    r = r*10 + n%10
    sum += n%10
    n = n//10

print(r)
print(sum)
