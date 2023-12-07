print("String operators")
print("1.uppercase")
print("2.lowercase")
print("3.swapcase")
print("4.reverse")
print("5.length")
print("6.titlecase")
print("7.check if alphabetic")
print("8.check if lowercase")
print("9.check if uppercase")
print("10.convert to lowercase")
while True:
    a= int (input("Enter your choice:"))
    s= input ("Enter the string:")
    if a==1:
        print (s.upper())
    elif a==2:
        print (s.lower())
    elif a==3:
        print (s.swapcase())
    elif a==4:
        print (s[::-1])
    elif a==5:
        print (len(s))
    elif a==6:
        print (s.title())
    elif a==7:
        print (s.isalpha())
    elif a==8:
        print (s.islower())
    elif a==9:
        print (s.isupper())
    elif a==10:
        print (s.istitle())
    else:
        print("Enter valid option")
    rep=input("Do you want to continue?(yes/no):")
    if rep.lower()!="yes":
        break