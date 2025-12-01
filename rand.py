import random
import string
def rand():
    while True:
        choose = int(input("username(1) or password(2): "))
        if choose == 2:
            characters = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(characters) for i in range(8))
            print(random_string)
        elif choose == 1:
            characters = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(characters) for i in range(10))

            print(random_string + '@gmail.com')
rand()