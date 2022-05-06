import random


def generate_mobile():
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        num = random.randint(1, 9)
        phone += str(num)
    return phone


if __name__ == '__main__':
    print(generate_mobile())