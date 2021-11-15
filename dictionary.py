words = []


def check(word):
    if word in words:
        return True
    else:
        return False


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.append(line.rstrip())
    return True


def size():
    n = 0
    for word in words:
        n += 1
    return n


def unload():
    return True
