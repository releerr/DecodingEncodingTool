# base64 encode/decode
# TODO:和PHP中base64_encode结果不一样？？？


import base64


# encoded base64
def encodeBase64(data):
    b = bytes(data, 'utf-8')
    encode64 = base64.b64encode(b)
    print(encode64.decode('utf-8'))


# decode base64
def decodeBase64(data):
    decoded = base64.b64decode(data)
    print(decoded.decode('utf-8'))


def main():
    inputD = input("Base64 'encode' or 'decode' or 'q' to quit ? ")
    inputD.lower()
    try:
        while inputD != 'q':
            if inputD == 'encode':
                encodeData = input("To encode: ")
                encodeBase64(encodeData)
            elif inputD == 'decode':
                decodeData = input("To decode: ")
                decodeBase64(decodeData)
            else:
                print("Err")
            inputD = input("Base64 'encode' or 'decode' or 'q' to quit ? ")
            inputD.lower()
    except Exception:
        print("Err.")


if __name__ == '__main__':
    main()
