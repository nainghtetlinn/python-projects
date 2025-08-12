cipher_text = "abcdefghijklmnopqrstuvwxyz"
key = 12

plain_text = "attackistoday"

encrypted_text = ""
decrypted_text = ""

last_key = -1

for c in plain_text:
    index = cipher_text.find(c)
    temp = 0
    if last_key < 0:
        temp = index + key
    else:
        temp = index + last_key

    temp %= cipher_text.__len__()
    encrypted_text += cipher_text[temp]

    last_key = index

print("Encrypted text: ", encrypted_text)

last_key = -1

for c in encrypted_text:
    index = cipher_text.find(c)
    temp = 0
    if last_key < 0:
        temp = index - key
    else:
        temp = index - last_key

    temp %= cipher_text.__len__()
    decrypted_text += cipher_text[temp]

    last_key = temp

print("Decrypted text: ", decrypted_text)
