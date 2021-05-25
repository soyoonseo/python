s = input()
arr=[0 for i in range(1,123)]
for i in range(0, len(s)):
       n = ord(s[i])
       arr[n]+=1              

for i in range(97, 123):
          print(chr(i),":",arr[i])
          
                    
                    
                    

