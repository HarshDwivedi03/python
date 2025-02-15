# n=int(input("enter your no"))
# x=n
# sum=0
# while n>0:
#     last_digit=n%10
#     sum=sum+last_digit
#     n=n//10
# print(sum)
# print(n)
# if n%sum==0:
#     print("harshad number")
# else:
#     print("not harshad number")
    # spy number
n=int(input("enter your no"))
prod=1
sum=0
while n>0:
    last_digit=n%10
    sum=sum+last_digit
    prod=prod*last_digit
    n=n//10
if sum==prod:
    print("spy number")
else:
    print("not a spy number")