import string

plainText = input("Enter some plaintext: ")
shift = int(input("Enter the shift key value: "))
shift %= 26

# uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def shift_cipher(plainText, shift):
    cipherText = ""

    for c in plainText:
        alphabet = string.ascii_letters
        shifted = alphabet[shift:] + alphabet[:shift]

        table = str.maketrans(alphabet, shifted)
        cipherText = plainText.translate(table)

    print("Cipher text: ", cipherText)
shift_cipher(plainText, shift)


