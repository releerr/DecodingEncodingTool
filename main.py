# main page for all kinds of encode/decode method.

from Methods import Base64, Conversion, URL, Hash, Railfence

if __name__ == '__main__':
    print("------- Algorithms ----------------------------")
    print("url: URL decode/encode, ASCII - win1252. ")
    print("con: Converter to all kinds of Binary/Decimal/Hex/Octal. ")
    print("64: base64.")
    print("hash: hash for md5. ")
    print("r: Rail Fence. ")
    print("-----------------------------------------------")
    alg = input("--Which algorithms? 'q' to quit. ")
    algInput = alg.lower()
    try:
        while algInput != 'q':
            if algInput == 'url':
                URL.main()
            elif algInput == 'con':
                Conversion.main()
            elif algInput == '64':
                Base64.main()
            elif algInput == 'hash':
                Hash.main()
            elif algInput == 'r':
                Railfence.main()
            else:
                print("Err, try again!")
            alg = input("--Which algorithms? 'q' to quit. ")
            algInput = alg.lower()
    except Exception:
        print("Err. ")
