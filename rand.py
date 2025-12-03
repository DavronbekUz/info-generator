import random
import string
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="Davron.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )
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

        if choose > 2 or choose < 1:
            logging.debug(ValueError)
        else:
            logging.info("worked")
        return choose
start = rand()
print(start)