# Write a Python function to calculate the area of a rectangle given its length and width.
def main():
    length = get_length()
    width = get_width()
    area = get_area(length, width)
    print("The area of the rectangle is", area)

def get_length():
    while True:
        try:
            l = int(input("What's the length of the rectangle? "))
            if l > 0:
                return l
            else:
                print("Length must be a positive integer ")
        except ValueError:
            print("That is not an integer")

def get_width():
    while True:
        try:
            w = int(input("What's the width of the rectangle? "))
            if w > 0:
                return w
            else:
                print("Width must be a positive integer")
        except ValueError:
            print("That is not an integer ")

def get_area(length, width):
    return length * width

main()