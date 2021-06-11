sum = 0
for i in range(1, 101):
    s = "{:b}".format(i)

    if s.count("0") == 1:
        print("{}:{}".format(i, "{:b}".format(i)))

        sum += i
print("합계:", sum)







    
    
