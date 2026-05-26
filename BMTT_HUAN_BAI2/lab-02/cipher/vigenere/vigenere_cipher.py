class VigenereCipher:

    @staticmethod
    def generate_key(text, key):

        key = list(key)

        if len(text) == len(key):
            return key

        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])

        return "".join(key)

    @staticmethod
    def encrypt_text(plain_text, key):

        plain_text = plain_text.upper()
        key = VigenereCipher.generate_key(
            plain_text,
            key.upper()
        )

        cipher_text = ""

        for i in range(len(plain_text)):

            if plain_text[i].isalpha():

                x = (
                    ord(plain_text[i]) +
                    ord(key[i])
                ) % 26

                x += ord('A')

                cipher_text += chr(x)

            else:
                cipher_text += plain_text[i]

        return cipher_text

    @staticmethod
    def decrypt_text(cipher_text, key):

        cipher_text = cipher_text.upper()

        key = VigenereCipher.generate_key(
            cipher_text,
            key.upper()
        )

        plain_text = ""

        for i in range(len(cipher_text)):

            if cipher_text[i].isalpha():

                x = (
                    ord(cipher_text[i]) -
                    ord(key[i]) + 26
                ) % 26

                x += ord('A')

                plain_text += chr(x)

            else:
                plain_text += cipher_text[i]

        return plain_text