

# Algorithm_1:
list_of_numbers = [10, 20, 30, 40, 50]

element = int(input("Enter element to find: "))

found = False
# idx = 0

for num in list_of_numbers:
    # idx = idx + 1
    if(num == element):
        found = True
        break

if(found == True):
    print(f"Element found!")
else:
    print("Element not found!")
