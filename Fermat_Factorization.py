from math import sqrt
PRIME_NUMS = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
              223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
              337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
              457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547]

NUMBER = 240316637260283
SIZE = len(PRIME_NUMS)


def get_quadratic_residue(number):
    qr_list = []
    for i in range(0, (number-1)//2 + 1):
        qr_list.append((i*i) % number)
    qr_list.sort()
    return qr_list


def build_column():
    column = []
    for i in range(0, SIZE):
        column.append((NUMBER + 1) % PRIME_NUMS[i])
    return column


def update_column(b, column):
    for i in range(0, SIZE):
        column[i] = (column[i] + 2*b + 1) % PRIME_NUMS[i]
    return column


def compare(column):
    for i in range(0, SIZE):
        num = column[i]
        qr = get_quadratic_residue(PRIME_NUMS[i])
        flag = False
        for j in range(0, len(qr)):
            if num == qr[j]:
                flag = True
                break
        if flag:
            continue
        else:
            return False
    return True


def start():
    temp = NUMBER + 1
    column = build_column()
    for i in range(1, NUMBER//2 + 1):
        if compare(column):
            print(i, temp, sqrt(temp))
            print(NUMBER, " = ", sqrt(temp) + i, "*", sqrt(temp) - i)
            return
        temp += 2*i + 1
        column = update_column(i, column)
    print("Not found")


start()
