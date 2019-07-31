# encrypter
import random

def key_generator ():
    element1=random.randrange(0,5)
    element2=random.randrange(0,5)
    key=[element1,element2]
    return key

def encryption (message,encryption_key):
    temp_message=message
    encrypted_message=''

    for i in range(len(temp_message)):
        a=ord(temp_message[i])+encryption_key[0]+i*encryption_key[1]
        encrypted_message += chr(a)

    #encrypted_message = str([chr(ord(temp_message[i])+encryption_key[0]+i*encryption_key[1]) for i in range(len(temp_message))])

    return encrypted_message

def decryption (encrypted_message,key):
    temp_message=encrypted_message
    message=''
    for i in range(len(temp_message)):
        a=ord(temp_message[i])-key[0]-i*key[1]
        message += chr(a)
    return message

def main():
    while True:
        print('Do you want to 1.encrypt or 2.decrypt? and 3.exit ')
        choice = int(input())
        if choice == 1:
            key = key_generator()
            print('Key is ' , key)
            message = input('Enter a message to be encrypted')
            encrypted_message = encryption(message,key)
            print('Encrypted Message' , encrypted_message)
        if choice == 2:
            key1 = int(input('Enter the first element of the first key'))
            key2 = int(input('Enter the second element of the second key'))
            key = [key1,key2]
            encrypted_message=input('Enter the message to be decrypted')
            message = decryption(encrypted_message,key)
            print('Decrypted Message' , message)
        if choice == 3:
            break
main()













































































































































































