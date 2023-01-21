"""Knock knock joke with conditionals"""

inter_cow: str = input("Do you want an interrupting cow? ")


if (inter_cow == "yes"):
    print("Knock knock")
    print("...who's there?")
    print ("Interrupting cow.")
    print ("...interrupting cow wh---")
    print ("MOO!!!")
else: 
    print("Oh...okay.. :(")
    if (inter_cow == "you're not funny"):
        print ("Wow.. that hurts my feelings. :'(")



