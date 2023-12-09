import string
text = input('')
text = text.title()
for symbol in string.punctuation:
    text = text.replace(symbol, '')
    for i in range(len(text)):
        text = text.replace(' ', '')
text = '#' + text
print(text[0:139])










