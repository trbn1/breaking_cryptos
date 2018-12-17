with open('text.txt', 'r') as f:
    text = list(f.read())

# calculate frequency of letters in given text
counter = 0
freq = [0 for x in range(26)]
for c in text:
    for i in range(65, 92):
        if i is ord(c):
            freq[i - 65] = freq[i - 65] + 1
    for i in range(97, 123):
        if i is ord(c):
            freq[i - 97] = freq[i - 97] + 1
    counter += 1

string = list('abcdefghijklmnopqrstuvwxyz')

print('Letter, Freq in %')
for i, f in enumerate(freq):
    print(string[i], ': ', round((f / counter) * 100, 2))

# swap letters
for i, c in enumerate(text):
    # from knowledge
    if c is 'K':
        text[i] = 'R'
    if c is 'U':
        text[i] = 'O'
    if c is 'W':
        text[i] = 'Z'
    if c is 'Q':
        text[i] = 'W'
    if c is 'J':
        text[i] = 'A'
    if c is 'G':
        text[i] = 'L'

    # lowercase is the same
    if c is 'k':
        text[i] = 'r'
    if c is 'u':
        text[i] = 'o'
    if c is 'w':
        text[i] = 'z'
    if c is 'q':
        text[i] = 'w'
    if c is 'j':
        text[i] = 'a'
    if c is 'g':
        text[i] = 'l'

    # from frequency analysis
    if c is 'S':
        text[i] = 'E'
    if c is 's':
        text[i] = 'e'
    if c is 'B':
        text[i] = 'T'
    if c is 'b':
        text[i] = 't'

    # from knowledge of words
    if c is 'L':
        text[i] = 'I'
    if c is 'l':
        text[i] = 'i'
    if c is 'R':
        text[i] = 'K'
    if c is 'r':
        text[i] = 'k'
    if c is 'Y':
        text[i] = 'F'
    if c is 'y':
        text[i] = 'f'
    if c is 'T':
        text[i] = 'C'
    if c is 't':
        text[i] = 'c'
    if c is 'I':
        text[i] = 'N'
    if c is 'i':
        text[i] = 'n'
    if c is 'C':
        text[i] = 'S'
    if c is 'c':
        text[i] = 's'
    if c is 'E':
        text[i] = 'Y'
    if c is 'e':
        text[i] = 'y'
    if c is 'O':
        text[i] = 'V'
    if c is 'o':
        text[i] = 'v'
    if c is 'V':
        text[i] = 'G'
    if c is 'v':
        text[i] = 'g'
    if c is 'D':
        text[i] = 'H'
    if c is 'd':
        text[i] = 'h'
    if c is 'P':
        text[i] = 'U'
    if c is 'p':
        text[i] = 'u'
    if c is 'N':
        text[i] = 'D'
    if c is 'n':
        text[i] = 'd'
    if c is 'X':
        text[i] = 'J'
    if c is 'x':
        text[i] = 'j'
    if c is 'Z':
        text[i] = 'B'
    if c is 'z':
        text[i] = 'b'
    if c is 'F':
        text[i] = 'P'
    if c is 'f':
        text[i] = 'p'
    if c is 'A':
        text[i] = 'X'
    if c is 'a':
        text[i] = 'x'
    # m = m
    # h = 0%

print()  
print(''.join(text))