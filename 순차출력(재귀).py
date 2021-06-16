def rec(n):

    if n != 0:
        rec(n-1)
        print(n)
    else:
        return 0

n = int(input())
rec(n)
