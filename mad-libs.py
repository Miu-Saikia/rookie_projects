import sys



def story1():
    mc = input("What is main character's name? >> ")
    obj_action=input("What was MC doing? >> ")
    obj = input("What MC is protecting? >> ")
    enemy = input("Who is the attacker? >> ")
    enemy_action=input("What did the attacker do? >> ")
    fake_aim=input("What was MC's ulterior motive? >> ")
    extra=input("Who came to help MC? >> ")
    extra_aim=input("What did they want to do? >> ")
    moral=input("What lesson did the MC learn? >> ")

    print("")

    a= f"""
            {mc} was bored while {obj_action},
            so he pretended  {enemy} was attacking to {fake_aim}. 
            {extra} rushed to { extra_aim} but found no {enemy}. 
            {mc} repeated this trick a few times. 
            One day, {enemy} actually attacked {obj}, but when {mc} called for help, 
            {extra} didn't believe {mc} and no one came. 
            {enemy} {enemy_action} many of {obj}, and 
            {mc} learned lesson: {moral}."""

    print (a)
    print("")
    start()

def start():
    while True:
        command = input("continue? y/n >> ").lower()

        if command == "y":
            story1()
            break
        elif command == "n":
            print("adiossss")
            sys.exit("exiting mad-libs...")

        else:
            print("invalid input. enter again")

start()