

# Algorithm_2:
list_1 = [10, 20, 30, 40, 50]
list_2 = [60, 70, 80, 90, 100]

num = int(input("Enter element to find: "))

found = False

for i in list_1:
    if(i == num):
        print("Element found in List 1")
        found = True

for i in list_2:
    if(i == num):
        print("Element found in List 2")
        found = True

if(found == False):
    print("Element not found")

