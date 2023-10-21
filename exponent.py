def exponent(base, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base
    return result

print(exponent(5, 3))