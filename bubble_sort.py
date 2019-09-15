list= [3,2,100,6,67,56]

for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
print(list)
