class PlayFairCipher:
    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        seen = set()
        matrix_list = [char for char in key if not (char in seen or seen.add(char))]
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in seen:
                matrix_list.append(char)
        return [matrix_list[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def split_pairs(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    pairs.append(a + "X")
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + "X")
                i += 1
        return pairs

    def playfair_encrypt(self, plain_text, matrix):
        pairs = self.split_pairs(plain_text)
        encrypted_text = ""
        for pair in pairs:
            r1, c1 = self.find_letter_coords(matrix, pair[0])
            r2, c2 = self.find_letter_coords(matrix, pair[1])
            if r1 == r2:
                encrypted_text += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                encrypted_text += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                encrypted_text += matrix[r1][c2] + matrix[r2][c1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            r1, c1 = self.find_letter_coords(matrix, pair[0])
            r2, c2 = self.find_letter_coords(matrix, pair[1])
            if r1 == r2:
                decrypted_text += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                decrypted_text += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
            else:
                decrypted_text += matrix[r1][c2] + matrix[r2][c1]
        
        # Xử lý loại bỏ 'X' đệm theo logic bạn đã viết
        banro = ""
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i + 2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i + 1]
        
        if len(decrypted_text) >= 2:
            if decrypted_text[-1] == "X":
                banro += decrypted_text[-2]
            else:
                banro += decrypted_text[-2] + decrypted_text[-1]
                
        return banro