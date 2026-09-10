n=int(input("Enter a number: "))
if n% 2!=0 :
    print("Weird")
elif n%2==0 & 1<n<6:
    print("Not Weird")
elif n%2==0 & 5<n<21:
    print("Weird")
else:
    print("Not Weird")