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
        if "dog" in a or "Dog" in a:
            print("you used the word \"dog\" or the word \"Dog\"")
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
    for d in range (1, 41):
        if d % 2 == 0:
            continue
        elif d % 5 == 0:
            continue
        elif d % 3 != 0:
            continue
        else:
            print(d)


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    my_list_vowel = [97, 101, 105, 111, 117]
    v =  input("give me a string: ")
    l = len(v)
    if 2<= l <= 5:
        for m in v:
            if ord(m) in my_list_vowel:
                print("letter ", m, "is a vowel")
            else:
                print("letter ", m, "is a consonant")
        
    

    

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    user_choice = input("Choose one option: a, b, or c: ")
    while True:
        if user_choice == "a":
            user_choice = input("Choose one option: a, b, or c: ")
        elif user_choice == "b":
            print("Goodbye")
            break
        elif user_choice == "c":
            sys.exit()
        else:
            print("try again")
            user_choice = input("Choose one option: a, b, or c: ")
            
            

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
