x=int(input("enter first no"))
y=int(input("enter second no"))
z=int(input("enter third no"))
if(x>y and x>z):
    print(f'{x}is greater')
else:
    if(y>z and y>x):
         print(f'{y}is greater')
    else:
        print("z is greater")

x=int(input("enter first no"))
y=int(input("enter second no"))
z=int(input("enter third no"))
if(x>y and x>z):
    print(f'{x}is greater')
elif(y>z and y>z):
    print(f'{y}is greater ')
elif(z>x and z>y):
    print(f'{z}is greater')
elif(x==y):
    print(f'{x}any{y}both are equal')
elif(y==z):
    print(f'{y}any{z}both are equal')
elif(z==x):
    print(f'{z}any{x}both are equal')


