# scope of variable
# local scope
# global scope
# x=10
# def add():
#     global y
#     y=20
#     print(x)
#     print(y)
# add()
# print(x)
# print(y)
# x=10
# def add():
#     global x
#     print(x)
#     x=20
#     print(x)
    
# add()
# print(x)
x=10
def add():
    global y
    x=20
    y=10
    print("value of global variable x:",globals()['x'])
    print("value of global variable x:",x)
    print("value of global variable y:",y)
    
add()
print(x)
print(y)
