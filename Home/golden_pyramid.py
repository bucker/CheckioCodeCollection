def count_gold(pyramid):
    # save the max possible sum to the current layer
    layer_max = []
    for layer in range(len(pyramid)):
        this_layer = []
        for n in range(len(pyramid[layer])):
            if layer == 0:
                this_layer.append(pyramid[layer][n])
            elif n == 0:
                this_layer.append(layer_max[n] + pyramid[layer][n])
            elif n == len(pyramid[layer]) - 1:
                this_layer.append(layer_max[n-1] + pyramid[layer][n])
            else:
                this_layer.append(max(layer_max[n-1], layer_max[n]) + pyramid[layer][n])
        layer_max = this_layer

    return max(layer_max)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
