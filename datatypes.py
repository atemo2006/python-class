"""
there are 2 categories of datatypes in python:
*primitive, and
*data collection
examples of primitive:
1 string 
2 boolean
3 none
4 integer
5 float
examples of data collection:
1 list
2 tuple
3 dictionary
4 set 
"""
# examples of strings
name = "atemo"
school = "g-skills"
age = '18'
print(type(name))
print(type(school))
print(type(age))
# anything inside a quote is known as a string(whether is a number or text)

# examples of integer
age = 15
print(type(age))
# integers are also called numbers but the type is called(int)

# examples of float
price = 6.7
print = (type(price))
# float is an integer with decimal(generally in programming)

# examples of boolean
is_student = True
print(type(is_student))
# boolean is a true or false statement and its known as (bool)

# examples of none 
none = 5*"n"
print(none)

# examples of list
# is a way of collecting data in python
list = []
print(type(list))
# when printing longer text no need to add type
courses =["python","js","html","css"]
print(courses)
print(type(courses))

# examples of tuple
tuple = ()
print(type(tuple))

# example of dictionary
dict = ()
print(type(dict))

# example of set
set = ()
# this is how to create a set
courses ={'html','css','js','python'}
courses.add('python')
print(courses)
courses.remove('python')
print(courses)
courses.update('project')
print(courses)
courses.pop()
print(courses)
new_courses = courses.copy()
print(courses)