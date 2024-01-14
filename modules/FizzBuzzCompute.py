
def GetFizzBuzzResult(n1, n2, limit, str1, str2):

    fizz = str1
    buzz = str2
    fizzbuzz = str1+str2

    numsList = []

    for i in range(1, limit+1):
        if i % n1 == 0 and i % n2 == 0:
            numsList.append(fizzbuzz)
        elif i % n1 == 0:
            numsList.append(fizz)
        elif i % n2 == 0:
            numsList.append(buzz)
        else:
            numsList.append(str(i))

    return ",".join(numsList)


if __name__ == "__main__":
    pass
