def insertionsort(list):

    for index in range(1 , len(list)):
        current_value = list[index]
        position = index
        while current_value < list[position-1] and position>0:
            list[position] = list[position-1]
            position = position-1
        list[position] = current_value
        
list1=[3,5,33,1,2,45,65,30]
insertionsort(list1)
print(list1)
