print("Exercise Lab 1: Create and Modify a List")
print()

print("Create a list of at least 6 names:")
student_list = ['Charlotte', 'Sabrina', 'Celeste', 'Charles', 'Joey', 'Cayden']
print(student_list)
print()
 
print("Add a name using append(): ")
student_list.append('Lee')
print(student_list)
print()

print("Insert a name at the 3rd position using insert():")
student_list.insert(2,'Hemory')
print(student_list)
print()

print("Remove the 5th entry:")
student_list.pop(4)
print(student_list)
print()

print("Print the remaining list in reverse-alphabetical order:")
student_list.reverse()
print(student_list)
print()

print("Exercise Lab 2: Create and Modify a List")
print()

print("Create a list of at least 5 numbers:")
num_list = [21,2,16,7,1]
print(num_list)
print()

print("Add a number to the list:")
num_list.append(23)
print(num_list)
print()

print("Insert a number in the 1st position:")
num_list.insert(0,99)
print(num_list)
print()

print("Remove the entry in the 3rd position:")
num_list.pop(2)
print(num_list)
print()

print("Print the remaining list in sorted order:")
num_list.sort()
print(num_list)
print()

print("Create a second list of numbers:")
num_list_two = [10,20,30,40,50]
print(num_list_two)
print()

print("Combine the second list of numbers to the first and print the results:")
num_list.extend(num_list_two)
print(num_list)
