s='neeraj'
l=[10,20,30,40]
t=[10,20,2,4,6,8]
d={'name','neeraj','quali','m.tech'}
s1={'neeraj','rahul','jai'}
x=frozenset(s)
print(x)
print(type(x))
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.union(y))
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
# print(x.intersection(y))
print(x.isdisjoint(y))
print(y.isdisjoint(x))
x={1,2,3}
y={1,2,3,4,5,6,7,8}
print(x.issubset(y))
print(y.issuperset(x))