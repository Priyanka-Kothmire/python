user=input("enter the user :")
if len(user)>2:
    if user[-3:]=="ing":
        print(user+"ly")
    else:
        print(user+"ing")
else:
    print(user)



