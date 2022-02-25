x = [42]

def print_x():
    inner()
    print(x)

def inner():
    print("hello")

if __name__ == "__main__":
    print_x()

    print(__name__)