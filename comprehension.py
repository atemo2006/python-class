"""
first = [2,3,4,5]
print(first)
first[0] = 6
first[1] = 9
first[2] = 12 
first[3] = 15
print(first)
"""
# you times it by 3  or multiply by 3 to give the answer
list = [2,3,4,5]
result = []
for i in list:
    result.append(i*3)
print(result)

list = ['john','peter','james','paul']
result = []
for i in list:
    result.append(i.upper())
    print(result)

name = ["john","james","daniel","richards"]
to_upper = []
for i in name:
    to_upper.append(i.upper())
print(to_upper)

upper = [x.upper() for x in name]
print(upper)

result = [x*3 for x in list]
print(result)

# numerics = [16, "Daniels", 19, 24, "Samuel", "david", 56, "richard"]
# age = []
# for i in numerics:
#    age.append(i.integer())
# print(age)
# friends_name = []
# for x in numerics:
    # friends_name.append(x.strings())
# print(friends_name)
# numerics = [16, "tony",24, "michael",73, "rogers"]

# age = [x for x in numerics if isinstance(x, int)]
# friends = [i for i in numerics if not isinstance(i, int)]

# print("age", age)
# print("friends", friends)

numerics = [16, 'sanchez', 21, 'kelvin', 54, 'tony', 32, 'aria']
age = []
friends = []
for i in numerics:
    if type(i)==int :
        age.append(i)
print(age)

for i in numerics:
    if type(i)==str:
        friends.append(i)
    print(friends)

age = [i for i in numerics if type(i)==int]
print(age)
friends = [i for i in numerics if type(i)==str]
print(friends)

scores = [20,30,23,34, 56,34,23,56,45,84,46,49]
results = []
for i in scores:
    if i >60 and i <= 95:
        results.append(i+5)
print(results)


results = [i + 5 for i in scores if i > 60 and i <= 95]
print(results)

market = {
    'hp' : 230000,
    'apple' : 899000,
    'bios' : 10000,
    'ide' : 9000,
}
print(market.values())
new_market = [value + (value * 0.05) for value in market.values()]
print(new_market)
discount_market =[value -(value *0.07) for value in market.values() if value>=5000]
print(discount_market)
