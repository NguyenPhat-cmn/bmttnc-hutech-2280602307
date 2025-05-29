from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(self.alphabet)

    def encrypt_text(self, text: str, key: int) -> str:
        """
        Mã hóa văn bản bằng Caesar cipher với khóa key.
        """
        try:
            key = int(key)
        except ValueError:
            return "Lỗi: key phải là số nguyên"

        encrypted_text = []
        for letter in text:
            if letter.upper() in self.alphabet:
                letter_index = self.alphabet.index(letter.upper())
                output_index = (letter_index + key) % self.alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter if letter.isupper() else output_letter.lower())
            else:
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        """
        Giải mã văn bản bằng Caesar cipher với khóa key.
        """
        try:
            key = int(key)
        except ValueError:
            return "Lỗi: key phải là số nguyên"

        decrypted_text = []
        for letter in text:
            if letter.upper() in self.alphabet:
                letter_index = self.alphabet.index(letter.upper())
                output_index = (letter_index - key) % self.alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter if letter.isupper() else output_letter.lower())
            else:
                decrypted_text.append(letter)
        return "".join(decrypted_text)
