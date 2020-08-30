
import string

def simplify(text, whitespace=string.whitespace, delete=""):
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
            else:
            	word += char
    if word:
        result.append(word)
    print (" ".join(result))
    return " ".join(result)
    

def shorten(text, length=25, indicator="..."):
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text















