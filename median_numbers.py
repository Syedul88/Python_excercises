length_of_list = int(input("number of value: "))
list = []
for i in range(length_of_list):
    user_input = int(input("enter value: "))
    list.append(user_input)
print(list.sort())

def median():
    result = len(list)/2
    print("Median is: ", list[int(result)])

median()

"""
list1 = [45, 60, 61, 66, 70, 77, 80]
list1.sort()
a = (len(list1))/2
print("Median: ",list1[int(a)])
"""