x=10
y=10
print(id(x))
print(id(y))
# string
x='harsh'
y='harsh'
print(id(x),(id(y)))
# tuple
x=(10,20,30,'harsh')
x=(10,20,30,'harsh')
print(id(x),(id(y)))
# list
l1=(10,20,30,'harsh')
l2=(10,20,30,'harsh')
print(id(l1),(id(l2)))
# dictionary
d1={'name':'harsh','age':37}
d2={'name':'harsh','age':37}
print(id(d1),id(d2))
# set
s1={'name':'harsh','age':37}
s2={'name':'harsh','age':37}
print(id(s1),id(s2))
# frozenset
fset1=frozenset({10,20,30,'harsh',30})
fset2=frozenset({10,20,30,'harsh',30})
print(id(fset1),id(fset2))