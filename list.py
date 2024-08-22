student = ["joshua","mbata","lincoln","rodrigo","richards"]
print(student[1])
print(len(student))

# slicing has a starting and a ending but the ending is not always inclusive
# slicing from the front is done with positive digits, while slicing from the back is done with negative digits
print(student[1:4])
print(student[-4:-1])
print(student[0:4])
student[0] = 'john' 
print(student)

# list method
# append
student.append("donald")
print(student)
# append is used to add to the end of the list
# insert
student .insert(2,"rick")
print (student)
# insert adds a stringed value in place of another

# pop
student.pop()
print(student)
# pop will remove the last item


# clear
# student.clear()
# print(student)
# clear removes all the values that have benn typed
#  
# copy
new_student = student.copy()
print(new_student)
# it prints out what has been typed/ copies it

# index
index = student.index("richards")
print(index)
# index tells you the location of the value

# extend
namings = [2,3,4,5,6]
namings_two =["1","7","8","9","10"]
namings.extend(namings_two)
print(namings)
# it links two different sets of values and prints them 