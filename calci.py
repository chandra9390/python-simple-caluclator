print("Are you up for caluclations answer in yes or no")
answer=input()
if answer=="yes":
    print("lets go!")
elif answer=="no":
    print("not a math lover i guess,see you bye")
elif answer=="":
    print("please answer in yes or no, only")
    answer=input()
    if answer=="yes":
        print("lets go!")
    elif answer=="no":
        print("not a math lover i guess,see you bye")

print("\n\ni guess you love math , lets get the inputs dude")
firstnumber=input("firstnumber: ")
secondnumber=input("secondnumber: ")
print("sorry buddy if you want to choose multiple numbers or multiple operations,you can wait for the next patch\nType the no. which of the following operations you want to do:\n1)add\n2)subract\n3)multiply\n4)divide\n")
print("NOTE: PLEASE DONT USE SPECIAL CHARACTERS OR DECIMAL NUMBERS IN GIVING INPUT NUMBERS")
ans=int(input())
if ans==1:
    print("sum is:",int(firstnumber)+int(secondnumber))
elif ans==2:
    print("subraction is:",int(firstnumber)-int(secondnumber))
elif  ans==3:
    print("multiplication is:",int(firstnumber)*int(secondnumber))
elif ans==4:
    print("Division is:",int(firstnumber)/int(secondnumber))

print("\nIt's pleasure doing buisness ,byee!\n")
    
