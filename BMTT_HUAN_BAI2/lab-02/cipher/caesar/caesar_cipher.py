from .alphabet import LOWERCASE, UPPERCASE

class CaesarCipher:
    @staticmethod
    def encrypt_text(plain_text, key):
        cipher_text = ""
        for char in plain_text:
            if char in LOWERCASE:
                index = LOWERCASE.index(char)
                cipher_text += LOWERCASE[(index + key) % 26]
            elif char in UPPERCASE:
                index = UPPERCASE.index(char)
                cipher_text += UPPERCASE[(index + key) % 26]
            else:
                cipher_text += char
        return cipher_text

    @staticmethod
    def decrypt_text(cipher_text, key):
        plain_text = ""
        for char in cipher_text:
            if char in LOWERCASE:
                index = LOWERCASE.index(char)
                plain_text += LOWERCASE[(index - key) % 26]
            elif char in UPPERCASE:
                index = UPPERCASE.index(char)
                plain_text += UPPERCASE[(index - key) % 26]
            else:
                plain_text += char
        return plain_text