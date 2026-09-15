# a = int(input("Enter a number : "))
# b= 20
# c= a + b
# print(c)






# a= int(input("Enter a number: "))
# if a%2==0:
#     # print("The given number is EVEN: True")
#     print(f"The given number is even: True")
# else:
#     print("The given number is ODD : False")




# a = 3
# a%2 != 0
# print("Number is odd:",a%2!=0)



# WAP to print age in days
# 3years=1095 days

# age =22
# print(f"{age} years =",age*365, "days")

# # wap to convert miniutes into hours and print it
# minutes=int(input("Enter minutes: "))


# print(f"{minutes} is {minutes//60} hours {minutes%60} minutes")



# wap to extract last digit of a number
# a=1234
# print(f"{1234} : last digit is {a%10}")


# role=str(input("Enter role : "))
# age=int(input("Enter age : "))
# a=(role=="student") and  (age<21)
# print(f"Eligible : {a}")


# WAP to swap two variables without third variable using arithmetic operator

# a=10
# b=20
# print(f"Before swap : a={a} b={b}")
# print(f"After swap : a={a+b-a} b={b+a-b}")





# -----if-else--------- #
# is_raining=False
# if is_raining==True:
#     print("Raining outside")
# else:
#     print("Not raining")



# ------------------------------------------------------------------------------
# age=int(input("Enter your age: "))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")



# -------------------------------------------------------------------------------------------
# n=int(input("Enter a number: "))
# if n==1:
#     print("Sunday")
# elif n==2:
#     print("Monday")
# elif n==3:
#     print("Tuesday")
# elif n==4:
#     print("Wednesday")
# elif n==5:
#     print("Thursday")
# elif n==6:
#     print("Friday")
# elif n==7:
#     print("Saturday")
# else:
#     print("Invalid number")


# ------------------------------------------------------------------------------------------------
# day=int(input("Enter the day number: "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")





# --------------------------------------------------------------------------------------------

# n=int(input("Enter a number: "))
# if n%2==0:
#     print(f"the number {n} is even")
# else:
#     print(f"the number {n} is odd")



# --------------------------------------------------------------------------------------------

# tic=100
# disc=tic*10/tic
# disc_price=100-disc

# age=int(input("Enter your age : "))

# if age<12:
#     print(f"You have got 10% off on the ticket")
#     print(f"Your ticket price is {disc_price}")
# else:
#     print(f"The ticket price is 100")



# --------------------------------------------------------------------------------------------
# marks=int(input("Enter your marks: "))
# if 100>marks>90:
#     print("O")
# elif marks>100:
#     print("Marks will not be calculated above 100")
# elif marks>=80:
#     print("A+")
# elif marks>=65:
#     print("B")
# elif marks>=35:
#     print("C")
# elif 0<marks<35:
#     print("F")
# else:
#     print("Invalid marks")


# # ------------------------------------------------
# num=eval(input("enter a number: "))
# if num>0:
#     print("The number is positive")
# elif num==0:
#     print("0 is neither positive nor negative")
# else:
#     print("The number is negative")


# ---------------------------------------------------
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))

# if b<a>c:
#     print("The value of a is greater")
# elif a<b>c:
#     print("The value of b is greater")
# elif a==b==c:
#     print("All numbers are same")
# elif a==b>c:
#     print("the value a & b is greater than c")
# elif a==c>b:
#     print("The value of a & c is greater than b")
# elif b==c>a:
#     print("The value of b & c is greater than a")
# else:
#     print("The value of c is greater")

# --------------------------------------------------------------------------------------


# year=2000
# days=year*365
# days=year%5
# if days==366:
#     print("The given year is leap year")
# else:
#     print("the given year is not leap year")

# ---->This problem is not done yet

# ----------------------------------------------------------------------------



# a=eval(input("Enter a number: "))
# b=eval(input("Enter a number: "))
# operand=input("enter an operand: ")

# operand=="+","-","*","/"
# if operand=="+":
#     print(f"{a+b}")
# elif operand=="-":
#     print(f"{a-b}")
# elif operand=="*":
#     print(a*b)
# elif operand=="/" and b==0:
#     print("Cannot be divided by zero")
# elif operand=="/":
#     print(f"{a/b}")
# else:
#     print("invalid operand")


# ------------------------------------------------

a=eval(input("Enter a number: "))
b=eval(input("Enter a number: "))
operator=input("Enter operator: ")
match operator:
    case "+":
        print(a+b)
    case "-":
        print(f"{a-b}")
    case "*":
        print(f"{a*b}")
    case "/":
        if b==0:
            print(f"cannot be divided by zero")
        else:
            print(a/b)
    case _:
        print("Invalid operand")
    

# --------------------------------------------------------------------------------------------

