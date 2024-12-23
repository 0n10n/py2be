from os.path import splitext


def get_suffix(filename, ignore_dot=True):
    return splitext(filename)[1][1:]

filename = '1jfkashdf.1.2.3'
print(get_suffix(filename))