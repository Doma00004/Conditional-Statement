user=input("Enter user id:")
if user=="admin":
    print("Login successfull")
    attendance=input("Enter attendance:")
    if attendance=="Full":
        print("Staff attendance is full")
    elif attendance=="Half":
        print("Staff attendance is half")
    elif attendance=="Morning":
        print("Staff attendance is morning")
    else:
        print("Staff is absent")
else:
    print("Unable to login")
