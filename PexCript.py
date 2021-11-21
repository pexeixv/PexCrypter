from cryptography.fernet import Fernet
import base64

def turnInto32Byte(password):
    char32 = ''
    while len(char32)<32:
        if len(char32)+len(password)<=32:
            char32 += password
        else:
            diff = 32 - len(char32)
            char32 += password[:diff]
    char32 = str.encode(char32)
    return char32

def encrypt():
    fileName = input('Enter file name: ')
    password = input('Enter encryption key: ')
    char32 = turnInto32Byte(password)
    pexcript = Fernet(base64.urlsafe_b64encode(char32))
    with open(fileName, "rb") as f:
        data = f.read()

    encryptedData = pexcript.encrypt(data)
    
    with open(fileName, "wb") as f:
        f.write(encryptedData)

def decrypt():
    fileName = input('Enter file name: ')
    password = input('Enter decryption key: ')
    char32 = turnInto32Byte(password)
    pexcript = Fernet(base64.urlsafe_b64encode(char32))
    with open(fileName, "rb") as f:
        data = f.read()

    try:
        decryptedData = pexcript.decrypt(data)
        with open(fileName, "wb") as f:
            f.write(decryptedData)
    except:
        print('\nDecryption key error!')

def main():
    choice = 1
    while choice>0:
        print('\n______PexCripter______\n')
        print('Choose one of the following options.')
        print('1. Encrypt a file')
        print('2. Decrypt a file')
        print('0. Exit')
        choice = int(input('Enter choice: '))
        if choice==1:
            encrypt()
        elif choice==2:
            decrypt()
        elif choice>2:
            print('Invalid choice.')

if __name__ == '__main__':
    main()