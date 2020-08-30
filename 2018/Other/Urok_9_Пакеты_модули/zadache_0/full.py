
import string

def simplify(text, whitespace=string.whitespace, delete=""):
    r"""Возвращает текст, из которого удалены лишние пробелы.
    Параметр whitespace - это строка символов, каждый из которых
    считается символом пробела.Если параметр delete не пустой,
    он должен содержать строку, и тогда все символы, входящие
    в состав строки delete, будут удалены из строки результата.
    >>> simplify(" this and\n that\t too")
    'this and that too'
    >>> simplify(" Washington D.C.\n")
    'Washington D.C.'
    >>> simplify(" Washington D.C.\n", delete=",;:.")
    'Washington DC'
    >>> simplify(" disemvoweled ", delete="aeiou")
    'dsmvwld'
    """
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
    return " ".join(result)
    

def shorten(text, length=25, indicator="..."):
    """Возвращает text или усеченную его копию с добавлением indicator в конце
    text &#8211; любая строка; 
    length &#8211; максимальная длина возвращаемой строки string (включая indicator); 
    indicator &#8211; строка, добавляемая в конец результата, чтобы показать, что текст аргумента text был усечен
    >>> shorten("The Road")
    'The Road'
    >>> shorten("No Country for Old Men", 20)
    'No Country for Ol...'
    >>> shorten("Cities of the Plain", 15, "*")
    'Cities of the *'
    """
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text


def is_balanced(text, brackets="()[]{}<>"):
    """
    Проверяет баланс открывающих и закрывающих скобок в text.
    """
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"

    left = brackets[::2]
    right = brackets[1::2]
    print('left = {} and right = {} '.format(left, right))
    stack = []
    for c in text:
    	if c in left:
    		stack.append(c)
    		#print ('stack : ',stack)
    	elif c in right:
    		#print ('last_ : ',stack[-1])
    		stack.pop()

    return stack

if __name__ == "__main__":
    #import doctest      # import, который нужен только для тестирования, пишем прямо тут
    #doctest.testmod()   # выполним примеры (как - расскажем дальше)
    s = "qq((jjj()adf"
    print('\n\n',s,'\t\t',is_balanced(s))

    #s = "{{()()}}"
    #print(s, is_balanced(s))

