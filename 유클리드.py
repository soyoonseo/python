def f(n,m):
    if(n < m):
        n , m = m, n
    while( m != 0):
        n = n%m
        n ,m = m , n
    print(n)
          
n, m = map(int, input().split())
f(n,m)
