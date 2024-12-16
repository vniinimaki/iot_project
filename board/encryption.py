import aesio
key = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6])
DEBUG = 0
CHUNKSIZE = 16
#iv = [119,241,17,59,208,205,213,198,240,107,22,55,238,63,191,159] /// Needed for other modes
cipher = aesio.AES(key, aesio.MODE_ECB)
def encrypt_message(message):
    inp = bytes(message, 'utf-8')
    #Padding to 16 bytes
    len_diff = CHUNKSIZE - len(inp)
    inp += "\0" * len_diff
    outp = bytearray(len(inp))
    cipher.encrypt_into(inp, outp)
    if (DEBUG):
        print(outp)
        outp2 = bytearray(len(inp))
        cipher.decrypt_into(outp, outp2)
        print(outp2)
    return bytes(outp)

