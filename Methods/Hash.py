#Hash for md5,

import hashlib


def md5Encode(s):
    encodeStr = s.encode('utf-8')
    md5 = hashlib.md5(encodeStr)
    md5Hex = md5.hexdigest()
    print("MD5: "+md5Hex)




def main():
    inputStr = input("Enter string to encode, 'quit' to quit: ")
    while inputStr != '0':
        md5Encode(str)
        inputStr = input("Enter string to encode, '0' to quit: ")


if __name__ == '__main__':
    main()