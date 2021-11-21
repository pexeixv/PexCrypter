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


def encrypt(bool):
    fileName = input('Enter file name: ')
    password = input('Enter encryption key: ')
    char32 = turnInto32Byte(password)
    PexCrypter = Fernet(base64.urlsafe_b64encode(char32))
    with open(fileName, "rb") as f:
        data = f.read()
    
    if(bool):
        encryptedData = PexCrypter.encrypt(data)
        with open(fileName, "wb") as f:
            f.write(encryptedData)
        return

    try:
        decryptedData = PexCrypter.decrypt(data)
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
            encrypt(True)
        elif choice==2:
            encrypt(False)
        elif choice>2:
            print('Invalid choice.')

if __name__ == '__main__':
    main()
