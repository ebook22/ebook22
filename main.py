ciag = int(input("enter fibonacci sequence length: "))


def get_fibonacci(c):
    d = []
    for i in range(c):
        if i <= 1:

            d.append(i)
            print(d[i])
        else:
            d.append(d[i-2]+d[i-1])
            print(d[i])
            if i == c-1:
                break


get_fibonacci(ciag)
