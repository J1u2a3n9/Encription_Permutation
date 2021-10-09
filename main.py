from io import open
import os
import matplotlib.pyplot as mpl

def transposition_encryption():
    os.system('clear')
    # Read file
    txtFile = open('plain text.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ").upper()

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

    # Delete special characters
    final_plain_text = ""
    for pt in plain_text:
        if pt.upper() in alphabet:
            final_plain_text += pt.upper()
        else:
            if pt == " ":
                final_plain_text += " "
            else:
                final_plain_text += ""

    print("========== Plain text ==========\n\n", final_plain_text)

    # print(msg)
    keyin = input("\n~# KEY: ").upper()
    paddingin = input("\n~# PADDING [a-z]: ").lower()

    key = ''
    padding = ''
    if keyValidate(keyin):
        key = keyin
    else:
        exit()
    if paddingValidate(paddingin):
        padding = paddingin
    else:
        exit()

    msg = final_plain_text.replace(" ", padding)

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    print("\n\n========== Transposition grid ==========\n")
    # printing key
    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    # for
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    # for
    print("\n-------------------------")

    # in case characters don't fit the entire grid perfectly.
    extra_letters = len(msg) % len(key)
    # print(extraLetters)
    dummy_characters = len(key) - extra_letters
    # print(dummyCharacters)

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += padding
    # if

    # print(msg)

    num_of_rows = int(len(msg) / len(key))

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1
        # for
    # for

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()
    # for

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # cipher
    cipher_text = ""
    k = 0
    for i in range(len(key)):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        # if
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        # for
        k += 1
    # for

    print("\n\n========== Final Text Encrypted ==========\n")
    print(cipher_text+'\n\n')

    # Create output file
    outputFile = open('encrypted text.txt','w')
    outputFile.write(cipher_text)
    outputFile.close()
    createHistogram(cipher_text.replace(padding," "))

def transposition_decryption():
    os.system('clear')
    # Read file
    txtFile = open('encrypted text.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    tws = ""
    for fc in fileContent:
        tws += fc.replace("\n", " ")

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    alphabetM = "abcdefghijklmnñopqrstuvwxyz"

    # Replace returns by spaces
    encrypted_text = ""
    for fc in tws:
        if fc in alphabet:
            encrypted_text += fc.upper()
        elif fc in alphabetM:
            encrypted_text += " "
        else:
            encrypted_text += ""

    print("========== Encrypted text ==========\n\n", encrypted_text)

    msg = encrypted_text
    # print(msg)
    # print(msg)
    keyin = input("\n~# KEY: ").upper()

    key = ''
    if keyValidate(keyin):
        key = keyin
    else:
        exit()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    num_of_rows = int(len(msg) / len(key))

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    for i in range(len(msg)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = msg[itr]
            itr += 1
        if itr == len(msg):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])

    print("\n========== Decrypted text ==========\n")
    print(plain_text)

    # Create output file
    outputFile = open('decrypted text.txt','w')
    outputFile.write(plain_text)
    outputFile.close()

def keyValidate(key):
    alphabet = "12345678"

    if(len(key) > len(alphabet) or len(key) < 4):
        print("ERROR! THE KEY MUST BE EQUAL TO THE ALPHABET [4-8]")
        return False

    flag = 0
    for k in key:
        repeat = 0
        for l in key:
            if l in alphabet:
                if k == l:
                    repeat += 1
            else:
                flag += 1
            if repeat > 1:
                flag += 1

    if flag >= 1:
        print("\nERROR! A KEY NUMBER IS REPEATED OR IS INVALID")
        return False
    else:
        return True
# * ================================== *
# *         GENERATE HISTOGRAM         *
# * ================================== *

def createHistogram(plainText):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    A=0;B=0;C=0;D=0;E=0;F=0;G=0;H=0;I=0;J=0;K=0;L=0;M=0;N=0;Ñ=0;O=0;P=0;Q=0;R=0;S=0;T=0;U=0;V=0;W=0;X=0;Y=0;Z=0
    one=0;two=0;three=0;four=0;five=0;six=0;seven=0;eigth=0;nine=0;ten=0

    for cc in plainText:
        if cc in alphabet:
            if cc == 'A': A += 1
            if cc == 'B': B += 1
            if cc == 'C': C += 1
            if cc == 'D': D += 1
            if cc == 'E': E += 1
            if cc == 'F': F += 1
            if cc == 'G': G += 1
            if cc == 'H': H += 1
            if cc == 'I': I += 1
            if cc == 'J': J += 1
            if cc == 'K': K += 1
            if cc == 'L': L += 1
            if cc == 'M': M += 1
            if cc == 'N': N += 1
            if cc == 'Ñ': Ñ += 1
            if cc == 'O': O += 1
            if cc == 'P': P += 1
            if cc == 'Q': Q += 1
            if cc == 'R': R += 1
            if cc == 'S': S += 1
            if cc == 'T': T += 1
            if cc == 'U': U += 1
            if cc == 'V': V += 1
            if cc == 'W': W += 1
            if cc == 'X': X += 1
            if cc == 'Y': Y += 1
            if cc == 'Z': Z += 1
            if cc == '0': one += 1
            if cc == '1': two += 1
            if cc == '2': three += 1
            if cc == '3': four += 1
            if cc == '4': five += 1
            if cc == '5': six += 1
            if cc == '6': seven += 1
            if cc == '7': eigth += 1
            if cc == '8': nine += 1
            if cc == '9': ten += 1

    histogram = mpl.figure(u'FRECUENCY HISTOGRAM ON CIPHER TEXT')
    axis = histogram.add_subplot(111)

    aLabels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    num = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eigth,nine,ten]
    xx  = range(len(num))
    rects1 = axis.bar(xx,num,width=0.5,color = 'y',align='center')
    axis.set_xticks(xx)
    axis.set_xticklabels(aLabels)
    mpl.xlabel("Cipher Text")
    mpl.ylabel("Absolute Frecuency")

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            axis.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    mpl.show()

def paddingValidate(padding):
    alpha = "abcdefghijklmnñopqrstuvwxyz"
    flag = True
    if len(padding) > 1:
        print("ERROR! PADDING MUST BE A ONLY ONE CHARACTER")
        flag = False
    elif padding not in alpha:
        print("ERROR! PADDING MUST BE A LOWER CASE CHARACTER [a-z]")
        flag = False
    return flag

def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key)):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
            # if
        # for
    # for
    return num_loc

def keyword_num_assign(key):
    alpha = "12345678"
    kywrd_num_list = list(range(len(key)))
    # print(kywrdNumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init - 1
            # if
        # inner for
    # for
    return kywrd_num_list

def main():
    os.system('clear')
    option = int (input("========== Choose an option ==========\n1) Encrypt \n2) Decrypt\n\n"))

    if option == 1:
        transposition_encryption()
    elif option == 2:
        transposition_decryption()
    else:
        print("Incorrect option")

if __name__ == "__main__":
    main()