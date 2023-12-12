
#10-2 1
def decimalToBinary(decimal):
    binary = bin(decimal)[2:]
    print("Binary: " + binary)

#2-10 2
def binaryToDecimal(binary):
    decimal = int(binary, 2)
    print("Decimal: " + str(decimal))

#10-16 3
def decimalTOHexadecimal(decimal):
    hexadecimal = hex(decimal)[2:]
    print("Hexadecimal: " + hexadecimal)

#16-10 4
def hexadecimalToDecimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    print("Decimal: " + str(decimal))

#10-8 5
def decimalToOctal(decimal):
    octal = oct(decimal)
    print("Octal: " + octal)
#8-10 6
def octalToDeciaml(octal):
    decimal = int(octal, 8)
    print("Decimal: " + str(decimal))

#2-16 7
def binaryToHexadecimal(binary):
    hexadecimal = hex(binary)[2:]
    print("Hexadecimal: " + hexadecimal)

#16-2 8
def hexadecimalToBinary(hex):
    binary = bin(hex)[2:]
    print("Binary: " + binary)

def main():
    print("1: decimal to binary, 10 -> 2.")
    print("2: binary to decimal, 2 -> 10.")
    print("3: decimal to hexadecimal, 10 -> 16.")
    print("4: hexadecimal to decimal, 16 -> 10.")
    print("5: decimal to octal, 10 -> 8.")
    print("6: octal to decimal, 8 -> 10.")
    print("7: binary to hexadecimal, 2 -> 16.")
    print("8: hexadecimal to binary, 16 -> 2.")
    ques = input("Enter # to converter, 'q' to quit: ")
    inputNum = ques.lower()
    try:
        while inputNum != 'q':
            if inputNum == '1':
                num = input("Enter a decimal #: ")
                one = int(num)
                decimalToBinary(one)
            elif inputNum == '2':
                num = input("Enter a binary #: ")
                two = str(num)
                binaryToDecimal(two)
            elif inputNum == '3':
                num = input("Enter a decimal #: ")
                three = int(num)
                decimalTOHexadecimal(three)
            elif inputNum == '4':
                num = input("Enter a hex #: ")
                four = str(num)
                hexadecimalToDecimal(four)
            elif inputNum == '5':
                num = input("Enter a decimal #: ")
                five = int(num)
                decimalToOctal(five)
            elif inputNum == '6':
                num = input("Enter an octal #: ")
                six = str(num)
                octalToDeciaml(six)
            elif inputNum == '7':
                num = input("Enter an binary #: ")
                seven = int(num, 2)
                binaryToHexadecimal(seven)
            elif inputNum == '8':
                num = input("Enter an hex #: ")
                eight = int(num, 16)
                hexadecimalToBinary(eight)
            elif inputNum == 'h':
                print(" ------------- Guideline ---------------------")
                print("1: decimal to binary, 10 -> 2.")
                print("2: binary to decimal, 2 -> 10.")
                print("3: decimal to hexadecimal, 10 -> 16.")
                print("4: hexadecimal to decimal, 16 -> 10.")
                print("5: decimal to octal, 10 -> 8.")
                print("6: octal to decimal, 8 -> 10.")
                print("7: binary to hexadecimal, 2 -> 16.")
                print("8: hexadecimal to binary, 16 -> 2.")
            else:
                print("Err, try again.")
            ques = input("Enter # to converter, 'q' to quit, 'h' for help: ")
            inputNum = ques.lower()
    except Exception:
        print("unexcept, Err.")


if __name__ == '__main__':
    main()
