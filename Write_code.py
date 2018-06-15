while True:
    while True:
        try:
            size = int(input("Input word size: "))
            if size < 1:
                print("Please use an integer")
            else:
                break
        except ValueError:
            print("Please use an integer")

    for i in range(size):
        if i == 0 or i == size - 1:
            for j in range(4):
                if j == 2:
                    print("* " * (size - 1), end="")
                    print("  ", end="")
                else:
                    print("* " * size, end="")
                print("\t", end="")
            print()
        else:
            for j in range(4):
                if j == 0 or j == 3:
                    print("* ", end="")
                    if j == 3 and i == int((size - 1) / 2):
                        print("* " * (size - 1), end="")
                    else:
                        print("  " * (size - 1), end="")
                else:
                    print("* ", end="")
                    print("  " * (size - 2), end="")
                    print("* ", end="")
                print("\t", end="")
            print()


