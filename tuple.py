# tuple is inmutable(cannot be edited)
family = ('okki', 'ronald', 'kevin', 'richards')
print(family[0])
# family.append('jameson')
print(family)
new_tuple = list(family)
new_tuple.append('jameson')
print(new_tuple)
family = tuple(family)
# for anything that is constant and does not need change you use tuple 
# for anything that will not change you use tuple