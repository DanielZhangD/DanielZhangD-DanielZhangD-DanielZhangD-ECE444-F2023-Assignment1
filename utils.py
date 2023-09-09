def reversed(number):
    ret = 0
    negative = 1
    if (int(number) != number):
        raise TypeError()
    if (number < 0):
        number *= -1
        negative = -1
    while (number > 0):
        ret = ret * 10 + number % 10
        number = number // 10
    return ret * negative

def formatter(number):
    return (bin(number), oct(number))

if __name__ == '__main__':
    print(reversed(1.123))