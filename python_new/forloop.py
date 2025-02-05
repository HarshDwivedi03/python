# # # # n=input("enter your name")
# # # # print(type(n))
# # # # for i in n:
# # # #     print(i)
# # # n='abcd'
# # # for i in n:
# # #     x=ord(i)+5
# # #     y=chr(x)
# # #     print(y,end='')
# # # n=input("enter any string")
# # # if n==n[::-1]:
# # #     print("pallindrome")
# # # else:
# # #     print("not a pallindrome")
# #     # range used for range(start,stop,step)
# # n=50
# # x=range(2,51,2)
# # print(list(x))
# # # range for even number
# # n=int(input("enter any no"))
# # x=range(2,n+1,2)
# # print(list(x))
# # # range for odd number
# # n=int(input("enter any no"))
# # x=range(1,n+1,2)
# # print(list(x))
# l=10
# x=range(l-1,-1,-1)
# print(list(x))
n=input("enter any string")
l=len(n)
x=''
for i in range(l-1,-1,-1):
    x=x+n[i]
if n==x:
    print(f'given string{n}is pallindrome')
else:
    print("not pallindrome")