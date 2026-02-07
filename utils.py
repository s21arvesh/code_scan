def complex_function(a, b, c):
    result = 0
    if a > 0:
        if b > 0:
            if c > 0:
                result += 1
            else:
                result -= 1
        else:
            if c > 0:
                result += 2
            else:
                result -= 2
    else:
        if b > 0:
            result += 3
        else:
            result -= 3

    for i in range(10):
        if i % 2 == 0:
            result += i
        else:
            result -= i

    return result
