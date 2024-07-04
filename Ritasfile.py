alphabet = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё """
def transposition(message: str, key : str, alphabet: str, encode = True):
    sorted_key = sorted(set(key))
    colls = len(key)
    rows = (len(message)+colls-1)//colls
    key = [key.index(i) for i in (sorted_key)]
    encrypted = []
    if encode:
        message = [message[0+colls*i:(i+1)*colls] for i in range((len(message)+colls-1)//colls)]
    else:
        decrypted = []
        message_iter = iter(message)
        for row in range(colls):
            s = ''
            for coll in range(rows if row not in key[colls - (colls*rows-len(message)):] else rows - 1):
                s+= next(message_iter)
            decrypted.append(s)
        decrypted = [dict(zip(key, decrypted))[i] for i in range(colls)]
        message = decrypted
    for i in key if encode else range(rows):
        enc = ''
        for part in message:
            if i < len(part):
                enc += part[i]
        encrypted.append(enc)
    return ''.join(encrypted)
    
if __name__ == "__main__":
    print(transposition("THISISWIKIPEDIA", 'cipher', alphabet))
    print(transposition('TWDIPSIHIIIKASE', 'cipher', alphabet, False))
    a = transposition('СЕГОДНЯ ЧЕТВЕРГ', '53124', alphabet)
    print(a)
    print(transposition(a, '53124', alphabet, False))
