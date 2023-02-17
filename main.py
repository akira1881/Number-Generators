import random

# Programmed by: Charina C. Vallecera
# BSCOE 2-2
# DSA Final Project
# Number Generators


def main():
    print("\n <<<<<< MAIN >>>>>> \n")
    print("1. Sequence Generator ")
    print("2. Sorting Numbers")
    print("3. Generating Random Numbers")
    print("4. Text to Number Generator")
    print("5. Exit the Program")


def fibonacci():
    while True:
        print("\n<<< Fibonacci Sequencing Numbers >>>")
        num = int(input(" -> Enter a number: "))

        n1, n2 = 0, 1
        count = 0

        if num <= 0:
            print(" -> Please Enter a Positive Integer")
        elif num == 1:
            print("Fibonacci Sequence - ", num, ":")
            print(n1)
        else:
            print("Fibonacci Sequence:")
            while count < num:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1

        again = input("\n-> Would you like to enter another number? [ yes / no ] : ")
        if again.casefold() == "yes":
            fibonacci()
        elif again.casefold() == "no":
            runProg()


def sorting():
    while True:
        print("\n<<< Sorting Numbers >>>")
        print(" -> Enter a number: ")
        num = list(map(int, input().split()))
        num.sort()
        print("\n -> Sorted Numbers:")
        print(num)

        again = input("\n-> Would you like to sort another number? [ yes / no ] : ")
        if again.casefold() == "yes":
            sorting()
        elif again.casefold() == "no":
            runProg()


def random_num():
    while True:
        print("\n<<< Generating Random Number >>>")
        listed = random.sample(range(0, 100), 10)
        print(" -> Random Number: ", listed)

        again = input("\n-> Would you like to generate another number list? [ yes / no ] : ")
        if again.casefold() == "yes":
            random_num()
        elif again.casefold() == "no":
            runProg()


def text_to_num():
    while True:
        print("\n<<< Text to Number Generator >>>")
        converts = input("Enter the text to convert: ")
        listed = []
        for i in converts:
            listed.append(ord(i) - 96)
        print(listed)

        again = input("\n-> Would you like to convert another text to number? [ yes / no ] : ")
        if again.casefold() == "yes":
            text_to_num()
        elif again.casefold() == "no":
            runProg()


def exits():
    while True:
        print("\n<<< EXIT >>>")
        exited = input(" -> Do you want to exit program? [ yes / no ] : ")
        if exited.casefold() == "yes":
            print("Thank you for using the Program!")
            print("Bye!")
            exit()
        elif exited.casefold() == "no":
            runProg()
        else:
            print("Invalid Input! Please try again!")
            continue


def runProg():
    while True:
        main()
        Option = int(input("\n -> Choose the number corresponding to your choice: "))

        if Option in (1, 2, 3, 4, 5, 6, 7):
            if Option == 1:
                fibonacci()
            if Option == 2:
                sorting()
            if Option == 3:
                random_num()
            if Option == 4:
                text_to_num()
            if Option == 5:
                exits()
        else:
            print("Invalid Input! Choose a number on the menu and try again!")
            continue


while True:
    runProg()
