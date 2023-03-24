import sys
import random

penalty = 0
score = 0


def start():
    target_num = random.randint(1, 10)
    for y in range(1, target_num):
        u_limit = y

    for z in range(target_num, 10):
        d_limit = z
    clue_num = []

    for x in range(u_limit, d_limit):
        clue_num.append(x)

    def input_val():
        def clue():
            while True:

                help = input("want a clue bud? y/n >> ").lower()
                if help == "y":
                    print(f"guess num is one of among these : {clue_num}")
                    penalty = +1
                    current_score = score - penalty
                    print(f"your score has decreased to {current_score}")
                    break
                elif help == "n":
                    print("alright no clue then")
                    break
                else:
                    print("invalid input. enter again")

        print("")
        try:
            user_num = int(input("enter your guess >> "))
        except:
            print("invalid input. enter again\n")
            input_val()

        if user_num == target_num:
            print("ya won!!!")
            start()
        elif user_num != target_num:
            print("eeeeeerrrr try again")
            clue()
            input_val()
        else:
            print("invalid input. enter again")
            input_val()

    while True:
        com = input("continue? y/n >> ").lower()
        if com == "y":
            input_val()
            break
        elif com == "n":
            sys.exit("exting...")
            break
        else:
            print("invalid input. enter again")
            start()


start()
