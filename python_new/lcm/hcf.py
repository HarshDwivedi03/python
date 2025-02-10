# lcm
# x=int(input("enter your first choice"))
# y=int(input("enter your second choice"))
# max_no=max(x,y)
# while True:
#    if max_no%x==0 and max_no%y==0:
#     break
# max_no=max_no+1
# print(f'lcm of{x}and {y}is{max_no}')
# hcf
x=int(input("enter your first choice"))
y=int(input("enter your second choice"))
min_no=min(x,y)
while True:
    if x%min_no==0 and y%min_no==0:
      break
    min_no=min_no-1
print(f'hcf of{x}and {y}is{min_no}')


