# viết thuật toán kiểm tra xem 1 str có phải unique str hay không

# dùng list
def uniqueStr():
    str2 = []
    for i in str:
        if i in str2:
            return False
        str2.append(i)
    return True

# dùng dictionary


def uniqueStr1():
    str2 = {}
    for i in str:
        if i in str2:
            return False
        str2[i] = 1
    return True


if __name__ == "__main__":
    str = "abcd"
    print(uniqueStr())
    print(uniqueStr1())
