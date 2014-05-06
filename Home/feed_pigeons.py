def checkio(food):
    next_pigeon_number = 1
    total_pigeons = 0

    while food > total_pigeons + next_pigeon_number:
        total_pigeons += next_pigeon_number
        food -= total_pigeons
        next_pigeon_number += 1

    return max(food, total_pigeons)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(3) == 2, "XD example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"