# # # # # poistional argument
# # # # def sum(x,y):
# # # #     return x+y
# # # # p=sum(4,5)
# # # # print(p)
# # # # # keyword argument
# # # # def fun_name(x,y):
# # # #     print("value of x",x)
# # # #     print("value of y:,y")
# # # #     return x+y
# # # # p=int(input("enter number"))
# # # # q=int(input("enter number"))
# # # # z=fun_name(x=p,y=q)
# # # # print(z)
# # # # deafault
# # # def fun.name(x=0,y=0,z=0):
# # # print('x='x)
# # # print('y='y)
# # # print('z='z)
# # # return x+y+z:
# # # x=fun.name(4,5,6)
# # # print(x)
# # # variable lenth
# # # argument(*argument)
# # def add(*n):
# #     print(n)
# #     print(type(n))
# #     sum=0
# #     print(type(sum))
# #     for i in n:
# #         sum=sum+i
# #     return sum
# # # p=eval(input("enter any tuple"))
# # x=add(2,4,8)
# # print(x)
# # def add(*n):
# #     print(n)
# #     print(type)
# # x=eval(input("enter your type"))
# # add(*x)
# # def add(*n):
# #     sum=0
# #     for i in n:
# #      sum=sum+i
# #     return sum
# # x=eval(input("enter your type"))
# # y=add(*x)
# # print(y)
# # variable ker argument
# def show_my_detail(name='guest',age=None,qualifi=None):
#     print('name is:',name)
#     print('age is:',age)
#     print('qualifi is:',qualifi)
#     show_my_detail(name='harsh',age=27,qualifi='btech')
# def show_my_detail(**n):
#     print(n)
#     print(type(n))
# show_my_detail()
# show_my_detail(name='harsh',age=27,qualifi='btech')
def show_my_detail(**n):
    for k,v in n.items():
        print(f'my {k} is {v}')
# show_my_detail()
# show_my_detail(name='harsh',age=27,qualifi='btech')
# def show_my_detail(**n):
#     for k,v in n.items():
#         print(f'my {k} is {v}')
# # show_my_detail()
# show_my_detail(name='harsh',age=27,qualifi='btech')
# def show_my_detail(**n):
#     print(n)
#     print(type(n))
# x=eval(input("enter your dict"))
# show_my_detail(**x)
# keys() value() item() use for dictionary


             