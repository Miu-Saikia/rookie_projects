import sys
def value():
    global num_1
    global num_2
    global opr
    global result

    num_1 = int(input("enter number #1 >> "))
    num_2 = int(input("enter number #2 >> "))
    opr = input("chose operator (+,-,*,/) >> ")
    result = 0
    process()


def process():
    if opr == "+":
        result = num_1 + num_2
        print(result)
    elif opr == "-":
        result = num_1 - num_2
        print(result)
    elif opr == "*":
        result = num_1 * num_2
        print(result)
    elif opr == "/":
        result = num_1 / num_2
        print(result)
    else:
        print("invalid operator input")

def start():
    while True:
        decision = input("Launch Calcy y/n? >> ").lower()
        if decision == "y":
            value()
        elif decision == "n":
            sys.exit("exiting calcy....")
            break
        else:
            print("invalid input. please enter again")
start()