
def fun(a,b,operator):
    if operator =="+":
      return a+b
    elif operator=="*":
      return a* b
    elif operator=="/":
      return a / b
    elif operator=="-":
      return a-b
    else:
     print("your input is incorect, so the program is terminate ")
print("please, input a number= ")
a=int(input())
print ("please in put second number= ")
b=int(input())  
print("input the operator +,-,*,/")
operator=input()  
answer= fun(a,b,operator)   
print("your output is=",answer)