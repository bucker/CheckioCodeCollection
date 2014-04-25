def checkio(words):
    counter = 0
    for word in words.split(' '):
        if word.isalpha():
            counter += 1
            if counter >= 3:
                return True
        elif word.isdigit():
            counter = 0
    return counter >= 3

checkio2=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())

if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
