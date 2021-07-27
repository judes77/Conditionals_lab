print("Turn the computer on")
is_it_on = input("Did it boot up? ")
if is_it_on == "yes":
    print("Login with password")
elif is_it_on == "no":
    input("Is it plugged in? ")
    print("Plug it in ")
    plug_in = input("Did this fix the problem? ")
if plug_in == "yes":
    print("Log in with password")
elif plug_in == "no":
    print("The computer is broken!")