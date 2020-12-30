# importing modules
import base64
from os import system
from termcolor import colored
#from pyfiglet import Figlet

# colors
gr = 'green'
rd = 'red'
bl = 'blue'
cn = 'cyan'
wt = 'white'
mn = 'magenta'

# Installing requirements....
#inst = input('''Need to install ...Do you want to install the requirements? (yes/no) : ''')
#print(colored("\n=============<( REQUIREMENTS SATISFIED )>=============\n",mn))


# Banner part
print(colored("   __________          _________________     ________   _____ ",cn))
print(colored("   \______   \_____   /   _____/\_____  \   /  _____/  /  |  |",cn))
print(colored("    |    |  _/\__  \  \_____  \   _(__  <  /   __  \  /   |  |_",cn))
print(colored("    |    |   \ / __ \_/        \ /       \ \  |__\  \/    ^   /",cn))
print(colored("    |______  /(____  /_______  //______  /  \_____  /\____   | By Jopraveen",cn))
print(colored("           \/      \/        \/        \/         \/      |__|",cn))
print()

# selecting option
print(colored("------<( Options )>------\n",wt))

print(colored(" 1) Encode",gr))
print(colored(" 2) Decode",rd)) 
print(colored(" 3) Force Encode",cn))
print(colored(" 4) Force Decode\n",mn))
option = int(input("====<( Choose your option: "))

# Encoding part
if option == 1:
    word = input("\nType something to encode: ")
    word_enc = word.encode("ascii")
    word_final = base64.b64encode(word_enc)
    print("\n =====<( The Encrypted message )>=====\n\n" , word_final)

# Decoding part
elif option == 2:
    enc_word = input("\nType something to decode: ")
    decrypt_word = base64.b64decode(enc_word)
    print("\n =====<( The Decrypted message )>=====\n\n",decrypt_word)

# Force Encoding
elif option == 3:
        print("\n=====<( Welcome to Force Encode mode :D )>=====\n")
        while True:
           word = input("\nType something to encode: ")
           word_enc = word.encode("ascii")
           word_final = base64.b64encode(word_enc)
           print("\n =====<( The Encrypted message )>=====\n\n", word_final)

elif option == 4:
        print("\n=====<( Welcome to Force Decode mode :D )>=====\n")
        while True:
         enc_word = input("\nType something to decode: ")
         decrypt_word = base64.b64decode(enc_word)
         print("\n =====<( The Decrypted message )>=====\n\n",decrypt_word)

# Errors Handling!
else:
    print(colored("\nChoose the correct option !\n",rd))
    system('python3 bas364.py')
