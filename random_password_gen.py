import argparse
import random
import string

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('chars', nargs='?', help='The length of the password in characters.')
args = parser.parse_args()
# Argument Parser End

# Random Generator
def generate():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(converted_chars))
    print(password)
chars = args.chars
converted_chars = int(chars)
if converted_chars < 8:
    print('Password should be equal to/longer than 8 characters.')
    # gen_nonsecure = input('Do you want to generate a less secure password? [y/n] : ')
    # while '' in gen_nonsecure:
    while True:
        gen_nonsecure = input('Do you want to generate a less secure password? [y/n] : ')
        if gen_nonsecure == 'y' or gen_nonsecure == 'yes':
            generate()
            quit(0)
        elif gen_nonsecure == 'n' or gen_nonsecure == 'no':
            quit(0)
        else:
            print('Please answer y or n.')
            gen_nonsecure = gen_nonsecure
else:
    generate()
# Random Generator End