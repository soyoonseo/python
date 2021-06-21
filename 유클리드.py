#최대공약수
def f(n,m):
    if(n < m):
        n , m = m, n
    while( m != 0):
        n = n%m
        n ,m = m , n
    print(n)
          
n, m = map(int, input().split())
f(n,m)



#최대공약수, 최소공배수
a, b=map(int, input().split())

def gcd(a,b):
    if(a<b):
        a,b=b,a
    while(b!= 0):
        a = a%b
        a,b = b,a
    return a
        
def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))
