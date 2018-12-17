# -*- coding: utf-8 -*-

import base64


def b64_decode(text):
    """Return base64 decoded string."""

    return base64.b64decode(text)

def xor(text, key):
    """Decrypt given string using single-byte XOR cipher."""

    return ''.join(chr(letter ^ key) for letter in text)

STRING = 'GCg7Ozs7Oy01e3oNMz4gP3ogP3ovPjs2NXoZM3opMz96KDUgKSAjPCg1LTs5\
ei4/MSkueiA7KSAjPCg1LTs0I3oqNTA/PiM0OSAjN3o4OzAuPzd0ehQ1ej41\
OCg7dno8Njs9O3ouNWB6CBUADRsWBSEJMzQ9Nj8CNSgYIy4/GTMqMj8oJw=='

MAX_SECRET_SIZE = 256
for i in range(MAX_SECRET_SIZE):
    decrypted_string = xor(b64_decode(STRING), i)
    if 'ROZWAL_{' in decrypted_string:
        print('Used secret key:', i)
        print('Decrypted string:\n', decrypted_string)
        break
