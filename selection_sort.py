list = [10,34,9,4,89,566,88]

for i in range(len(list)):
    min_index = i
    for j in range(i+1, len(list)):
        if list[j] < list[min_index]:
            min_index = j

    list[i],list[min_index] = list[min_index],list[i]

print(list)
