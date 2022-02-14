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
    print('Password shpuld be equal to or longer than 8 characters.')
    gen_nonsecure = input('Do you want to generate a less secure password? [y/n] : ')
    if 'y' in gen_nonsecure:
        generate()
    else:
        quit(0)
else:
    generate()
# Random Generator End