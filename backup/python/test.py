mainPassword = "Jacob@2005"
print("What is your name?")
userName=input()
if userName == "Nolan":
	print("Nolan bad")
elif userName == "nolan":
        print("Nolan bad")
elif userName == "Jacob":
        print("password")
        password=input()
        if password == mainPassword:
                print("nice")
        else:
                print("Go die you don't deserve to live")
elif userName == "jacob":
        print("password")
        password1=input()
        if password == "Jacob@2005":
                print("Yes it is you")
        else:
                print("Go die you don't deserve to live")
elif userName == "Eliot":
        print("password")
        password2=input()
        if password2 == "Eliot@2007":
                print("surprisingly " + password2 + " was correct. How did  you guess")
        else:
                print("surprisingly " + password2 + " was incorect")
elif userName == "eliot":
        print("password")
        password2=input()
        if password3 == "Eliot@2007":
                print("surprisingly " + password2 + " was correct. How did  you guess")
        else:
                print("surprisingly " + password2 + " was incorect")
else:
        print("Hello, " + userName)
        print("Have a nice day " + userName)
input("Press Enter to exit")
