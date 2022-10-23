import rsa

def rsaEncryptor(str):
    (public_key, private_key) = rsa.newkeys(512)
    print("-------------------------------------")
    text_for_cipher = str.encode('utf-8')
    encr_text = rsa.encrypt(text_for_cipher, public_key)
    return (encr_text, private_key)


def rsaDecryptor(str, private_key):
    text_for_cipher = rsa.decrypt(str, private_key)
    decr_text = text_for_cipher.decode('utf-8')
    return decr_text


print("-------------------------------------")
text = input("Введіть текст для шифрування: \n")


if __name__ == '__main__':
    str, private_key = rsaEncryptor(text)

print('Зашифрований текст:', str, "\n")


# Decryption
decrypted_text = rsaDecryptor(str, private_key)
print('Відкритий текст після розшифрування:', decrypted_text)
print("-------------------------------------")

if text == decrypted_text:
    print("Шифрування і дешифрування пройшло успішно!")
else:
    print("Помилка в шифруванні/дешифруванні!")