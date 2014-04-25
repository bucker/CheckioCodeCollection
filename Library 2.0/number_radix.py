# def checkio(str_number, radix):
#     total = 0
#     power = 0
#     for s in reversed(str_number):
#         num = ord(s) - ord('A') + 10 if ord(s) >= ord('A') else int(s)
#         if num >= radix:
#             return -1
#         total += num * (radix**power)
#         power += 1
#     return total

# You can use the multiple arguments such as: *a 
def checkio(str_number,radix):
    try:
        return int(str_number,radix)
    except ValueError:
        return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
