student = {
    'name': 'atemo',
    'age' : '18',
    'courses' : 'python',
}
# name,age and course is the dictionary keys while the values behind the colon is called dictionary values
print(student)
print(student['name'])
student['age'] = 20
print(student)
print(student.keys())
# it prints only the dictionary keys
print(student.values())
# it prints only the dictionary values
print(student.items())
# it prints the dictionary keys and values in groups
student.update({'gender':'male'})
# it updates any additional keys and values to the dictionary
print(student)

sales_products = {
    'laptop' : 'HP',
    'price' : 7875489,
    'phone' : 'blackberry',
    'price' : 7889768,
}
for i in sales_products.keys():
    print(i)
# for i in sales_products.values():
#     print(i) 
# for key, value in sales_products.items():
#     print(f'{key}:{value}')     