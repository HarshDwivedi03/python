# # n=int(input("enter any no"))
# # i=1
# # while i<=n:
# #     print(i)
# #     i=i+1
# n=int(input("enter any no"))
# i=1
# while(i<=n):
#     x=2*1
#     print(f'2*1{i}={x}')
#     print(x)
#     i+=1
# 1 to 10 print by using while loops
# n=int(input("enter any no"))
# i=1
# while(i<=n):
#     if i<n:
#         print(i,end=",")
#     else:
#         print(i)
#     i=i+1
    # amstrong number by while loop
# n=int(input("enter any no"))
# x=n
# digit=0
# while(n>0):
#         digit=digit+1
#         n=n//10
# print(digit)
# print(x)
    
    # sum
# n=int(input("enter any no"))
# x=y=n
# digit=0
# while(n>0):
#     digit=digit+1
#     n=n//10
# sum=0
# while (y>0):
#     lastdigit=y%10
#     sum=sum+lastdigit**digit
#     y=y//10
# if (n==sum):
#     print(f'{x}is armstrong')
# else:
#      print(f'{x}is not armstrong')
n=int(input("enter any no"))
x=n
revdigit=0
while(n>0):
    x=n%10
    revdigit=revdigit*10+n
    n=n//10
if x==revdigit:
    print(f'{x}is palindrome')
else:
    print(f'{x}is  not palindrome')


        

    
    