from math import gcd
NUMBER = 20129388696149
x0 = 2
MAX_ITERATIONS = 11


def polinom(x):
    return (x * x + 1) % NUMBER


def start():
    array = [x0]
    for k in range(0, MAX_ITERATIONS):
        while len(array) < 2 ** (k+1)+1:
            array.append(polinom(array[len(array)-1]))
        for i in range(2**k + 1, 2**(k+1)+1):
            nod = gcd(abs(array[i]-array[2**k]), NUMBER)
            if nod != 1:
                print(nod)
                print(NUMBER / nod)
                print("Length of sequence, where p and q were found is:", i)
                print("Compared elements: ", i, "-th and ", 2**k, "-th", sep='')
                return


start()
