list1 = [1, 2, 3] 
list2 = [4, 5, 6]

temp = list2.copy()
list2 = list1.copy()
list1 = temp.copy()

print(list1)
print(list2)