import string
import keyword
s = input('entered text')
bad_symbol = False
for i in range(len(s)):
    if s[i].isupper():
        bad_symbol = True
        break
    elif s[i] == ' ':
        bad_symbol = True
        break
    elif s[i] in string.punctuation and s[i] != '_':
        bad_symbol = True
        break
if not bad_symbol:
    if s in keyword.kwlist:
        print(False)
    elif s[0].isnumeric():
        print(False)
    else:
        print(True)
else:
    print(False)

