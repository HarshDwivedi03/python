# poistional argument
def sum(x,y):
    return x+y
p=sum(4,5)
print(p)
# keyword argument
def fun_name(x,y):
    print("value of x",x)
    print("value of y:,y")
    return x+y
p=int(input("enter number"))
q=int(input("enter number"))
z=fun_name(x=p,y=q)
print(z)
