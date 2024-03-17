import csv


def get_apikey():
    with open('tests/keys.csv', 'r') as file:
        csv_file = csv.reader(file, delimiter=';')
        data = list(csv_file)
        data = list(filter(lambda x: x, data))
        my_keys = {k: int(v) for k, v in data if k and v}
    for k, v in my_keys.items():
        if v != 0:
            my_keys[k] -= 1
            with open('tests/keys.csv', 'w') as file:
                csv_file = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                csv_file.writerows(list(my_keys.items()))
            print(f"{k}: {my_keys[k]}")
            return k


def drop_file():
    file = csv.reader(open('keys.csv', 'r'), delimiter=';')
    data = list(file)
    data = list(filter(lambda x: x, data))
    data = list(map(lambda x: [x[0], "200"], data))
    w_file = csv.writer(open('keys.csv', 'w'), delimiter=';', quoting=csv.QUOTE_MINIMAL)
    w_file.writerows(data)


if __name__ == '__main__':
    drop_file()