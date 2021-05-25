n = int(input())

arr = [ 0 for i in range(0,11)]

for i in range(1,n):
          s = int(input())
          arr[s] += 1

for i in range(1,n+1):
          if(arr[i] ==0):
                    print(i)
          
                    
                    
                    

