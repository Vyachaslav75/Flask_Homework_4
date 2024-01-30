from random import randint

def fill_list():
    res = []
    for i in range(1000000):
        res.append(randint(1, 101))
    return res


if __name__ == '__main__':
    print(fill_list())