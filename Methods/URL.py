# URL decoding and encoding tool

from urllib.parse import quote, unquote
from utilities import DataListContainer

asciiList = DataListContainer.asciiList
win1252EncodeList = DataListContainer.win1252EncodeList


# ASCII encoded
def asciiEncode(input):
    s = []
    try:
        for i in range(len(input)):
            for j in range(len(asciiList)):
                if input[i] == asciiList[j]:
                    s.append(win1252EncodeList[j])
                    print("' " + input[i] + " '" + " = " + win1252EncodeList[j])
                    break
                elif j == len(asciiList) - 1:
                    print("no such char")
                else:
                    continue
        print(*s)
    except Exception:
        print("Err. ")

# ASCII decoded
def asciiDecode(input):
    decoded = unquote(input)
    print("Decoded: " + decoded)


# url encode
def urlEncode(input):
    encoded = quote(input)
    print("URL Encoded: " + encoded)

#url decode
def urlDecode(input):
    decode = unquote(input)
    print("URL Decode: "+decode)


def main():
    enOrDe = input(" Enter 'Encode' 'Decode' 'url' 'q' (to quit)? ")
    enOrDeInput = enOrDe.lower()
    try:
        while enOrDeInput != 'q':
            if enOrDeInput == 'encode':
                inputAsciiEncode = input("Enter ASCII: ")
                asciiEncode(inputAsciiEncode)
            elif enOrDeInput == 'decode':
                inputAsciiDecode = input("Enter win1252: ")
                asciiDecode(inputAsciiDecode)
            elif enOrDeInput == 'url':
                i = input("'encode' or 'decode'?")
                inputURL = i.lower()
                if inputURL == 'encode':
                    en = input("Encode: ")
                    urlEncode(en)
                elif inputURL == 'decode':
                    de = input("Decode: ")
                    urlDecode(de)
                else:
                    print("Err.")
            else:
                print("Err, Try again.")
            enOrDe = input(" Enter 'Encode' 'Decode' 'url' 'q' (to quit)? ")
            enOrDeInput = enOrDe.lower()
    except Exception:
        print("Err. ")


