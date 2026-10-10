# ------------------------------------------------------
#        Name: (Abigail)
#       Peers: (add any collaborators)
#  References: (https://realpython.com/ref/glossary/ascii/)
# ------------------------------------------------------
import sys

secret_word = "food"


# Task 1
def check_text():
    """ This function takes in a sentence from the user and then checks it against the secret word
then checks it against the word dog and Dog. and if it doesnt have that you have to try again"""
    a = input(" give me a sentance: ")
    while True:
        if secret_word in a: # doesn't need to be in the loop since it is not repeated
            print("You used the secret word!")
            break
        elif "dog" in a or "Dog" in a: # must set both into a or it wont work
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")
            a = input(" give me a sentance: ")
    
            
        



# Task 2
def check_greater():
    """this function gets two integer inputs from the user and decides which one is bigger.
if they are the same it goes again"""
    b = int(input("give me an integer: "))
    c = int(input("give me a second integer: "))
    while True:
        if b > c:
            print("First is Greater")
            break
        elif c > b:
            print("Second is Greater")
            break
        elif b == c:  
            print("Try again")
            b = int(input("give me an integer: ")) #  allows for the loop to repeat
            c = int(input("give me a second integer: "))
    print("Done")
            



# Task 3
def get_special_numbers():
    """ This function takes numbers [1,40] and tests them against certain conditions
these if it passes said contitions it will be printed, if not it will be discarded"""
    for d in range (1, 41):
        if d % 2 == 0:
            continue # need this to pass onto the next condition
        elif d % 5 == 0:
            continue
        elif d % 3 != 0:
            continue
        else:
            print(d) # only will happen if all the of statements are passed


# Task 4.a
def my_for_loop():
    """ takes input from user, this string must be a 2 to 5 letter word, if not it will be ignored.
then it compares them to the ascii values and decide if its a vowle or a consonant"""
    my_list_vowel = [97, 101, 105, 111, 117] # ascii values for aeoiu
    v =  input("give me a string: ")
    l = len(v) # stores length of the input
    for m in v:
        if 2<= l <= 5:
            if ord(m) in my_list_vowel:
                print("letter", m," is a vowel")
            elif ord(m) not in my_list_vowel:
                print("letter", m, "is a consonant")
        else:
            SystemExit()
    

    

# Task 4.b
def my_while_loop():
    """ takes inputed choice. is a is chosen the question is repeated, if b is chosen
the loop ends, if c is chosen exit code, if other letrer inputed repeat"""
    user_choice = input("Choose one option: a, b, or c: ")
    while True:
        if user_choice == "a":
            user_choice = input("Choose one option: a, b, or c: ")
        elif user_choice == "b":
            print("Goodbye")
            break # exits the loop
        elif user_choice == "c": 
            sys.exit()# quits the code
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
