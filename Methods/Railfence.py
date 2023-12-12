

#加密
def railfenceEncrypt(text,num_rows):
    if num_rows == 1:
        return text
    rows = ['']*num_rows
    row = 0 #第几行
    for ch in text:
        rows[row] += ch
        # print("rows["+str(row)+"]: "+rows[row])
        if row == num_rows -1: #if row = 最后一行
            row = -1
        row += 1
        # print("row+1: " + str(row))
    print(''.join(rows))

# w型加密
def wEncrypt(text, num_rows):
    if num_rows ==1:
        return text
    rows = ['']*num_rows
    row = 0
    direction = -1
    for ch in text:
        rows[row] += ch
        if row == 0 or row == num_rows-1:
            direction *= -1
        row +=direction
    print(''.join(rows))

#解密
def railfenceDecrypt(text,num_rows):
    # m = []
    if num_rows ==1:
        return text
    if len(text) % 2 != 0:
        text_len = len(text)+1
    index = text_len//num_rows
    row = 0
    rows = ['']*num_rows
    for ch in text:
        rows[row] += ch
        if len(rows[row]) > index-1:
            row +=1

    # print("rows[0]: "+rows[0])
    # print("rows[1]: " + rows[1])
    # print("rows[2]: " + rows[2])

    result = ""
    for i in range(index):
        for j in range(len(rows)):
            result += rows[j][i]
    print(result)

# W型解密
def wDecrypt(ciphertext, num_rows):
    if num_rows == 1:
        return ciphertext
    cycle_length = 2 * (num_rows - 1)
    text_length = len(ciphertext)
    decrypted_text = [''] * text_length

    index = 0
    for row in range(num_rows):
        step1 = (cycle_length - 2 * row) if (cycle_length - 2 * row) != 0 else cycle_length
        # step2 = (2 * row) if (2 * row) != 0 else cycle_length
        j = row
        while j < text_length:
            decrypted_text[j] = ciphertext[index]
            index += 1
            if step1 != cycle_length and j + step1 < text_length:
                decrypted_text[j + step1] = ciphertext[index]
                index += 1
            j += cycle_length

    print(''.join(decrypted_text))


def main():
    print("Railfence -  1:encrypt, 2: decrypt, 3: w型encrypt, 4: w型decrypt. ")
    railFin = input("Enter: ")
    if railFin == '1':
        m = input("Enter text:")
        key = input("Enter num of rows:")
        railfenceEncrypt(m,int(key))
    elif railFin == '2':
        m = input("Enter text: ")
        key = input("Enter num of rows: ")
        railfenceDecrypt(m, int(key))
    elif railFin == '3':
        m = input("Enter text: ")
        key = input("Enter num of rows: ")
        wEncrypt(m, int(key))
    elif railFin == '4':
        m = input("Enter text: ")
        key = input("Enter num of rows: ")
        wDecrypt(m, int(key))


if __name__ == '__main__':
    main()