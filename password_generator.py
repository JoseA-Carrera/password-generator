import random
import string


def generator():

    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    nums = list(string.digits)
    symb = list(string.punctuation)

    characters = mayus + minus + symb + nums
    password = []

    for i in range(15):
        char_random = random.choice(characters)
        password.append(char_random)
    password = ''.join(password)

    return password


def run():
    password = generator()
    print(f'your new password is: {password}')


if __name__ == '__main__':
    run()
