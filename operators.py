# there are four operator types
"""
*assignment operator
*logical "
*arithmetic "
*comparison "
"""
# arithmethic operator
"""
+ add
- sub
/ div
* multiply
** exp(exponential)
// absolute division
% modulus
"""
#add
a=5
b=3
add = a+b
print(f"5+3={add}")

#sub
a = 5
b = 3
sub = a-b
print(f"5-3={sub}")

#multiply
a =5
b =3
multiply = a*b
print(f"5*3={multiply}")

#exponential
a =5
b =3
Exponential =a**b
print(f"5**3={Exponential}")

#absolute division
a =5
b =3
absolutedivision =a//b
print(f"5//3={absolutedivision}")

#module
a =5
b =3
mod =a%b
print(f"5%3={mod}")

#division
a =5
b =3
division =a/b
print(f"5/3={division}")

#comparison
"""
==equal to
!=not equal to
<less than
>greater than
<=less than or equal to
>= greater than or equal to
"""
#equal to
age =20
if age == 20:
    print(f'you are {age} years old')

#not equal to
if age !=20:
    print(f'you are {age} years old')
else:
    print(f'you are not {age}')
#less than
if age < 20:
    print(f'you are less than {age} years old')
else:
    print(f'you are not{age} years old')
# greater than
if age > 20:
    print(f'you are greater than {age} years old')

#equal to
if age <= 20:
    print(f'you are less than or eqaul to {age} years old')

#equal to 
if age >= 20:
    print(f'you are  more than or equal to 20 years old')


#logical 
"""
and
or 
"""
#and
#and condition will only be true when both the two condition are true
name = 'paige'
age = 21
if name =='paige' and age ==21:
    print(f'{name}is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')

if name =='gross' and age ==21:
    print(f'{name}is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')
    
if name =='paige' and age ==61:
    print(f'{name}is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')

if name =='pete' and age ==81:
    print(f'{name}is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')

#or
#or is only false when both are false
name = 'top boy'
age = 21
if name =='top boy' or age ==21:
    print(f'{name} is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')

if name =='lee' or age ==21:
    print(f'{name } is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')
    
if name =='jinx' or age ==61:
    print(f'{name} is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')

if name =='foe' or age ==81:
    print(f'{name} is {age} years old and youre welcome to class')
else:
    print(f'{name} you need to leave the building')


#assignment operators
"""
=
+=
-=
%=
*=
**=
/=
//=
"""
price =50
price +=90
print(price)

a = 20
a -= 15
print(a)

b = 5
b %= 2
print(b)

c = 50
c *= 20
print(c)

c = 200
c **= 100
print(c)

e = 9
e/= 3
print(price)

f =9
f //= 3
print(5%2)


