# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"


# Task 1
def check_text():
    """ Add your docstring """
    a = input(" give me a sentance: ")
    while secret_word not in a:
        if "dog" in a:
            print("you used the word \"dog\"")
            break
        if "Dog" in a:
            print("you used the word\"Dog\"")
            break
        else:
            print("try again")
            a = input(" give me a sentance: ")
    if secret_word in a:
        print("You used the secret word!")
            
        



# Task 2
def check_greater():
    """ Add your docstring """
    b = int(input("give me an integer: "))
    c = int(input("give me a second integer: "))
    while True:
        if b > c:
            print("first is greater")
            break
        elif c > b:
            print("second is greater")
            break
        else:
            print("try again")
            b = int(input("give me an integer: "))
            c = int(input("give me a second integer: "))
            



# Task 3
def get_special_numbers():
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
