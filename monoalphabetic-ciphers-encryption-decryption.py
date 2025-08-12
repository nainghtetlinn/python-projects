cipher_text = "abcdefghijklmnopqrstuvwxyz"
key = 15

plain_text = input("Enter text to encrypt: ")

encrypted_text = ""
decrypted_text = ""

for c in plain_text:
    index = cipher_text.find(c)
    index += key
    index %= cipher_text.__len__()
    encrypted_text += cipher_text[index]

print("Encrypted text: ", encrypted_text)

for c in encrypted_text:
    index = cipher_text.find(c)
    index -= key
    if index < 0:
        index += cipher_text.__len__()
    decrypted_text += cipher_text[index]

print("Decrypted text: ", decrypted_text)
