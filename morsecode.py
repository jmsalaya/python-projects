from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY


morseCode = { 'A':'.-', 'B':'-...',
              'C':'-.-.', 'D':'-..', 'E':'.',
              'F':'..-.', 'G':'--.', 'H':'....',
              'I':'..', 'J':'.---', 'K':'-.-',
              'L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-',
              'R':'.-.', 'S':'...', 'T':'-',
              'U':'..-', 'V':'...-', 'W':'.--',
              'X':'-..-', 'Y':'-.--', 'Z':'--..',
              '1':'.----', '2':'..---', '3':'...--',
              '4':'....-', '5':'.....', '6':'-....',
              '7':'--...', '8':'---..', '9':'----.',
              '0':'-----', ', ':'--..--', '.':'.-.-.-',
              '?':'..--..', '/':'-..-.', '-':'-....-',
              '(':'-.--.', ')':'-.--.-'}

def encrypt(text):
    cipher = ''

    for i in text:
        if i != ' ':

            cipher += morseCode[i] + ' '

        else:
            cipher += ' '

    return cipher



def decrypt(text):
    text += " "

    decipher = ''
    citext = ''

    for i in text:

        if (i != ' '):
            x = 0

            citext += i

        else:
            x += 1

            if i == 2:

                decipher += ' '

            else:

                decipher += list(morseCode.keys())[list(morseCode.values()).index(citext)]
                citext = ''

    return decipher

def main():

    while True:
       
        message = input("text to morse code: ")
        result = encrypt(message.upper())
        print(result)
    
        morse_code = input("morse code to text: ")
        result = decrypt(morse_code)
        print(result)

        Continue = input("Do you wish to continue? (y/n): ").lower()
        if Continue == "n":
            break
      


        



        



        


if __name__ == '__main__':
    main()