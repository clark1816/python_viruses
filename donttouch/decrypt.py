import os 
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'potter.py' or file == 'thekey.txt' or file == 'decrypt.py':
        continue
    files.append(file)


print(files)

with open("thekey.txt", "rb") as key:
    secretkey = key.read()



for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)


