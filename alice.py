# -*- coding: utf-8 -*-

import base64

from itertools import cycle


def b64_decode(text):
    """Return base64 decoded string."""

    return base64.b64decode(text).decode()

def find_key_length(text):
    """Calculate indexes of coincidence for key lengths (1, 50).
    https://crypto.stackexchange.com/a/35355
    """
    for step in range(1, 50):
        match = total = 0
        for a in range(len(text)):
            for j in range(a + step, len(text), step):
                total += 1
                if text[a] == text[j]:
                    match += 1

        ioc = float(match) / float(total)

        if 100 * ioc > 5:
            print('%2d%7.2f%%' % (step, 100 * ioc))


def xor(text, key):
    """Decrypt given string using multi-byte XOR cipher."""

    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, cycle(key)))


if __name__ == '__main__':
    STRING = b64_decode('PAADREshCgcRDgZPBAoPSxgGBBEOAR0ABksVEUUeDw4YCksoBlQWAg5PBgoRGBUNAxkEGBUGS\
    x8KGkUfDgQHEUVLIgEWAgoDVAoFSw0NBksFBhEGBEsLGBARGBUNSUsKDQ1FBgQVGAwcDk8WHA\
    cETwQXEQ4fBgocCgsOAAUCClQADQ4EABwcBQoTCksKGxUOHkVPOQoRDk8eABgRDA4ASx8dGwY\
    DDk8EBA8PBhoCHksVEQcSSwEdAEsJFhgKSxEOVBEZHgsaCkVLIB9JSw0DFQIKSxsbRTkkNSMk\
    JzQUNQkCCAo9FiIGHwYAGBgKEBg=')

    #find_key_length(STRING) # -> key length most likely = 5

    # known part of encrypted plaintext
    KNOWN = 'OZWAL' # ROZWAL -> ROZWA or OZWAL -> OZWAL gives good result

    LIST_STRING = list(STRING)
    LIST_KNOWN = list(KNOWN)

    KEYS = []

    for i in range(len(LIST_STRING) - len(LIST_KNOWN)):
        decrypted_string = xor(KNOWN, STRING[i:])
        KEYS.append(decrypted_string)

    for k in KEYS:
        decrypted_string = xor(STRING, k)
        if 'ROZWAL_{' in decrypted_string:
            print('Used secret key:', k)
            print('Decrypted string:\n', decrypted_string)
            break
