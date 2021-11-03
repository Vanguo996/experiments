
import time
from random import randint


def generate():
    i = 20
    value1 = 100
    value2 = 50
    t = 0
    while i:
        value1 += randint(0, 10)
        value2 += randint(0, 10)

        data = '{},{},{}\n'.format(t, value1, value2)
        print(data)
        i -= 1
        t += 1
        time.sleep(1)

if __name__ == '__main__':
    generate()
    