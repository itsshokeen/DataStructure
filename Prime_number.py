num = int(input())

for i in range(2,num):
    if i>1:
        for j in range(2,num):
            if (i%j)==1:
                print("not prime number")
        else:
            print ("prime",j)
