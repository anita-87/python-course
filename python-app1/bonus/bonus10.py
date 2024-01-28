try:
    width = float(input("Enter the rectangle width: "))
    length = float(input("Enter the rectangle length: "))

    if width == length:
        exit("That looks like a square.")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number.")
