
def decrypt(d, n, m):
    return (m ** d) % n


def decrypt_salaire():
    m = 1
    d = 1
    n = 1
    print(decrypt(d, n, m))


def decrypt_DH():
    m = 1
    d = 1
    n = 1
    print(decrypt(d, n, m))
