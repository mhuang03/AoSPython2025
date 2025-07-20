alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def reverse_cipher(message: str):
    return message[::-1]


def affine_cipher_encrypt(message: str, a: int, b: int):
    m_upper = message.upper()
    return "".join([
        alph[(a * (ord(c) - ord("A")) + b) % 26] if c in alph else c for c in m_upper
    ])


def rail_fence_encrypt(message: str, k: int):
    alph_only = [c for c in message.upper() if c in alph]
    rails = [[] for _ in range(k)]
    i = 0
    d = 1
    for c in alph_only:
        rails[i].append(c)

        next_i = i + d
        if next_i >= k:
            d = -d
        elif next_i < 0:
            d = -d
        i = i + d

    return "".join([c for i in range(k) for c in rails[i]])


def rail_fence_decrypt(message: str, k: int):
    chars = iter(message)
    message_len = len(message)
    period = 2*k - 2

    decrypted = ["" for _ in range(len(message))]
    for i in range(k):
        for j in range(i, message_len, period):
            decrypted[j] = next(chars)
            if i == 0 or i == k-1:
                continue

            back_i = j + period - 2 * i
            if back_i < message_len:
                decrypted[back_i] = next(chars)

    return "".join(decrypted)


if __name__ == "__main__":
    m = "SEND HELP IMMEDIATELY. NO MORE SNACKS."
    print(reverse_cipher(m))
    print(affine_cipher_encrypt(m, 2, 3))

    rail_encrypted = rail_fence_encrypt(m, 3)
    print(rail_encrypted)
    print(rail_fence_decrypt(rail_encrypted, 3))
