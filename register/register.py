
"""
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(k, ciphertext):
    plaintext = ""
    for c in ciphertext:
        if c == " ":
            plaintext = plaintext + " "
        else:
            i = ((ALPHABET.index(c) - k) % 26)
            plaintext = plaintext + ALPHABET[i]
    print("The plaintext is: ", plaintext)

if __name__ == "__main__":

    ciphertext = "VODP VHFWLRQ RIWHQ HQWHU"
    for k in range(26):
        decrypt(k, ciphertext)
    
    pass
"""
ciphertext = "VODP VHFWLRQ RIWHQ HQWHU"

for shift in range(1, 26):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += " "
    print(f"Shift {shift}: {decrypted}")
