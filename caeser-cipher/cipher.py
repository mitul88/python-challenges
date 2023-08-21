alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    enc_word = ""
    for t in plain_text:
        idx = alphabet.index(t)
        if idx + shift_amount < len(alphabet):
            enc_word += alphabet[idx + shift_amount]
        else:
            extra_idx = idx + shift_amount - len(alphabet)
            enc_word += alphabet[extra_idx]
            # print(f"given len is greater by {extra_idx}")

    print(enc_word)


def decrypt(plain_text, shift_amount):
    dec_word = ""
    for t in plain_text:
        idx = alphabet.index(t)
        if idx - shift_amount < 0:
            out_ranged_idx = shift_amount - idx
            dec_word += alphabet[-out_ranged_idx]
        else:
            dec_word += alphabet[idx - shift_amount]
    print(dec_word)


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
else:
    print('Type "encode" to encrypt or "decode" to decrypt')


#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"


