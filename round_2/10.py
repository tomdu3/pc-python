# Custom String Formatter: Create a function that takes a string and
# capitalizes every other letter in the string.

def capitalize_every_other(text):
    change = False
    new_text = ''
    while True:
        if len(text) == 0:
            break
        else:
            if text[0] == ' ':
                new_text += ' '
                text = text[1:]
                continue
            elif change == False:
                new_text += text[0].lower()
                change = True
            else:
                new_text += text[0].upper()
                change = False
        text = text[1:]
    return new_text


print(capitalize_every_other('hello world'))
