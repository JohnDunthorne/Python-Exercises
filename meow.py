def main():
    print("how many times would you like the cat to meow?")
    number_of_meows()


def number_of_meows():
    for _ in range(int(input("select number: "))):
        print("meow")


if __name__ == "__main__":
    main()
