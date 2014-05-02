def checkio(first, second):
    firset_set = set(first.strip().split(','))
    second_set = set(second.strip().split(','))
    result = []
    for s in firset_set:
        if s in second_set: 
            result.append(s)
    return ",".join(sorted(result))

def checkio2(first, second):
    """
    set data type has useful methods.
    """
    first_set, second_set = set(first.split(",")), set(second.split(","))
    common = first_set.intersection(second_set)
    return ",".join(sorted(common))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
