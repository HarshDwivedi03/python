# # # poistional argument
# # def sum(x,y):
# #     return x+y
# # p=sum(4,5)
# # print(p)
# # # keyword argument
# # def fun_name(x,y):
# #     print("value of x",x)
# #     print("value of y:,y")
# #     return x+y
# # p=int(input("enter number"))
# # q=int(input("enter number"))
# # z=fun_name(x=p,y=q)
# # print(z)
# # deafault
# def fun.name(x=0,y=0,z=0):
# print('x='x)
# print('y='y)
# print('z='z)
# return x+y+z:
# x=fun.name(4,5,6)
# print(x)
# variable lenth
# argument(*argument)
def add(*n):
    print(n)
    print(type(n))
    sum=0
    print(type(sum))
    for i in n:
        sum=sum+i
    return sum
# p=eval(input("enter any tuple"))
x=add(2,4,8)
print(x)

