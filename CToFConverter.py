# đổi độ C sang độ F


def cToFConverter():

    while True:
        C = input("Please enter C degree: ")
        if C.isdigit() == False:
            print("you have to enter a number")
            continue
        elif C:
            C = float(C)
            F = 9*C/5+32
            print(f"{C}C is converted to {F}F")
            break


def main():
    cToFConverter()


if __name__ == "__main__":
    main()
