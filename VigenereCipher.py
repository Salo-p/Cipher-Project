class VigenereCipher:
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        letter = letter.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if forward == True:
          current_index = alphabet.index(letter)
          new_index = (current_index + shift) % 26

          shifted_letter = alphabet[new_index].upper()

        else:
          current_index = alphabet.index(letter)
          new_index = (current_index - shift) % 26
          shifted_letter = alphabet[new_index].upper()

        return shifted_letter

    def __generate_shift_list(self, plaintext_length: int):
        shift_list = []

        keywordRepeated = self.keyword * (plaintext_length//len(self.keyword) + 1)

        for i in range(plaintext_length):
          shift_list.append(ord(keywordRepeated[i]) - self.offset)

        return shift_list

    def encrypt(self, plaintext: str):
        plaintext = plaintext.upper()
        plaintext = ''.join(i for i in plaintext if i.isalpha())

        shift_list = self.__generate_shift_list(len(plaintext))

        cipherlist = []

        for i in range(len(plaintext)):
            cipherlist.append(self.__shift_letter(plaintext[i], shift_list[i], True))


        ciphertext = ''.join(i for i in cipherlist)
        return ciphertext

    def decrypt(self, ciphertext: str):

        ciphertext = ciphertext.upper()
        ciphertext = ''.join(i for i in ciphertext if i.isalpha())

        shift_list = self.__generate_shift_list(len(ciphertext))

        plainlist = []

        for i in range(len(ciphertext)):
            plainlist.append(self.__shift_letter(ciphertext[i], shift_list[i], False))


        plaintext = ''.join(i for i in plainlist)
        return plaintext


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()
